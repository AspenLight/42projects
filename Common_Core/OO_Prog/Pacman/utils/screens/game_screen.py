from ..game_objects import Player, Ghost, Maze
from ..consts import BOTTOM_BAR, MARGIN
import random
from typing import Optional, cast
from ..system_data import (
    Inputs,
    State,
    SaveSystem,
)
import pygame
from .basis_screens import Screen


class GameScreen(Screen):
    def __init__(
        self,
        player_template: Player,
        maze: Maze,
        ghosts_template: tuple[Ghost, ...],
    ) -> None:
        self.player_template = player_template
        self.ghosts_template = ghosts_template
        self.player = player_template.clone()
        self.ghosts = tuple(g.clone() for g in ghosts_template)
        self.maze = maze
        self.background = pygame.Surface((0, 0))
        self.canvas = pygame.Surface((0, 0))
        self.last_step = 0
        self.elapsed_ms = 0
        self.time_death = 0

    def basis(self, state: State) -> None:
        self.maze.maze_fill(state)
        self.background = self.maze.build_maze_surface(state)
        self.player = self.player_template.clone()
        self.ghosts = tuple(g.clone() for g in self.ghosts_template)
        self.last_step = pygame.time.get_ticks()
        self.elapsed_ms = 0
        self.maze.build_gums(state)
        if state.cheat.increased_speed is True:
            self.player.speed += 5
        # print(self.player.speed)

    def on_enter(self, state: State) -> None:
        self.basis(state)
        state.level_sys.level = 1
        state.life = 3 + state.cheat.extra_lives
        state.current_score = 0
        state.timer = state.level_sys.level_max_time
        state.ingame = True

    def new_lvl(self, state: State) -> None:
        self.basis(state)
        state.level_sys.level += 1
        state.timer = state.level_sys.level_max_time
        state.vul_ghosts = False
        state.vul_timer = 0

    def on_redo(self) -> None:
        self.player = self.player_template.clone()
        self.last_step = pygame.time.get_ticks()

    def update(
        self, inp: Inputs, state: State, save_state: SaveSystem
    ) -> Optional[str]:
        if state.level_sys.level > 10:
            return "win"
        state.ghost_coords.clear()
        for ghost in self.ghosts:
            state.ghost_coords.append(ghost.grid_position)
        if state.cheat.lvl_skip:
            state.level_sys.seed = random.randint(0, 1000)
            random.seed(state.level_sys.seed)
            self.new_lvl(state)
            state.cheat.lvl_skip = False
        gums_left = any(
            node.contain != 0 for row in self.maze.grid for node in row
        )
        # if found is false, go to next lvl
        if gums_left is False:
            state.level_sys.seed = random.randint(0, 1000)
            random.seed(state.level_sys.seed)
            self.new_lvl(state)
        self.player.update(self.maze, inp.held, state)
        if state.life != 0:
            self.time_death = self.elapsed_ms
        self.player.advance(state.dt)
        self.player.update(self.maze, inp.held, state)
        self.elapsed_ms += state.dt
        for id, ghost in enumerate(self.ghosts):
            ghost.advance(state.dt)
            ghost.update(id, self.maze, state, self.player.grid_position)
            if not ghost.alive and ghost.grid_position == ghost.start_pos:
                ghost.alive = True
                ghost.vulnerable = False
                ghost.immune_gen = state.vul_gen
            if ghost.grid_position == self.player.grid_position:
                if not ghost.vulnerable:
                    if ghost.alive and state.cheat.invicibility is False:
                        state.end_life = True
                else:
                    state.current_score += state.level_sys.points_per_ghost
                    ghost.alive = False
                    ghost.vulnerable = False
        if state.timer <= 0.0:
            state.life = 0
        if state.vul_ghosts is True:
            for ghost in self.ghosts:
                ghost.lastmove = ""
            state.vul_timer += state.dt / 1000
            if state.vul_timer >= 10.0:
                state.vul_ghosts = False
                state.vul_timer = 0
        state.timer -= state.dt / 1000
        if state.end_life is True and state.life != 0:
            self.on_redo()
            if state.cheat.increased_speed is True:
                self.player.speed += 5
            state.life -= 1
            state.end_life = False
        elif self.elapsed_ms - self.time_death > 1000:
            state.ingame = False
            return "gameover"
        return None

    def draw(
        self, window: pygame.Surface, state: State, save_state: SaveSystem
    ) -> None:
        game_w = 2 * MARGIN + state.cell_size * state.m_width
        game_h = 2 * MARGIN + state.cell_size * state.m_height
        if self.canvas.get_size() != (game_w, game_h):
            self.canvas = pygame.Surface((game_w, game_h))
        self.draw_game(self.canvas, state)
        window.fill("black")
        block_h = game_h + BOTTOM_BAR
        pos_x = max(0, (window.get_width() - game_w) // 2)
        pos_y = max(0, (window.get_height() - block_h) // 2)
        window.blit(self.canvas, (pos_x, pos_y))
        self.draw_info(window, state, pos_y + game_h + BOTTOM_BAR // 2)

    def draw_info(
        self, window: pygame.Surface, state: State, center_y: int
    ) -> None:
        font = pygame.font.SysFont(None, 30)
        big_font = pygame.font.SysFont(None, 45)
        white = (255, 255, 255)
        texts = (
            font.render(f"Remaining life: {state.life}", True, white),
            font.render(f"score: {state.current_score}", True, white),
            font.render(f"time left: {round(state.timer)}", True, white),
            big_font.render(f"lvl:{state.level_sys.level}", True, white),
        )
        slot_w = window.get_width() // len(texts)
        for i, text in enumerate(texts):
            center_x = slot_w * i + slot_w // 2
            window.blit(text, text.get_rect(center=(center_x, center_y)))

    def draw_game(self, window: pygame.Surface, state: State) -> None:
        window.fill("black")
        window.blit(self.background, (0, 0))
        now = pygame.time.get_ticks()
        for row in range(state.m_height):
            for col in range(state.m_width):
                if self.maze.grid[row][col].contain == 1:
                    pygame.draw.circle(
                        window,
                        "orange",
                        (
                            (MARGIN + col * state.cell_size)
                            + state.cell_size / 2,
                            (MARGIN + row * state.cell_size)
                            + state.cell_size / 2,
                        ),
                        state.cell_size / 8,
                    )
                elif self.maze.grid[row][col].contain == 2:
                    pygame.draw.circle(
                        window,
                        "orange",
                        (
                            (MARGIN + col * state.cell_size)
                            + state.cell_size / 2,
                            (MARGIN + row * state.cell_size)
                            + state.cell_size / 2,
                        ),
                        state.cell_size / 5,
                    )
        player_sprite = cast(pygame.Surface, self.player.current_frame(now))
        window.blit(
            player_sprite,
            player_sprite.get_rect(center=self.player.pixel_position),
        )
        for ghost in self.ghosts:
            ghost_sprite = ghost.current_frame(now)
            if ghost_sprite is not None:
                window.blit(
                    ghost_sprite,
                    ghost_sprite.get_rect(center=ghost.pixel_position),
                )
