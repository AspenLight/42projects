import pygame
import tkinter
from utils import (
    Inputs,
    State,
    SaveSystem,
    Player,
    Ghost,
    Maze,
    MARGIN,
    KEY_TO_DIR,
    SPRITE_DIM,
    PLAYER_FRAMES,
    GHOST_FRAMES,
    BOTTOM_BAR,
    FPS,
    Screen,
    MainMenu,
    GameOverScreen,
    GameScreen,
    PauseMenu,
    VictoryScreen,
)

# --------------------------------------------------------------------------
# Loading helpers
# --------------------------------------------------------------------------


def get_img(
    sheet: pygame.Surface, row: int, col: int, size: int, out_size: int
) -> pygame.Surface:
    image = pygame.Surface((size, size), pygame.SRCALPHA)
    image.blit(sheet, (0, 0), pygame.Rect(col * size, row * size, size, size))
    scaled = int(out_size / 1.5)
    return pygame.transform.scale(image, (scaled, scaled))


def load_player(
    cell_size: int,
    sheet: pygame.Surface,
    center_coord: pygame.Vector2,
    state: State,
) -> Player:
    player = Player(cell_size)
    player.frames = [
        get_img(sheet, row, col, SPRITE_DIM, cell_size)
        for row, col in PLAYER_FRAMES
    ]
    player.grid_position = center_coord
    player.set_animation(None)
    if state.cheat.increased_speed:
        player.speed *= 2
    return player


def load_ghost(
    ghost: Ghost,
    cell_size: int,
    sheet: pygame.Surface,
    id: int,
    start_pos: pygame.Vector2,
) -> Ghost:
    ghost.frames = [
        get_img(sheet, row, col, SPRITE_DIM, cell_size)
        for row, col in GHOST_FRAMES[id]
    ]
    ghost.vul_frames = [
        get_img(sheet, row, col, SPRITE_DIM, cell_size)
        for row, col in GHOST_FRAMES[4]
    ]
    ghost.dead_frames = [
        get_img(sheet, row, col, SPRITE_DIM, cell_size)
        for row, col in GHOST_FRAMES[5]
    ]
    ghost.grid_position = start_pos
    ghost.set_animation(None, id, True)
    ghost.start_pos = start_pos
    return ghost


def load_ghosts(
    cell_size: int, sheet: pygame.Surface, m_w: int, m_h: int
) -> tuple[Ghost, Ghost, Ghost, Ghost]:
    return (
        load_ghost(
            Ghost(cell_size), cell_size, sheet, 0, pygame.Vector2(0, 0)
        ),
        load_ghost(
            Ghost(cell_size), cell_size, sheet, 1, pygame.Vector2(m_w - 1, 0)
        ),
        load_ghost(
            Ghost(cell_size), cell_size, sheet, 2, pygame.Vector2(0, m_h - 1)
        ),
        load_ghost(
            Ghost(cell_size),
            cell_size,
            sheet,
            3,
            pygame.Vector2(m_w - 1, m_h - 1),
        ),
    )


# --------------------------------------------------------------------------
# Input and shared state
# --------------------------------------------------------------------------


def handle_events(inp: Inputs, savefile: SaveSystem, state: State) -> bool:
    inp.pressed.clear()
    inp.typed.clear()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.TEXTINPUT:
            inp.typed.append(event.text)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                savefile.export()
                return False
            if state.mode == "game":
                if event.key == pygame.K_SPACE:
                    state.mode = "pause"
                if event.key == pygame.K_l:
                    state.cheat.lvl_skip = True
            inp.pressed.append(event.key)
            if event.key in KEY_TO_DIR and event.key not in inp.held:
                inp.held.append(event.key)
        elif event.type == pygame.KEYUP and event.key in inp.held:
            inp.held.remove(event.key)
    return True


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------
def main() -> None:
    root = tkinter.Tk()
    root.withdraw()
    monitor_w: int = root.winfo_screenwidth()
    # monitor_h = root.winfo_screenheight()
    state = State()
    savefile = SaveSystem()
    if savefile.loading(state) is False:
        return
    pygame.init()
    pygame.display.set_caption("PAC-MAN")
    info = pygame.display.Info()
    state.compute_cell_size(info.current_w, info.current_h)
    if (
        state.cell_size * state.m_width >= info.current_w
        or state.cell_size * state.m_height >= info.current_h
    ):
        print("change Maze size")
        return
    window_width = 2 * MARGIN + state.cell_size * state.m_width
    window_height = 2 * MARGIN + state.cell_size * state.m_height + BOTTOM_BAR
    if window_width < monitor_w // 1.5:
        window_width = int(monitor_w // 1.5)
    if window_height < 800:
        window_height = 800
    window = pygame.display.set_mode((window_width, window_height))
    pygame.key.stop_text_input()
    clock = pygame.time.Clock()
    sheet = pygame.image.load("pac_sheet.png").convert_alpha()
    maze = Maze(state)
    centerwidth = (
        state.m_width // 2 - 1
        if state.m_width % 2 == 0
        else state.m_width // 2
    )
    player_template = load_player(
        state.cell_size,
        sheet,
        pygame.Vector2(centerwidth, state.m_height // 2),
        state,
    )
    ghosts_template = load_ghosts(
        state.cell_size, sheet, state.m_width, state.m_height
    )

    title_font = pygame.font.SysFont(None, 100)
    button_font = pygame.font.SysFont(None, 48)
    win_w = window.get_width()

    inp = Inputs()
    screens: dict[str, Screen] = {
        "main menu": MainMenu(
            "PAC MAN",
            [
                ("Select to play", "game"),
                ("Invicibility", ""),
                ("extra_life", ""),
                ("ghost_freeze", ""),
                ("increased_speed", ""),
            ],
            title_font,
            button_font,
            win_w,
        ),
        "pause": PauseMenu(
            "PAUSE",
            [
                ("get back to the game", "game"),
                ("get back to the main menu", "main menu"),
            ],
            title_font,
            button_font,
            win_w,
        ),
        "gameover": GameOverScreen(button_font, win_w, state.current_score),
        "win": VictoryScreen(button_font, win_w, state.current_score),
        "game": GameScreen(player_template, maze, ghosts_template),
    }
    running = True
    while running:
        screen = screens[state.mode]
        running = handle_events(inp, savefile, state)
        next_mode = screen.update(inp, state, savefile)
        screen.draw(window, state, savefile)
        if next_mode and next_mode != state.mode:
            state.mode = next_mode
            inp.held.clear()
            if state.ingame is False:
                screens[next_mode].on_enter(state)
        pygame.display.flip()
        state.dt = clock.tick(FPS)
    print("\033[H\033[J", end="")
    pygame.quit()


if __name__ == "__main__":
    main()
