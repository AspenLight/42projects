from dataclasses import dataclass, field
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


@dataclass
class State:
    mode: str = "main menu"
    name: str = ""
    current_score: int = 0
    m_width: int = 15
    m_height: int = 15
    life: int = 3
    end_life: bool = False
    debugg: bool = False
    dt: int = 0
    cell_size: int = 0
    level_sys = LevelSystem()
    timer: float = 0.0
    vul_ghosts: bool = False
    vul_timer: float = 0.0

    def compute_cell_size(self, screen_w: int, screen_h: int) -> None:
        size = (
            max(4, min(screen_h // self.m_height, screen_w // self.m_width))
            // 2
        )
        self.cell_size = max(size, 10)

    def timer_handle(self) -> None:
        return


class SaveSystem:
    def __init__(self) -> None:
        self.scores: dict[str, int] = field(default_factory=dict)
        self.datas = {}
        self.file = ""

    def loading(self, state: State) -> bool:
        args = sys.argv[1:]
        if len(args) == 0:
            print("Usage: main.py <file.json>")
            return False
        try:
            self.file = args[0]
            with open(args[0], "r") as file:
                self.data = json_parse(file)
                self.scores = self.data["scores"]
                state.m_height, state.m_width = self.data["width-height"]
                state.level_sys.pac_gums = self.data["pac_gums"]
                state.level_sys.points_per_pacgum = self.data[
                    "points_per_pacgum"
                ]
                state.level_sys.points_per_super_pacgum = self.data[
                    "points_per_super_pacgum"
                ]
                state.level_sys.points_per_ghost = self.data[
                    "points_per_ghost"
                ]
                state.level_sys.level_max_time = self.data["level_max_time"]
                if self.data.get("seed"):
                    state.level_sys.seed = self.data["seed"]
                else:
                    state.level_sys.seed = random.randint(0, 1000000)
                random.seed(state.level_sys.seed)
                print(state.level_sys.seed)
            return True
        except Exception as e:
            print(f"Error opening file '{args[0]}': {e}")
            return False

    def export(self):
        self.data["scores"] = self.scores
        with open(self.file, "w") as file:
            file.write(json.dumps(self.data))
