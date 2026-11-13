from ..consts import (
    GHOST_ANIMATIONS,
    PLAYER_ANIMATIONS,
    IDLE,
    KEY_TO_DIR,
    VECTORS,
    PLAYER_SPEED,
)
from ..system_data import State
from typing import Optional
import pygame
from .mother_classes import Entity, Pathfinding
from .maze import Maze


class Ghost(Entity, Pathfinding):
    def __init__(self, cell_size: int) -> None:
        Entity.__init__(self, cell_size, PLAYER_SPEED - PLAYER_SPEED / 8)
        Pathfinding.__init__(self)
        self.vulnerable: bool = False
        self.vul_frames: list[pygame.Surface] = []
        self.dead_frames: list[pygame.Surface] = []
        self.dir: pygame.Vector2 = pygame.Vector2(0, 0)
        self.start_pos: pygame.Vector2 = pygame.Vector2(0, 0)
        self.immune_gen: int = -1

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
        if state.cheat.ghost_freeze:
            return
        if state.cheat.ghost_freeze:
            return
        self.vulnerable = (
            state.vul_ghosts
            and self.alive
            and self.immune_gen != state.vul_gen
        )
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
                self.pathfind(node, player_pos, state)
                if self.alive
                else self.pathfind(node, self.start_pos, state)
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
            state.vul_gen += 1
        name = KEY_TO_DIR[held[-1]] if held else None
        self.set_animation(name)
        if name is None:
            return
        target = self.grid_position + VECTORS[name]
        if maze.valid_dir(self.grid_position, VECTORS[name]):
            self.grid_position = target
