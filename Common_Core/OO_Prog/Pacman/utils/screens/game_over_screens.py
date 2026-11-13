from ..consts import MAX_NAME_LEN
from typing import Optional
from ..system_data import (
    Inputs,
    State,
    SaveSystem,
)
import pygame
from .basis_screens import Screen


class GameOverScreen(Screen):
    def __init__(self, font: pygame.font.Font, win_w: int, score: int) -> None:
        self.font = font
        self.win_w = win_w
        self.backspace_ms = 0

    def on_enter(self, state: State) -> None:
        self.backspace_ms = 0

    def update(
        self, inp: Inputs, state: State, save_state: SaveSystem
    ) -> Optional[str]:
        pygame.key.start_text_input()
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
                state.name = ""
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
        score = self.font.render(
            f"score : {state.current_score}", True, (255, 255, 255)
        )
        text = self.font.render(f"{state.name}_", True, (255, 255, 255))
        validate = self.font.render(
            "press enter to validate", True, (255, 255, 255)
        )
        window.blit(score, score.get_rect(center=(self.win_w // 2, 225)))
        window.blit(text, text.get_rect(center=(self.win_w // 2, 300)))
        window.blit(validate, validate.get_rect(center=(self.win_w // 2, 400)))


class VictoryScreen(GameOverScreen):
    def draw(
        self, window: pygame.Surface, state: State, save_state: SaveSystem
    ) -> None:
        # You have won the game
        window.fill((0, 0, 0))
        super().draw(window, state, save_state)
        congrat = self.font.render("CONGRATULATION!!", True, "yellow")
        congrat2 = self.font.render("You have won the game", True, "yellow")
        window.blit(congrat, congrat.get_rect(center=(self.win_w // 2, 100)))
        window.blit(congrat2, congrat2.get_rect(center=(self.win_w // 2, 150)))
