from typing import Optional
import pygame

MARGIN: int = 15
FPS: int = 60
SPRITE_DIM: int = 31
ANIM_STEP_MS: int = 100  # time per animation frame
BOTTOM_BAR: int = 70  # extra space under the maze (for score, etc.)
MAX_NAME_LEN: int = 10
YELLOW = (255, 227, 0)
KEY_TO_DIR: dict[int, str] = {
    pygame.K_w: "up",
    pygame.K_UP: "up",
    pygame.K_s: "down",
    pygame.K_DOWN: "down",
    pygame.K_a: "left",
    pygame.K_LEFT: "left",
    pygame.K_d: "right",
    pygame.K_RIGHT: "right",
}
VECTORS: dict[str, pygame.Vector2] = {
    "up": pygame.Vector2(0, -1),
    "down": pygame.Vector2(0, 1),
    "left": pygame.Vector2(-1, 0),
    "right": pygame.Vector2(1, 0),
}
PLAYER_FRAMES: list[tuple[int, int]] = [
    (8, 1),
    (8, 2),
    (8, 3),
    (8, 4),
    (8, 5),
    (9, 2),
    (9, 3),
    (9, 4),
    (9, 5),
    (8, 0),
    (9, 0),
    (9, 1),
]
GHOST_FRAMES: list[list[tuple[int, int]]] = [
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)],
    [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)],
    [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)],
    [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3)],
    [
        (0, 4),  # 0 right1
        (0, 5),  # 1 right3
        (1, 4),  # 2 right2
        (1, 5),  # 3 right4
        (2, 4),  # 4 down1
        (2, 5),  # 5 down3
        (3, 4),  # 6 down2
        (3, 5),  # 7 down4
        (4, 4),  # 8 left1
        (4, 5),  # 9 left3
        (5, 4),  # 10 left2
        (5, 5),  # 11 left4
        (6, 4),  # 12 up1
        (6, 5),  # 13 up3
        (7, 4),  # 14 up2
        (7, 5),  # 15 up4
    ],
]
IDLE: tuple[int, ...] = (0, 0, 0, 0)
# Keys are Optional[str] because set_animation() can be called with None
PLAYER_ANIMATIONS: dict[Optional[str], tuple[int, ...]] = {
    "up": (0, 5, 6, 5),
    "down": (0, 3, 4, 3),
    "left": (0, 7, 8, 7),
    "right": (0, 1, 2, 1),
    "dead": (0, 9, 10, 11),
}
GHOST_ANIMATIONS: dict[Optional[str], tuple[int, ...]] = {
    "up": (6, 7),
    "down": (2, 3),
    "left": (4, 5),
    "right": (0, 1),
    "v_up": (12, 14, 13, 15),
    "v_down": (4, 6, 5, 7),
    "v_left": (8, 10, 9, 11),
    "v_right": (0, 2, 1, 3),
}
