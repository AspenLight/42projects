from typing import Optional
import pygame
from ..system_data import (
    Inputs,
    State,
    SaveSystem,
)


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
        self.hover = hover

    def draw(
        self,
        window: pygame.Surface,
        offset: int = 0,
        axis: int = 0,
        text: str | None = None,
    ) -> None:
        rect = self.rect.copy()
        if axis == 1:
            rect.x += offset
        else:
            rect.y += offset
        pygame.draw.rect(window, "black", rect)

        shown = self.text if text is None else text
        label = (
            self.font.render(shown, True, "white")
            if not self.hover
            else self.font.render(f">{shown}", True, "yellow")
        )
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
        pass

    def update(
        self, inp: Inputs, state: State, save_state: SaveSystem
    ) -> Optional[str]:
        pass

    def draw(
        self, window: pygame.Surface, state: State, save_state: SaveSystem
    ) -> None:
        pass
