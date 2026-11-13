from ..consts import YELLOW
from typing import Optional
from ..system_data import (
    Inputs,
    State,
    SaveSystem,
)
import pygame
from .basis_screens import MenuScreen


class PauseMenu(MenuScreen):
    def draw(
        self, window: pygame.Surface, state: State, save_state: SaveSystem
    ) -> None:
        window.fill((0, 0, 0))
        title = self.title_font.render(self.title, True, YELLOW)
        window.blit(title, title.get_rect(center=(self.win_w // 2, 100)))

        for button in self.buttons:
            button.draw(window)

    def on_enter(self, state: State) -> None:
        self.selected = 0

    def update(
        self, inp: Inputs, state: State, save_state: SaveSystem
    ) -> Optional[str]:
        for key in inp.pressed:
            if key == pygame.K_UP:
                if self.selected != 0:
                    self.selected -= 1
            if key == pygame.K_DOWN:
                if self.selected != 1:
                    self.selected += 1
            for j, button in enumerate(self.buttons):
                button.hover = j == self.selected
                self.selected = self.selected
            if key == pygame.K_SPACE:
                return self.targets[self.selected]

        for key in inp.pressed:
            if key == pygame.K_UP:
                self.buttons[0].hover = True
                self.buttons[1].hover = False
                self.selected = 0
            if key == pygame.K_DOWN:
                self.buttons[0].hover = False
                self.buttons[1].hover = True
                self.selected = 1

            if key == pygame.K_SPACE:
                return self.targets[self.selected]
        return None
