from typing import Self
from ..consts import (
    MARGIN,
    ANIM_STEP_MS,
)
from ..system_data import State
from typing import Optional
import pygame
import copy
import random
from .maze import Node


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

    def clone(self) -> Self:
        other = copy.copy(self)
        other.grid_position = self.grid_position.copy()
        other.visual_position = None  # respawn snaps instead of gliding
        return other


class Pathfinding:
    def __init__(self) -> None:
        self.grid_position: pygame.Vector2
        self.lastmove: str
        self.alive: bool
        self.vulnerable: bool
        self.n_dir: str = ""

    def target_tile(
        self, dirs: list[str], target_pos: pygame.Vector2
    ) -> pygame.Vector2 | None:
        dir_NS = target_pos[1] - self.grid_position[1]
        dir_EW = target_pos[0] - self.grid_position[0]
        if dir_NS == 0 and dir_EW == 0:
            return None

        if (abs(dir_NS) > abs(dir_EW)) and dir_NS != 0:
            if dir_NS < 0 and "N" in dirs:
                self.lastmove = "N"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] - 1
                )
            if dir_NS > 0 and "S" in dirs:
                self.lastmove = "S"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] + 1
                )
        elif (abs(dir_EW) > abs(dir_NS)) and dir_EW != 0:
            if dir_EW > 0 and "E" in dirs:
                self.lastmove = "E"
                return pygame.Vector2(
                    self.grid_position[0] + 1, self.grid_position[1]
                )
            if dir_EW < 0 and "W" in dirs:
                self.lastmove = "W"
                return pygame.Vector2(
                    self.grid_position[0] - 1, self.grid_position[1]
                )

        if dir_NS == 0:
            if dir_EW > 0 and "E" in dirs:
                self.lastmove = "E"
                return pygame.Vector2(
                    self.grid_position[0] + 1, self.grid_position[1]
                )
            if dir_EW < 0 and "W" in dirs:
                self.lastmove = "W"
                return pygame.Vector2(
                    self.grid_position[0] - 1, self.grid_position[1]
                )
        if dir_EW == 0:
            if dir_NS < 0 and "N" in dirs:
                self.lastmove = "N"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] - 1
                )
            if dir_NS > 0 and "S" in dirs:
                self.lastmove = "S"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] + 1
                )

        if abs(dir_NS) > abs(dir_EW):
            if dir_EW > 0 and "E" in dirs:
                self.lastmove = "E"
                return pygame.Vector2(
                    self.grid_position[0] + 1, self.grid_position[1]
                )
            if dir_EW < 0 and "W" in dirs:
                self.lastmove = "W"
                return pygame.Vector2(
                    self.grid_position[0] - 1, self.grid_position[1]
                )
        if abs(dir_EW) > abs(dir_NS):
            if dir_NS < 0 and "N" in dirs:
                self.lastmove = "N"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] - 1
                )
            if dir_NS > 0 and "S" in dirs:
                self.lastmove = "S"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] + 1
                )

        if "N" in dirs:
            self.lastmove = "N"
            return pygame.Vector2(
                self.grid_position[0], self.grid_position[1] - 1
            )
        if "E" in dirs:
            self.lastmove = "E"
            return pygame.Vector2(
                self.grid_position[0] + 1, self.grid_position[1]
            )
        if "S" in dirs:
            self.lastmove = "S"
            return pygame.Vector2(
                self.grid_position[0], self.grid_position[1] + 1
            )
        if "W" in dirs:
            self.lastmove = "W"
            return pygame.Vector2(
                self.grid_position[0] - 1, self.grid_position[1]
            )
        return pygame.Vector2(self.grid_position[0], self.grid_position[1])

    def escape_tile(
        self, dirs: list[str], target_pos: pygame.Vector2
    ) -> pygame.Vector2 | None:
        dir_NS = target_pos[1] - self.grid_position[1]
        dir_EW = target_pos[0] - self.grid_position[0]
        if dir_NS == 0 and dir_EW == 0:
            return None

        if (abs(dir_NS) < abs(dir_EW)) and dir_NS != 0:
            if dir_NS > 0 and "N" in dirs:
                self.lastmove = "N"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] - 1
                )
            if dir_NS < 0 and "S" in dirs:
                self.lastmove = "S"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] + 1
                )
        elif (abs(dir_EW) < abs(dir_NS)) and dir_EW != 0:
            if dir_EW < 0 and "E" in dirs:
                self.lastmove = "E"
                return pygame.Vector2(
                    self.grid_position[0] + 1, self.grid_position[1]
                )
            if dir_EW > 0 and "W" in dirs:
                self.lastmove = "W"
                return pygame.Vector2(
                    self.grid_position[0] - 1, self.grid_position[1]
                )

        if dir_EW == 0:
            if "E" in dirs:
                self.lastmove = "E"
                return pygame.Vector2(
                    self.grid_position[0] + 1, self.grid_position[1]
                )
            if "W" in dirs:
                self.lastmove = "W"
                return pygame.Vector2(
                    self.grid_position[0] - 1, self.grid_position[1]
                )
        if dir_NS == 0:
            if "N" in dirs:
                self.lastmove = "N"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] - 1
                )
            if "S" in dirs:
                self.lastmove = "S"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] + 1
                )

        if abs(dir_NS) < abs(dir_EW):
            if dir_EW < 0 and "E" in dirs:
                self.lastmove = "E"
                return pygame.Vector2(
                    self.grid_position[0] + 1, self.grid_position[1]
                )
            if dir_EW > 0 and "W" in dirs:
                self.lastmove = "W"
                return pygame.Vector2(
                    self.grid_position[0] - 1, self.grid_position[1]
                )
        if abs(dir_EW) < abs(dir_NS):
            if dir_NS > 0 and "N" in dirs:
                self.lastmove = "N"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] - 1
                )
            if dir_NS < 0 and "S" in dirs:
                self.lastmove = "S"
                return pygame.Vector2(
                    self.grid_position[0], self.grid_position[1] + 1
                )

        if "N" in dirs:
            self.lastmove = "N"
            return pygame.Vector2(
                self.grid_position[0], self.grid_position[1] - 1
            )
        if "E" in dirs:
            self.lastmove = "E"
            return pygame.Vector2(
                self.grid_position[0] + 1, self.grid_position[1]
            )
        if "S" in dirs:
            self.lastmove = "S"
            return pygame.Vector2(
                self.grid_position[0], self.grid_position[1] + 1
            )
        if "W" in dirs:
            self.lastmove = "W"
            return pygame.Vector2(
                self.grid_position[0] - 1, self.grid_position[1]
            )
        return pygame.Vector2(self.grid_position[0], self.grid_position[1])

    def pathfind(
        self, node: Node, target_pos: pygame.Vector2, state: State
    ) -> pygame.Vector2 | None:
        dirs: list[str] = []
        newpos: pygame.Vector2 | None = None
        rand: int

        if node.n is True:
            dirs.append("N")
        if node.e is True:
            dirs.append("E")
        if node.s is True:
            dirs.append("S")
        if node.w is True:
            dirs.append("W")

        if self.alive is True:
            for ghost_coord in state.ghost_coords:
                if (
                    pygame.Vector2(
                        self.grid_position[0], self.grid_position[1] - 1
                    )
                    == ghost_coord
                ) and "N" in dirs:
                    dirs.remove("N")
                if (
                    pygame.Vector2(
                        self.grid_position[0], self.grid_position[1] + 1
                    )
                    == ghost_coord
                ) and "S" in dirs:
                    dirs.remove("S")
                if (
                    pygame.Vector2(
                        self.grid_position[0] + 1, self.grid_position[1]
                    )
                    == ghost_coord
                ) and "E" in dirs:
                    dirs.remove("E")
                if (
                    pygame.Vector2(
                        self.grid_position[0] - 1, self.grid_position[1]
                    )
                    == ghost_coord
                ) and "W" in dirs:
                    dirs.remove("W")

        if len(dirs) == 0:
            return None
        if len(dirs) == 1:
            newpos = self.target_tile(dirs, target_pos)
        elif (
            len(dirs) > 1 and self.vulnerable is False
        ) or self.alive is False:
            if self.n_dir == "up" and "S" in dirs:
                dirs.remove("S")
            if self.n_dir == "right" and "W" in dirs:
                dirs.remove("W")
            if self.n_dir == "down" and "N" in dirs:
                dirs.remove("N")
            if self.n_dir == "left" and "E" in dirs:
                dirs.remove("E")
            newpos = self.target_tile(dirs, target_pos)
            rand = random.randint(0, 12)
            if rand == 12 and len(dirs) > 1:
                if self.lastmove == "N" and "N" in dirs:
                    dirs.remove("N")
                if self.lastmove == "W" and "W" in dirs:
                    dirs.remove("W")
                if self.lastmove == "S" and "S" in dirs:
                    dirs.remove("S")
                if self.lastmove == "E" and "E" in dirs:
                    dirs.remove("E")
                newpos = self.target_tile(dirs, target_pos)
        elif len(dirs) > 1 and self.vulnerable is True:
            if self.n_dir == "up" and "S" in dirs:
                dirs.remove("S")
            if self.n_dir == "right" and "W" in dirs:
                dirs.remove("W")
            if self.n_dir == "down" and "N" in dirs:
                dirs.remove("N")
            if self.n_dir == "left" and "E" in dirs:
                dirs.remove("E")
            newpos = self.escape_tile(dirs, target_pos)
            rand = random.randint(0, 12)
            if rand == 12 and len(dirs) > 1:
                if self.lastmove == "N" and "N" in dirs:
                    dirs.remove("N")
                if self.lastmove == "W" and "W" in dirs:
                    dirs.remove("W")
                if self.lastmove == "S" and "S" in dirs:
                    dirs.remove("S")
                if self.lastmove == "E" and "E" in dirs:
                    dirs.remove("E")
                newpos = self.escape_tile(dirs, target_pos)
        dirs.clear()
        return newpos
