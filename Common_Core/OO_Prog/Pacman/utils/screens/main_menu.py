from ..consts import YELLOW, RULES
from typing import Optional, cast
from ..system_data import (
    Inputs,
    State,
    SaveSystem,
)
import pygame
from .basis_screens import MenuScreen, Button


class MainMenu(MenuScreen):
    def __init__(
        self,
        title: str,
        items: list[tuple[str, str]],  # (label, target mode)
        title_font: pygame.font.Font,
        button_font: pygame.font.Font,
        win_w: int,
        show_name: bool = False,
    ):
        super().__init__(
            title, items[:1], title_font, button_font, win_w, show_name
        )
        self.cheat_targets = [target for target, _ in items[1:]]
        self.cheats: list[tuple[Button, bool]] = [
            (
                Button(
                    label,
                    (win_w // 2, 300),
                    (200, 70),
                    pygame.font.SysFont(None, 36),
                    False,
                ),
                False,
            )
            for label, _ in items[1:]
        ]
        self.row = 0
        self.cheat_sel = 0

    def wrap(self, text: str, font: pygame.font.Font, max_w: int) -> list[str]:
        lines: list[str] = []
        current = ""
        for word in text.split():
            test = f"{current} {word}".strip()
            if font.size(test)[0] <= max_w:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines

    def draw_rules(self, window: pygame.Surface) -> None:
        small_font = pygame.font.SysFont(None, 21)
        margin = 30
        max_w = 380
        x = window.get_width() - margin - max_w
        y = 35
        header = small_font.render("Rules:", True, YELLOW)
        window.blit(header, (x, y))
        y += header.get_height() + 8
        for rule in RULES:
            for chunk in self.wrap(rule, small_font, max_w):
                surf = small_font.render(chunk, True, YELLOW)
                window.blit(surf, (x + 15, y))
                y += surf.get_height() + 4
            y += 6
        controls_img = pygame.image.load("controls.png").convert_alpha()
        w_controls_img = cast(pygame.Surface, controls_img)
        window.blit(
            w_controls_img,
            (130, 35),
        )

    def draw(
        self, window: pygame.Surface, state: State, save_state: SaveSystem
    ) -> None:
        state.vul_ghosts = False
        # print(state.vul_ghosts)
        offset = 0
        window.fill((0, 0, 0))
        title = self.title_font.render(self.title, True, YELLOW)
        window.blit(title, title.get_rect(center=(self.win_w // 2, 100)))
        scoring = self.score_font.render("highscores:", True, "white")
        window.blit(scoring, scoring.get_rect(center=(self.win_w // 2, 350)))
        for button in self.buttons:
            button.draw(window)
        n = len(self.cheats)
        spacing = 250  # a bit more than the button width
        for k, cheat in enumerate(self.cheats):
            cheat[0].draw(
                window,
                int((k - (n - 1) / 2) * spacing),
                1,
                text=(
                    f"{cheat[0].text} [+{state.cheat.extra_lives}]"
                    if self.cheat_targets[k] == "extra_life"
                    else f"{cheat[0].text} [{'+' if cheat[1] else ' '}]"
                ),
            )
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
                name, name.get_rect(center=(self.win_w // 2, 400 + offset))
            )

            offset += 35
            i += 1
        self.draw_rules(window)

    def _refresh_hover(self) -> None:
        for button in self.buttons:
            button.hover = self.row == 0
        for k, cheat in enumerate(self.cheats):
            cheat[0].hover = self.row == 1 and k == self.cheat_sel

    def on_enter(self, state: State) -> None:
        self.row = 0
        self.cheat_sel = 0
        self._refresh_hover()

    def apply_cheat(self, state: State, name: str, id: int) -> None:
        match name:
            case "Invicibility":
                state.cheat.invicibility = not state.cheat.invicibility
                self.cheats[id] = (
                    self.cheats[id][0],
                    state.cheat.invicibility,
                )
            case "extra_life":
                if state.cheat.extra_lives == 10:
                    state.cheat.extra_lives = 0
                else:
                    state.cheat.extra_lives = min(
                        state.cheat.extra_lives + 1, 10
                    )
            case "ghost_freeze":
                state.cheat.ghost_freeze = not state.cheat.ghost_freeze
                self.cheats[id] = (
                    self.cheats[id][0],
                    state.cheat.ghost_freeze,
                )
            case "increased_speed":
                state.cheat.increased_speed = not state.cheat.increased_speed
                self.cheats[id] = (
                    self.cheats[id][0],
                    state.cheat.increased_speed,
                )

    def update(
        self, inp: Inputs, state: State, save_state: SaveSystem
    ) -> Optional[str]:
        if state.ingame:
            state.ingame = False
        for key in inp.pressed:
            up = key == pygame.K_UP or key == pygame.K_w
            down = key == pygame.K_DOWN or key == pygame.K_s
            left = key == pygame.K_LEFT or key == pygame.K_a
            right = key == pygame.K_RIGHT or key == pygame.K_d
            if up:
                if self.row != 0:
                    self.row -= 1
            elif down:
                if self.row != len(self.buttons):
                    self.row += 1
            if self.row == 1:
                if left and self.cheat_sel != 0:
                    self.cheat_sel -= 1
                elif right and self.cheat_sel != len(self.cheats) - 1:
                    self.cheat_sel += 1
            self._refresh_hover()
            if key == pygame.K_SPACE:
                match self.row:
                    case 0:
                        return self.targets[self.selected]
                    case 1:
                        # print(self.cheat_targets[self.cheat_sel])
                        self.apply_cheat(
                            state,
                            self.cheat_targets[self.cheat_sel],
                            self.cheat_sel,
                        )
        return None
