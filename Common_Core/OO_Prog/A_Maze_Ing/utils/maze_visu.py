from pymlx import Mlx, Color
from src.mazegen import Direction, MazeGenerator, maze_solver
from Xlib import display


# 791871
def is_wall(type: bool, tile: int, next_tile: int | None) -> bool:
    if tile == 16:
        return True
    if next_tile is None:
        return True
    if type:
        wall = (tile & Direction.EAST.value) != 0 or (
            next_tile & Direction.WEST.value
        ) != 0
    else:
        wall = (tile & Direction.SOUTH.value) != 0 or (
            next_tile & Direction.NORTH.value
        ) != 0
    return wall


def maze_terminal_visu(a_maze: MazeGenerator) -> None:
    print("██" * (a_maze.width * 2 + 1))

    for x in range(a_maze.height):
        row = "██"
        south_row = "██"

        for y in range(a_maze.width):
            current_tile = a_maze.contain[x][y]

            if current_tile == 16:
                row += "TT██"
            elif y == a_maze.width - 1:
                row += "  ██"
            else:
                next_tile = a_maze.contain[x][y + 1]
                if is_wall(True, current_tile, next_tile):
                    row += "  ██"
                else:
                    row += "    "

            if x == a_maze.height - 1:
                south_row += "████"
            else:
                below_tile = a_maze.contain[x + 1][y]
                if is_wall(False, current_tile, below_tile):
                    south_row += "████"
                else:
                    south_row += "  ██"

        print(row)
        print(south_row)
    print("\n")


def app_maze_visuals(
    maze: MazeGenerator,
    perf: bool,
    args: tuple,
    path: str,
    seed: int,
) -> None:
    a_width, a_height, output_file, perfect, entry, exit, has_seed = args
    d = display.Display()
    screen = d.screen()
    s_width, s_height = screen.width_in_pixels, screen.height_in_pixels
    cell_size = round(
        max(4, min(s_height // a_height, s_width // a_width)) // 1.5
    )
    side = max(
        a_height * round(cell_size * 1.3), a_width * round(cell_size * 1.3)
    )
    height = a_height * round(cell_size * 1.3)
    width = a_width * round(cell_size * 1.3)
    if width < 300:
        width = 300
    start_y = 25
    start_x = (width - (a_width * cell_size)) // 2
    options = [
        "1. Re-generate a new maze",
        "2. Show/Hide path from entry to exit",
        "3. Rotate maze colors",
        "4. Quit",
    ]
    d.close()
    with Mlx() as mlx:
        win = mlx.new_window(width, height, "a_maze_ing")
        coloring = 0
        pathing = True
        # color options = walls, 42, outer, path
        maze_colors = [
            (Color.WHITE, Color.BLUE, Color.BLUE),
            (0xD60270, 0x9B4F96, 0x0038A8),
            (0x9B4F96, 0x0038A8, 0xD60270),
            (0x5BCEFA, 0xF5A9B8, 0xFFFFFF),
            (0xF5A9B8, 0xFFFFFF, 0x5BCEFA),
            (0xFF0055, 0x00FF66, 0xFFCC00),
            (0xFFCC00, 0xFF0055, 0x00FF66),
            (0x00FF66, 0xFFCC00, 0xFF0055),
        ]

        def handle_keypress(key: int) -> None:
            nonlocal pathing
            nonlocal coloring
            nonlocal maze
            nonlocal path
            if key in (49, 65436):
                print("Maze REcreation...")
                if not has_seed:
                    maze = maze.maze_generator(perfect, entry, exit, seed)
                # maze_terminal_visu(maze)
                path = maze_solver(
                    (entry[1], entry[0]), (exit[1], exit[0]), maze.contain
                )
                draw_scene()
            elif key in (52, 65430):
                mlx.loop_end()
            elif key in (51, 65435):
                if coloring < len(maze_colors) - 1:
                    coloring += 1
                else:
                    coloring = 0
                draw_scene()
            elif key in (50, 65433):
                pathing = not pathing
                draw_scene()

        img = mlx.new_image(side, side)

        def draw_scene() -> None:
            print("\tstep 1..")
            img.clear(Color.BLACK)
            for x in range(maze.height):
                for y in range(maze.width):
                    pos_x = start_x + (y * cell_size)
                    pos_y = start_y + (x * cell_size)
                    current_tile = maze.contain[x][y]
                    # Full tiles
                    img.draw_rect_outline(
                        pos_x,
                        pos_y,
                        cell_size,
                        cell_size,
                        maze_colors[coloring][0],
                        thickness=1,
                    )
            print("\tstep 2..")
            for x in range(maze.height):
                for y in range(maze.width):
                    pos_x = start_x + (y * cell_size)
                    pos_y = start_y + (x * cell_size)
                    current_tile = maze.contain[x][y]
                    next_tile = None
                    below_tile = None
                    if (
                        y < maze.width - 1 and x < maze.height - 1
                    ) and not perf:
                        next_tile = maze.contain[x][y + 1]
                        below_tile = maze.contain[x + 1][y]
                        if not is_wall(
                            True, current_tile, next_tile
                        ) and not is_wall(False, current_tile, below_tile):
                            img.draw_rect(
                                pos_x + 1,
                                pos_y + 1,
                                cell_size,
                                cell_size,
                                Color.BLACK,
                            )
                    if y < maze.width - 1:
                        next_tile = maze.contain[x][y + 1]
                        if not is_wall(True, current_tile, next_tile):
                            img.draw_rect(
                                pos_x + cell_size,
                                pos_y + 1,
                                4,
                                cell_size - 1,
                                Color.BLACK,
                            )
                    if x < maze.height - 1:
                        below_tile = maze.contain[x + 1][y]
                        if not is_wall(False, current_tile, below_tile):
                            img.draw_rect(
                                pos_x + 1,
                                pos_y + cell_size,
                                cell_size - 1,
                                4,
                                Color.BLACK,
                            )
                    if current_tile == 16:
                        img.draw_rect(
                            pos_x - 1,
                            pos_y - 1,
                            cell_size + 2,
                            cell_size + 2,
                            maze_colors[coloring][1],
                        )
                        continue
            print("\tstep 3..")
            img.draw_rect_outline(
                start_x - 5,
                start_y - 5,
                a_width * cell_size + 10,
                a_height * cell_size + 10,
                maze_colors[coloring][2],
                thickness=5,
            )
            print("\tstep 4..")
            if pathing is False:
                circ = 4
                if cell_size < 8:
                    circ = 1
                elif cell_size < 17:
                    circ = 2
                cell_x, cell_y = entry[0], entry[1]
                img.draw_circle(
                    (cell_y * (cell_size)) + start_x + cell_size // 2,
                    (cell_x * (cell_size)) + start_y + cell_size // 2,
                    circ,
                    Color.YELLOW,
                )
                for i in range(len(path)):
                    match path[i]:
                        case "N":
                            img.draw_rect(
                                (
                                    (cell_y * (cell_size))
                                    + start_x
                                    + cell_size // 2
                                )
                                - 1,
                                (cell_x * (cell_size))
                                + start_y
                                - cell_size // 2,
                                circ,
                                (cell_size),
                                Color.YELLOW,
                            )
                            cell_x -= 1
                        case "S":
                            img.draw_rect(
                                (
                                    (cell_y * (cell_size))
                                    + start_x
                                    + cell_size // 2
                                )
                                - 1,
                                (cell_x * (cell_size))
                                + start_y
                                + cell_size // 2,
                                circ,
                                (cell_size),
                                Color.YELLOW,
                            )
                            cell_x += 1
                        case "E":
                            img.draw_rect(
                                (
                                    (cell_y * (cell_size))
                                    + start_x
                                    + cell_size // 2
                                )
                                - 1,
                                (cell_x * (cell_size))
                                + start_y
                                + cell_size // 2,
                                (cell_size),
                                circ,
                                Color.YELLOW,
                            )
                            cell_y += 1
                        case "W":
                            img.draw_rect(
                                (cell_y * (cell_size))
                                + start_x
                                - cell_size // 2,
                                (
                                    (cell_x * (cell_size))
                                    + start_y
                                    + cell_size // 2
                                )
                                - 1,
                                (cell_size),
                                circ,
                                Color.YELLOW,
                            )
                            cell_y -= 1
                    img.draw_circle(
                        (cell_y * (cell_size)) + start_x + cell_size // 2,
                        (cell_x * (cell_size)) + start_y + cell_size // 2,
                        circ,
                        Color.YELLOW,
                    )

            win.put_image(img)
            option_offset = 0
            for option in options:
                win.string_put(
                    round(a_width * cell_size // 2),
                    a_height * cell_size + 60 + option_offset,
                    Color.WHITE,
                    option,
                )
                option_offset += 15

        win.on_close(mlx.loop_end)
        win.on_key(handle_keypress)
        draw_scene()
        mlx.loop()
