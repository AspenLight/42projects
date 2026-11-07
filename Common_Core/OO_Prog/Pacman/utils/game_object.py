from .consts import (
    MARGIN,
    ANIM_STEP_MS,
    GHOST_ANIMATIONS,
    PLAYER_ANIMATIONS,
    IDLE,
    KEY_TO_DIR,
    VECTORS,
    PLAYER_SPEED,
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
    def __init__(self, cell_size: int, speed: float) -> None:
        self.grid_position: pygame.Vector2 = pygame.Vector2(2, 2)
        self.cell_size: int = cell_size
        self.frames: list[pygame.Surface] = []
        self.active_anim: Optional[list[pygame.Surface]] = []
        self.alive: bool = True
        self.anim_name: Optional[str] = None
        self.visual_position: Optional[pygame.Vector2] = None
        self.speed: float = speed

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
        step = self.speed * dt_ms / 1000
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


class Pathfinding:
    grid_position: pygame.Vector2

    def secondary_target(
        self,
        player_pos: pygame.Vector2,
        priority: str,
    ) -> str:
        direction = ""
        if priority == "EW":
            dir = player_pos[0] - self.grid_position[0]
            if dir > 0:
                direction = "E"
            elif dir < 0:
                direction = "W"
        elif priority == "NS":
            dir = player_pos[1] - self.grid_position[1]
            if dir > 0:
                direction = "S"
            elif dir < 0:
                direction = "N"
        return direction

    # intersect_move takes a list of available directions, the player position, and the ghost position
    # it returns a tuple coordinate of where the ghost should move
    def intersect_move(
        self,
        dirs: list[str],
        player_pos: pygame.Vector2,
    ) -> pygame.Vector2 | None:
        dir_NS = player_pos[1] - self.grid_position[1]
        dir_EW = player_pos[0] - self.grid_position[0]
        if dir_NS == 0 and dir_EW == 0:
            return
        if len(dirs) != 3:
            return
        priority = "NS"
        direction = "N"

        if abs(dir_NS) < abs(dir_EW):
            priority = "EW"
            direction = "E"

        if priority == "NS":
            if dir_NS > 0:
                direction = "S"
            if dir_NS < 0:
                direction = "N"
            if dir_NS == 0:
                priority = "EW"
        if priority == "EW":
            if dir_EW > 0:
                direction = "E"
            if dir_EW < 0:
                direction = "W"
            if dir_EW == 0:
                priority = "NS"
        if priority == "NS" and direction == ("E" or "W"):
            if dir_NS > 0:
                direction = "S"
            if dir_NS < 0:
                direction = "N"

        if direction == "N" and direction in dirs:
            return pygame.Vector2(
                self.grid_position[0], self.grid_position[1] - 1
            )
        if direction == "S" and direction in dirs:
            return pygame.Vector2(
                self.grid_position[0], self.grid_position[1] + 1
            )
        if direction == "E" and direction in dirs:
            return pygame.Vector2(
                self.grid_position[0] + 1, self.grid_position[1]
            )
        if direction == "W" and direction in dirs:
            return pygame.Vector2(
                self.grid_position[0] - 1, self.grid_position[1]
            )
        if priority == "NS":
            priority = "EW"
        elif priority == "EW":
            priority = "NS"
        direction = self.secondary_target(player_pos, priority)
        if direction == "N" and direction in dirs:
            return pygame.Vector2(
                self.grid_position[0], self.grid_position[1] - 1
            )
        if direction == "S" and direction in dirs:
            return pygame.Vector2(
                self.grid_position[0], self.grid_position[1] + 1
            )
        if direction == "E" and direction in dirs:
            return pygame.Vector2(
                self.grid_position[0] + 1, self.grid_position[1]
            )
        if direction == "W" and direction in dirs:
            return pygame.Vector2(
                self.grid_position[0] - 1, self.grid_position[1]
            )

    # hallway_move takes a list of available directions, the player position, and the ghost position
    # it returns a tuple coordinate of where the ghost should move
    def hallway_move(
        self,
        dirs: list[str],
        player_pos: pygame.Vector2,
    ) -> pygame.Vector2 | None:
        dir_NS = player_pos[1] - self.grid_position[1]
        dir_EW = player_pos[0] - self.grid_position[0]
        if dir_EW == 0 and dir_NS == 0:
            return

        if "N" in dirs and "S" in dirs:
            if dir_NS > 0:
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] + 1
                )
            elif dir_NS < 0:
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] - 1
                )
            else:
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] + 1
                )
        elif "E" in dirs and "W" in dirs:
            if dir_EW > 0:
                return pygame.Vector2(
                    self.grid_position[0] + 1, self.grid_position[1]
                )
            elif dir_EW < 0:
                return pygame.Vector2(
                    self.grid_position[0] - 1, self.grid_position[1]
                )
            else:
                return pygame.Vector2(
                    self.grid_position[0] + 1, self.grid_position[1]
                )
        else:
            if (abs(dir_NS) < abs(dir_EW)) and dir_NS != 0:
                if dir_NS > 0 and "N" in dirs:
                    return pygame.Vector2(
                        self.grid_position[0], self.grid_position[1] - 1
                    )
                elif dir_NS < 0 and "S" in dirs:
                    return pygame.Vector2(
                        self.grid_position[0], self.grid_position[1] + 1
                    )
            if abs(dir_NS) < abs(dir_EW) and dir_EW != 0:
                if dir_EW > 0 and "E" in dirs:
                    return pygame.Vector2(
                        self.grid_position[0] + 1, self.grid_position[1]
                    )
                if dir_EW < 0 and "W" in dirs:
                    return pygame.Vector2(
                        self.grid_position[0] - 1, self.grid_position[1]
                    )
            if dir_NS == 0 and ("E" or "W") in dirs:
                if dir_EW > 0 and "E" in dirs:
                    return pygame.Vector2(
                        self.grid_position[0] + 1, self.grid_position[1]
                    )
                elif dir_EW < 0 and "W" in dirs:
                    return pygame.Vector2(
                        self.grid_position[0] - 1, self.grid_position[1]
                    )
                else:
                    if "E" in dirs:
                        return pygame.Vector2(
                            self.grid_position[0] + 1, self.grid_position[1]
                        )
                    if "W" in dirs:
                        return pygame.Vector2(
                            self.grid_position[0] - 1, self.grid_position[1]
                        )
            if dir_EW == 0 and ("N" or "S") in dirs:
                if dir_NS > 0 and "N" in dirs:
                    return pygame.Vector2(
                        self.grid_position[0], self.grid_position[1] - 1
                    )
                elif dir_NS < 0 and "S" in dirs:
                    return pygame.Vector2(
                        self.grid_position[0], self.grid_position[1] + 1
                    )
                else:
                    if "N" in dirs:
                        return pygame.Vector2(
                            self.grid_position[0], self.grid_position[1] - 1
                        )
                    if "S" in dirs:
                        return pygame.Vector2(
                            self.grid_position[0], self.grid_position[1] + 1
                        )

    # free_move takes the player position and the ghost position
    # and returns the coordinate of where the ghost should go next
    def free_move(self, player_pos: pygame.Vector2) -> pygame.Vector2 | None:
        dir_NS = player_pos[1] - self.grid_position[1]
        dir_EW = player_pos[0] - self.grid_position[0]
        if dir_NS == 0 and dir_EW == 0:
            return

        if abs(dir_NS) < abs(dir_EW) and dir_NS != 0:
            if dir_NS > 0:
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] - 1
                )
            if dir_NS < 0:
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] + 1
                )
        if abs(dir_NS) > abs(dir_EW) and dir_EW != 0:
            if dir_EW > 0:
                return pygame.Vector2(
                    self.grid_position[0] + 1, self.grid_position[1]
                )
            if dir_EW < 0:
                return pygame.Vector2(
                    self.grid_position[0] - 1, self.grid_position[1]
                )
        if dir_NS > 0:
            return pygame.Vector2(
                self.grid_position[0], self.grid_position[1] + 1
            )
        if dir_NS < 0:
            return pygame.Vector2(
                self.grid_position[0], self.grid_position[1] - 1
            )

    # pathfind takes the node the ghost is on, the player position, and the ghost position
    # and returns the new position the ghost should be at.
    def pathfind(
        self,
        node: Node,
        player_pos: pygame.Vector2,
    ) -> pygame.Vector2 | None:
        dirs: list[str] = []
        newpos: pygame.Vector2 | None

        if node.n == True:
            dirs.append("N")
        if node.e == True:
            dirs.append("E")
        if node.s == True:
            dirs.append("S")
        if node.w == True:
            dirs.append("W")

        if len(dirs) == 2:
            print(f"hallway, {dirs}")
            newpos = self.hallway_move(dirs, player_pos)
            dirs.clear()
            return newpos
        if len(dirs) == 3:
            print(f"intersect, {dirs}")
            newpos = self.intersect_move(dirs, player_pos)
            dirs.clear()
            return newpos
        if len(dirs) == 4:
            print(f"free, {dirs}")
            newpos = self.free_move(player_pos)
            dirs.clear()
            return newpos
        else:
            dirs.clear()
            return


class Ghost(Entity, Pathfinding):
    def __init__(self, cell_size: int) -> None:
        super().__init__(cell_size, PLAYER_SPEED - PLAYER_SPEED / 8)
        self.vulnerable: bool = False
        self.vul_frames: list[pygame.Surface] = []
        self.dead_frames: list[pygame.Surface] = []
        self.dir: pygame.Vector2 = pygame.Vector2(0, 0)
        self.n_dir: str = ""
        self.start_pos: pygame.Vector2 = pygame.Vector2(0, 0)
        self.invul: tuple[bool, float] = (False, 0)

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
        if not self.alive:
            self.active_anim = [self.dead_frames[i] for i in indices]
        elif self.vulnerable:
            self.active_anim = [self.vul_frames[i] for i in indices]
        else:
            self.active_anim = [self.frames[i] for i in indices]

    def update(
        self, id: int, maze: Maze, state: State, player_pos: pygame.Vector2
    ) -> None:
        if state.vul_timer <= 1:
            self.invul = (False, 0.0)
        if self.invul[1] <= 10.0 and not self.invul[0]:
            self.vulnerable = state.vul_ghosts
        elif self.invul[0]:
            self.invul = (self.invul[0], self.invul[1] + state.dt / 1000)
            self.vulnerable = False
            if self.invul[1] > 10.0:
                self.invul = (False, 0)
        if not self.alive:
            self.speed = PLAYER_SPEED * 2
        elif self.vulnerable:
            self.speed = PLAYER_SPEED - PLAYER_SPEED / 2
        elif id == 1:
            self.speed = PLAYER_SPEED - PLAYER_SPEED / 10
        else:
            self.speed = PLAYER_SPEED - PLAYER_SPEED / 8
        player_state: bool = state.life != 0
        last_pos: pygame.Vector2 = self.grid_position
        if player_state and not self.is_moving:
            node = maze.grid[int(self.grid_position[1])][
                int(self.grid_position[0])
            ]
            newpos: pygame.Vector2 | None = (
                self.pathfind(node, player_pos)
                if self.alive
                else self.pathfind(node, self.start_pos)
            )
            if newpos is not None:
                self.grid_position = newpos
        self.dir = last_pos - self.grid_position
        match (round(self.dir.x), round(self.dir.y)):
            case (-1, 0):
                self.n_dir = "right"
            case (1, 0):
                self.n_dir = "left"
            case (0, 1):
                self.n_dir = "up"
            case (0, -1):
                self.n_dir = "down"
            case _:
                self.n_dir = self.n_dir

        name = (
            "d_" if not self.alive else "v_" if self.vulnerable else ""
        ) + self.n_dir
        self.set_animation(name, id, player_state)


class Player(Entity):
    def __init__(self, cell_size: int) -> None:
        super().__init__(cell_size, PLAYER_SPEED)
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
            state.vul_timer = 0
        name = KEY_TO_DIR[held[-1]] if held else None
        self.set_animation(name)
        if name is None:
            return
        target = self.grid_position + VECTORS[name]
        if maze.valid_dir(self.grid_position, VECTORS[name]):
            self.grid_position = target
