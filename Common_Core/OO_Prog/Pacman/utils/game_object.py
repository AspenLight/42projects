from .consts import (
    MARGIN,
    ANIM_STEP_MS,
    GHOST_ANIMATIONS,
    PLAYER_ANIMATIONS,
    IDLE,
    KEY_TO_DIR,
    VECTORS,
)
from mazegenerator.mazegenerator import MazeGenerator
from .system_data import State
from typing import Optional
import pygame
import copy
import random


class Node:
    def __init__(self) -> None:
        self.xy: tuple[int, int]
        self.val: int = 15
        self.contain: int = 0  # 0=nothing;1=pacgum;2=super_pacgum
        self.n: bool = False
        self.e: bool = False
        self.s: bool = False
        self.w: bool = False
        self.dist: int = -1

    def set_dir(self, node: int) -> None:
        if node & 1 == 0:
            self.n = True
        if node & 2 == 0:
            self.e = True
        if node & 4 == 0:
            self.s = True
        if node & 8 == 0:
            self.w = True

    def update_dist(self, d: int) -> None:
        if self.dist < 0 or d < self.dist:
            self.dist = d + 1

    def display_data(self) -> None:
        print(f"xy: {self.xy}")
        print(f"N: {self.n}")
        print(f"E: {self.e}")
        print(f"S: {self.s}")
        print(f"W: {self.w}")
        print(f"Dist: {self.dist}")


class Maze:
    def __init__(self, state: State) -> None:
        # 15 = all four walls set (bitmask); unused until walls are drawn
        self.grid: list[list[Node]] = []
        self.level: int = 0
        self.seed: int = 0

    def valid_dir(
        self,
        current_cell: pygame.Vector2,
        target_dir: pygame.Vector2,
    ) -> bool:
        cell: Node = self.grid[int(current_cell[1])][int(current_cell[0])]
        match (round(target_dir.x), round(target_dir.y)):
            case [0, -1]:
                return bool(cell.n)
            case [0, 1]:
                return bool(cell.s)
            case [-1, 0]:
                return bool(cell.w)
            case [1, 0]:
                return bool(cell.e)
            case _:
                return False

    def build_gums(self, state: State) -> None:
        random.seed(state.level_sys.seed)
        excluded = {
            (0, 0),  # ghost spawns (corners)
            (0, state.m_width - 1),
            (state.m_height - 1, 0),
            (state.m_height - 1, state.m_width - 1),
        }
        coords = random.sample(
            [
                (row, col)
                for row in range(len(self.grid))
                for col in range(len(self.grid[0]))
                if (row, col) not in excluded and self.grid[row][col].val != 15
            ],
            min(
                state.level_sys.pac_gums, (state.m_height * state.m_width) - 5
            ),
        )
        for row, col in coords:
            self.grid[row][col].contain = 1
        for row, col in (
            (0, 0),
            (0, state.m_width - 1),
            (state.m_height - 1, state.m_width - 1),
            (state.m_height - 1, 0),
        ):
            self.grid[row][col].contain = 2

    def build_maze_surface(self, state: State) -> pygame.Surface:
        width = 2 * MARGIN + state.cell_size * state.m_width
        height = 2 * MARGIN + state.cell_size * state.m_height
        surface = pygame.Surface((width, height))
        surface.fill((20, 20, 35))

        for row in range(state.m_height):
            for col in range(state.m_width):
                rect = pygame.Rect(
                    MARGIN + col * state.cell_size,
                    MARGIN + row * state.cell_size,
                    state.cell_size,
                    state.cell_size,
                )
                pygame.draw.rect(surface, (0, 75, 255), rect, 1)

                if state.debugg:
                    debug_font = pygame.font.SysFont(None, 15)
                    node = self.grid[row][col]
                    lines = [f"s:{node.s}", f"e:{node.e}"]
                    x = MARGIN + col * state.cell_size + state.cell_size // 3
                    y = MARGIN + row * state.cell_size + state.cell_size // 3

                    for i, line in enumerate(lines):
                        text = debug_font.render(line, True, (255, 255, 255))
                        surface.blit(
                            text, (x, y + i * debug_font.get_linesize())
                        )
                if self.grid[row][col].val == 15:
                    pygame.draw.rect(surface, (0, 75, 255), rect)
                else:
                    if (
                        self.grid[row][col].w is True
                        and self.grid[row][col].n is True
                    ):
                        shadow = pygame.Rect(
                            MARGIN + col * state.cell_size - 1,
                            MARGIN + row * state.cell_size - 1,
                            state.cell_size,
                            state.cell_size,
                        )
                        pygame.draw.rect(surface, (20, 20, 35), shadow, 2)
                    elif self.grid[row][col].n is True:
                        shadow = pygame.Rect(
                            MARGIN + col * state.cell_size + 1,
                            MARGIN + row * state.cell_size - 2,
                            state.cell_size - 2,
                            3,
                        )
                        pygame.draw.rect(surface, (20, 20, 35), shadow, 4)
                    elif self.grid[row][col].w is True:
                        shadow = pygame.Rect(
                            MARGIN + col * state.cell_size - 2,
                            MARGIN + row * state.cell_size + 1,
                            3,
                            state.cell_size - 2,
                        )
                        pygame.draw.rect(surface, (20, 20, 35), shadow, 4)
        pygame.draw.rect(
            surface,
            (0, 75, 255),
            pygame.Rect(
                MARGIN - 3,
                MARGIN - 3,
                state.cell_size * state.m_width + 6,
                state.cell_size * state.m_height + 6,
            ),
            3,
        )
        return surface

    def maze_fill(self, state: State):
        maze_gen = MazeGenerator(
            size=(state.m_width, state.m_height), seed=state.level_sys.seed
        )
        maze_grid = maze_gen.maze
        nodemaze = [
            [Node() for _ in range(state.m_width)]
            for _ in range(state.m_height)
        ]
        x = 0
        y = 0
        for lst in maze_grid:
            for val in lst:
                nodemaze[x][y].val = val
                nodemaze[x][y].xy = (x, y)
                nodemaze[x][y].set_dir(maze_grid[x][y])
                y += 1
            y = 0
            x += 1
        self.grid = nodemaze


class Entity:
    def __init__(self, cell_size: int) -> None:
        self.grid_position: pygame.Vector2 = pygame.Vector2(2, 2)
        self.cell_size: int = cell_size
        self.frames: list[pygame.Surface] = []
        self.active_anim: Optional[list[pygame.Surface]] = []
        self.alive: bool = True
        self.anim_name: Optional[str] = None
        self.visual_position: Optional[pygame.Vector2] = None

    @property
    def pixel_position(self) -> pygame.Vector2:
        pos = (
            self.grid_position
            if self.visual_position is None
            else self.visual_position
        )
        return pygame.Vector2(
            MARGIN + (pos.x + 0.5) * self.cell_size,
            MARGIN + (pos.y + 0.5) * self.cell_size,
        )

    @property
    def is_moving(self) -> bool:
        return (
            self.visual_position is not None
            and self.visual_position != self.grid_position
        )

    def advance(self, dt_ms: int) -> None:
        if self.visual_position is None:
            self.visual_position = self.grid_position.copy()
            return
        delta = self.grid_position - self.visual_position
        step = 7.5 * dt_ms / 1000
        if delta.length() <= step:
            self.visual_position = self.grid_position.copy()
        else:
            self.visual_position += delta.normalize() * step

    def current_frame(self, ticks: int) -> Optional[pygame.Surface]:
        if self.active_anim is not None:
            index = (ticks // ANIM_STEP_MS) % len(self.active_anim)
            return self.active_anim[index]
        return None

    def clone(self):
        other = copy.copy(self)
        other.grid_position = self.grid_position.copy()
        other.visual_position = None  # respawn snaps instead of gliding
        return other


class Ghost(Entity):
    def __init__(self, cell_size: int) -> None:
        super().__init__(cell_size)
        self.vulnerable: bool = False
        self.vul_frames: list[pygame.Surface] = []

    def set_animation(
        self, name: Optional[str], id: int, player_state: bool
    ) -> None:
        if player_state is False:
            self.active_anim = None
            return
        if name == self.anim_name and self.active_anim:
            return
        self.anim_name = name
        indices = GHOST_ANIMATIONS.get(name, IDLE)
        if self.vulnerable is False:
            self.active_anim = [self.frames[i] for i in indices]
        else:
            self.active_anim = [self.vul_frames[i] for i in indices]

    def update(self, id: int, maze: Maze, state: State) -> None:
        self.vulnerable = state.vul_ghosts
        if self.vulnerable is False:
            name = "right"
        else:
            name = "v_right"
        player_state = state.life != 0
        self.set_animation(name, id, player_state)


class Player(Entity):
    def __init__(self, cell_size: int) -> None:
        super().__init__(cell_size)
        self.name: str = ""

    def set_animation(self, name: Optional[str]) -> None:
        if name == self.anim_name and self.active_anim:
            return
        self.anim_name = name
        indices = PLAYER_ANIMATIONS.get(name, IDLE)
        self.active_anim = [self.frames[i] for i in indices]

    def update(self, maze: Maze, held: list[int], state: State) -> None:
        if state.life == 0:
            self.set_animation("dead")
            return
        if self.is_moving:
            return
        if (
            maze.grid[int(self.grid_position[1])][
                int(self.grid_position[0])
            ].contain
            == 1
        ):
            maze.grid[int(self.grid_position[1])][
                int(self.grid_position[0])
            ].contain = 0
            state.current_score += state.level_sys.points_per_pacgum
        if (
            maze.grid[int(self.grid_position[1])][
                int(self.grid_position[0])
            ].contain
            == 2
        ):
            maze.grid[int(self.grid_position[1])][
                int(self.grid_position[0])
            ].contain = 0
            state.current_score += state.level_sys.points_per_super_pacgum
            state.vul_ghosts = True
        name = KEY_TO_DIR[held[-1]] if held else None
        self.set_animation(name)
        if name is None:
            return
        target = self.grid_position + VECTORS[name]
        if maze.valid_dir(self.grid_position, VECTORS[name]):
            self.grid_position = target
