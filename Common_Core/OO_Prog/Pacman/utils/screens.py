from typing import Optional, cast
import random
import pygame
from .system_data import (
    Inputs,
    State,
    SaveSystem,
)
from .game_object import Player, Ghost, Maze
from .consts import YELLOW, MAX_NAME_LEN, BOTTOM_BAR, MARGIN


# --------------------------------------------------------------------------
# Screens
# --------------------------------------------------------------------------
class Button:
    def __init__(
        self,
        text: str,
        center: tuple[int, int],
        size: tuple[int, int],
        font: pygame.font.Font,
        hover: bool,
    ) -> None:
        self.text: str = text
        self.font: pygame.font.Font = font
        self.rect: pygame.Rect = pygame.Rect((0, 0), size)
        self.rect.center = center

    def draw(self, window: pygame.Surface, offset: int = 0) -> None:
        rect = self.rect.move(
            0, offset
        )  # a shifted copy; self.rect is unchanged
        pygame.draw.rect(window, "black", rect)
        label = self.font.render(self.text, True, "white")
        window.blit(label, label.get_rect(center=rect.center))


class Screen:
    def on_enter(self, state: State) -> None:
        pass

    def update(
        self, inp: Inputs, state: State, save_state: SaveSystem
    ) -> Optional[str]:
        pass

    def draw(
        self, window: pygame.Surface, state: State, save_state: SaveSystem
    ) -> None:
        pass


class MenuScreen(Screen):
    def __init__(
        self,
        title: str,
        items: list[tuple[str, str]],  # (label, target mode)
        title_font: pygame.font.Font,
        button_font: pygame.font.Font,
        win_w: int,
        show_name: bool = False,
    ) -> None:
        self.title = title
        self.title_font = title_font
        self.button_font = button_font
        self.score_font = pygame.font.SysFont(None, 36)
        self.win_w = win_w
        self.show_name = show_name
        self.targets = [target for _, target in items]
        self.selected = 0
        self.buttons = [
            Button(
                label,
                (win_w // 2, 220 + i * 100),
                (700, 70),
                button_font,
                i == 0,
            )
            for i, (label, _) in enumerate(items)
        ]

    def on_enter(self, state: State) -> None:
        self.selected = 0

    def update(
        self, inp: Inputs, state: State, save_state: SaveSystem
    ) -> Optional[str]:
        for key in inp.pressed:
            if key == pygame.K_SPACE:
                return self.targets[self.selected]
        return None

    def draw(
        self, window: pygame.Surface, state: State, save_state: SaveSystem
    ) -> None:
        offset = 0
        window.fill((0, 0, 0))
        title = self.title_font.render(self.title, True, YELLOW)
        window.blit(title, title.get_rect(center=(self.win_w // 2, 100)))
        scoring = self.score_font.render("highscores:", True, "white")
        window.blit(scoring, scoring.get_rect(center=(self.win_w // 2, 300)))

        for button in self.buttons:
            button.draw(window)
        i = 1
        for name, score in sorted(
            save_state.scores.items(), key=lambda item: item[1], reverse=True
        ):
            if i == 11:
                break
            name = self.score_font.render(
                f"{i}. {name} - {score}", True, "white"
            )
            window.blit(
                name, name.get_rect(center=(self.win_w // 2, 350 + offset))
            )

            offset += 35
            i += 1


class TypingScreen(Screen):
    def __init__(self, font: pygame.font.Font, win_w: int, score: int) -> None:
        self.font = font
        self.win_w = win_w
        self.backspace_ms = 0

    def on_enter(self, state: State) -> None:
        self.backspace_ms = 0
        pygame.key.start_text_input()

    def update(
        self, inp: Inputs, state: State, save_state: SaveSystem
    ) -> Optional[str]:
        for ch in inp.typed:
            if len(state.name) < MAX_NAME_LEN and (
                ch.isalpha() or ch.isnumeric() or ch == " "
            ):
                state.name += ch
        for key in inp.pressed:
            if key == pygame.K_BACKSPACE:
                state.name = state.name[:-1]
            elif key == pygame.K_RETURN:
                pygame.key.stop_text_input()
                if save_state.scores.get(state.name):
                    if state.current_score > save_state.scores[state.name]:
                        save_state.scores[state.name] = state.current_score
                else:
                    save_state.scores[state.name] = state.current_score
                return "main menu"
        if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
            self.backspace_ms += state.dt
            if self.backspace_ms >= 100:
                state.name = state.name[:-1]
                self.backspace_ms -= 50
        else:
            self.backspace_ms = 0
        return None

    def draw(
        self, window: pygame.Surface, state: State, save_state: SaveSystem
    ) -> None:
        window.fill((0, 0, 0))
        text = self.font.render(f"{state.name}_", True, (255, 255, 255))
        validate = self.font.render(
            "press enter to validate", True, (255, 255, 255)
        )
        window.blit(text, text.get_rect(center=(self.win_w // 2, 300)))
        window.blit(validate, validate.get_rect(center=(self.win_w // 2, 400)))


class GameScreen(Screen):
    def __init__(
        self,
        player_template: Player,
        maze: Maze,
        ghosts_template: tuple[Ghost, ...],
        background: pygame.Surface,
    ) -> None:
        self.player_template = player_template
        self.ghosts_template = ghosts_template
        self.player = player_template.clone()
        self.ghosts = tuple(g.clone() for g in ghosts_template)
        self.maze = maze
        self.background = background
        self.last_step = 0
        self.elapsed_ms = 0
        self.time_death = 0

    def on_enter(self, state: State) -> None:
        self.player = self.player_template.clone()
        self.ghosts = tuple(g.clone() for g in self.ghosts_template)
        self.last_step = pygame.time.get_ticks()
        self.elapsed_ms = 0
        self.maze.build_gums(state)
        state.life = 3
        state.current_score = 0
        state.timer = state.level_sys.level_max_time

    def on_redo(self) -> None:
        self.player = self.player_template.clone()
        self.last_step = pygame.time.get_ticks()

    def update(
        self, inp: Inputs, state: State, save_state: SaveSystem
    ) -> Optional[str]:
        gums_left = any(
            node.contain != 0 for row in self.maze.grid for node in row
        )
        # if found is false, go to next lvl
        if gums_left is False:
            state.level_sys.seed += 1
            random.seed(state.level_sys.seed)
        self.player.update(self.maze, inp.held, state)
        if state.life != 0:
            self.time_death = self.elapsed_ms
        self.player.advance(state.dt)
        self.player.update(self.maze, inp.held, state)
        self.elapsed_ms += state.dt
        for id, ghost in enumerate(self.ghosts):
            ghost.advance(state.dt)
            ghost.update(id, self.maze, state)
            if (
                ghost.vulnerable is False
                and ghost.grid_position == self.player.grid_position
            ):
                state.end_life = True
        if state.timer <= 0.0:
            state.life = 0
        if state.vul_ghosts is True:
            state.vul_timer += state.dt / 1000
            if state.vul_timer >= 10.0:
                state.vul_ghosts = False
                state.vul_timer = 0
        state.timer -= state.dt / 1000
        print(
            f"\033[K{gums_left}",
            end="\n",
            flush=True,
        )
        print(
            f"\033[K{self.elapsed_ms} - {self.time_death} = {self.elapsed_ms - self.time_death}",
            end="\n",
            flush=True,
        )
        print(f"\033[Ktime left = {round(state.timer)}", end="\n", flush=True)
        print(f"\033[Kvul_timer = {round(state.vul_timer)}", end="", flush=True)
        print("\033[3A\r", end="", flush=True)
        if state.end_life is True and state.life != 0:
            self.on_redo()
            state.life -= 1
            state.end_life = False
        elif self.elapsed_ms - self.time_death > 1000:
            return "typing"
        return None

    def draw(
        self, window: pygame.Surface, state: State, save_state: SaveSystem
    ) -> None:
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
        score = pygame.font.SysFont(None, 25).render(
            f"score: {state.current_score}",
            True,
            (255, 255, 255),
        )
        timer = pygame.font.SysFont(None, 25).render(
            f"time left: {round(state.timer)}",
            True,
            (255, 255, 255),
        )
        life = pygame.font.SysFont(None, 25).render(
            f"Remaining life: {state.life}",
            True,
            (255, 255, 255),
        )
        for ghost in self.ghosts:
            ghost_sprite = ghost.current_frame(now)
            if ghost_sprite is not None:
                window.blit(
                    ghost_sprite,
                    ghost_sprite.get_rect(center=ghost.pixel_position),
                )
        window.blit(
            score,
            score.get_rect(
                center=(
                    window.get_width() // 10 + 150,
                    window.get_height() - BOTTOM_BAR // 2,
                )
            ),
        )
        window.blit(
            life,
            life.get_rect(
                center=(
                    window.get_width() // 10,
                    window.get_height() - BOTTOM_BAR // 2,
                )
            ),
        )
        window.blit(
            timer,
            timer.get_rect(
                center=(
                    window.get_width() // 10 + 270,
                    window.get_height() - BOTTOM_BAR // 2,
                )
            ),
        )
