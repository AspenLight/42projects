from dataclasses import dataclass, field
from typing import Any
import pygame
import sys
import json
from .parser import json_parse
import random


@dataclass
class Inputs:
    held: list[int] = field(default_factory=list)  # direction keys (game)
    pressed: list[int] = field(default_factory=list)  # new key presses
    typed: list[str] = field(default_factory=list)  # TEXTINPUT this frame


@dataclass
class LevelSystem:
    points_per_pacgum: int = field(default_factory=int)
    points_per_super_pacgum: int = field(default_factory=int)
    points_per_ghost: int = field(default_factory=int)
    seed: int = field(default_factory=int)
    level_max_time: int = field(default_factory=int)
    pac_gums: int = field(default_factory=int)
    level: int = 1


class Cheat:
    invicibility: bool = False
    lvl_skip: bool = False
    ghost_freeze: bool = False
    extra_lives: int = 0
    increased_speed: bool = False


@dataclass
class State:
    mode: str = "main menu"
    name: str = ""
    current_score: int = 0
    m_width: int = 10
    m_height: int = 10
    life: int = 3
    end_life: bool = False
    debugg: bool = False
    dt: int = 0
    cell_size: int = 0
    level_sys = LevelSystem()
    timer: float = 0.0
    vul_ghosts: bool = False
    vul_timer: float = 0.0
    vul_gen: int = 0
    ingame: bool = False
    cheat: Cheat = Cheat()
    ghost_coords: list[pygame.Vector2] = field(default_factory=list)

    def compute_cell_size(self, screen_w: int, screen_h: int) -> None:
        size = (
            max(4, min(screen_h // self.m_height, screen_w // self.m_width))
            // 2
        )
        self.cell_size = max(size, 10)

    def timer_handle(self) -> None:
        return


class ConfigError(Exception):
    """The config file cannot be used at all."""


def warn(message: str) -> None:
    """Log a non-fatal config problem."""
    print(f"Config: {message}", file=sys.stderr)


def get_int(data: dict[str, Any], key: str, default: int, low: int) -> int:
    """Return data[key] as an int >= low, falling back to a default."""
    value: int = data.get(key, default)
    if isinstance(value, bool) or not isinstance(value, int):
        warn(f"'{key}' must be an integer, using {default}")
        return default
    if value < low:
        warn(f"'{key}' is too low ({value}), using {low}")
        return low
    return value


class SaveSystem:
    def __init__(self) -> None:
        self.scores: dict[str, int] = {}
        self.data: dict[str, Any] = {}
        self.file: str = ""

    @staticmethod
    def _read_config(path: str) -> dict[str, Any]:
        """Parse the config file or raise ConfigError."""
        try:
            with open(path, "r") as file:
                data = json_parse(file)
        except OSError as e:
            raise ConfigError(f"cannot open '{path}': {e.strerror}") from e
        except ValueError as e:  # adapt to what json_parse raises
            raise ConfigError(f"'{path}' is not valid JSON: {e}") from e
        if not isinstance(data, dict):
            raise ConfigError(f"'{path}' must contain a JSON object")
        return data

    @staticmethod
    def _ensure_int(value: Any, name: str) -> int:
        """Verify that a value is a strict integer (excluding booleans)."""
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(
                f"'{name}' must be an integer,",
                f"got {value} as type {type(value).__name__}",
            )
        return int(value)

    def loading(self, state: State) -> bool:
        self.file = "config.json"
        allowed_keys = {
            "scores",
            "height-width",
            "pac_gums",
            "points_per_pacgum",
            "points_per_super_pacgum",
            "points_per_ghost",
            "level_max_time",
            "seed",
        }

        try:
            self.data = self._read_config(self.file)

            # 1. Vérifier les clés inconnues
            for key in self.data:
                if key not in allowed_keys:
                    raise ConfigError(
                        f"invalid key found: '{key}', ",
                        f"please remove it from {self.file}",
                    )

            # 2. Validation de "scores" (dict[str, int], peut être vide {})
            raw_scores = self.data["scores"]
            if not isinstance(raw_scores, dict):
                raise TypeError("'scores' must be a JSON object")
            for player, score in raw_scores.items():
                if not isinstance(player, str):
                    raise TypeError("All keys in 'scores' must be strings")
                self._ensure_int(score, f"scores['{player}']")
            self.scores = raw_scores

            # 3. Validation de "height-width" (liste de 2 entiers >= min)
            wh = self.data["height-width"]
            if not isinstance(wh, list) or len(wh) != 2:
                raise ValueError("'width-height' must be a list of 2 integers")

            height = self._ensure_int(wh[0], "width-height[0]")
            width = self._ensure_int(wh[1], "width-height[1]")
            if height < 13 or width < 14:
                raise ValueError(
                    "height-width has one or both values too low",
                    f" (current: [{height}, {width}] min: [13, 14])",
                )
            state.m_height, state.m_width = height, width

            # 4. Validation des paramètres entiers du niveau
            int_fields = (
                "pac_gums",
                "points_per_pacgum",
                "points_per_super_pacgum",
                "points_per_ghost",
                "level_max_time",
            )
            validated = {
                field: self._ensure_int(self.data[field], field)
                for field in int_fields
            }

            if validated["pac_gums"] < 0 or validated["level_max_time"] <= 0:
                raise ValueError(
                    "'pac_gums' must be >= 0 and 'level_max_time' must be > 0"
                )
            if validated["pac_gums"] > height * width - 22:
                raise ValueError(
                    "'pac_gums' must be less",
                    "than the number of reachable tiles",
                    f" (current: {validated["pac_gums"]},",
                    f" max: {height * width - 22})",
                )
            state.level_sys.pac_gums = validated["pac_gums"]
            state.level_sys.points_per_pacgum = validated["points_per_pacgum"]
            state.level_sys.points_per_super_pacgum = validated[
                "points_per_super_pacgum"
            ]
            state.level_sys.points_per_ghost = validated["points_per_ghost"]
            state.level_sys.level_max_time = validated["level_max_time"]

            # 5. Gestion optionnelle et typée de "seed"
            if "seed" in self.data and self.data["seed"] is not None:
                state.level_sys.seed = self._ensure_int(
                    self.data["seed"], "seed"
                )
            else:
                state.level_sys.seed = random.randint(0, 1000000)
            random.seed(state.level_sys.seed)

            return True

        except KeyError as e:
            print(
                f"Missing key: {e}, please add it to {self.file}",
                file=sys.stderr,
            )
            return False
        except (ConfigError, ValueError, TypeError) as e:
            print(f"Config error: {e}", file=sys.stderr)
            return False

    def export(self) -> None:
        self.data["scores"] = self.scores
        with open(self.file, "w") as file:
            file.write(json.dumps(self.data))
