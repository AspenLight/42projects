from mazegenerator.mazegenerator import MazeGenerator
from ..consts import MARGIN
from ..system_data import State
import pygame
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

    # def display_data(self) -> None:
    #     print(f"xy: {self.xy}")
    #     print(f"N: {self.n}")
    #     print(f"E: {self.e}")
    #     print(f"S: {self.s}")
    #     print(f"W: {self.w}")
    #     print(f"Dist: {self.dist}")


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

    def maze_fill(self, state: State) -> None:
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
