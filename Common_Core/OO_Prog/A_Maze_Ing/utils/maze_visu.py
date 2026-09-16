from pymlx import Mlx, Color
from .maze_gen import Direction, Maze, maze_generator


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


def maze_terminal_visu(a_maze: Maze) -> None:
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
    maze: Maze, perf: bool, m_height: int, m_width: int, args: tuple
) -> None:
    a_width, a_height, output_file, perfect, entry, exit, has_seed = args
    height = m_height * 36 + 130
    width = m_width * 36 + 50
    start_x = 25
    start_y = 25
    options = [
        "1. Re-generate a new maze",
        "2. Show/Hide path from entry to exit",
        "3. Rotate maze colors",
        "4. Quit",
    ]
    with Mlx() as mlx:
        win = mlx.new_window(width, height, "a_maze_ing")
        img = mlx.new_image(width, height)
        coloring = 0
        # color options = walls, 42, outer
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

        def handle_keypress(key):
            nonlocal coloring
            nonlocal maze
            if key in (49, 65436):
                if not has_seed:
                    maze = maze_generator(perfect, (a_height, a_width))
                maze_terminal_visu(maze)
                draw_scene()
            elif key in (52, 65430):
                mlx.loop_end()
            elif key in (51, 65435):
                if coloring < len(maze_colors) - 1:
                    coloring += 1
                else:
                    coloring = 0
                draw_scene()
            # elif key == 50 or key == 65433:

        def draw_scene():
            for x in range(maze.height):
                for y in range(maze.width):
                    pos_x = start_x + (y * 36)
                    pos_y = start_y + (x * 36)
                    current_tile = maze.contain[x][y]
                    # Full tiles
                    img.draw_rect_outline(
                        pos_x,
                        pos_y,
                        35,
                        35,
                        maze_colors[coloring][0],
                        thickness=1,
                    )
            for x in range(maze.height):
                for y in range(maze.width):
                    pos_x = start_x + (y * 36)
                    pos_y = start_y + (x * 36)
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
                                pos_x + 2, pos_y + 2, 35, 35, Color.BLACK
                            )
                    if y < maze.width - 1:
                        next_tile = maze.contain[x][y + 1]
                        if not is_wall(True, current_tile, next_tile):
                            img.draw_rect(
                                pos_x + 35, pos_y + 1, 4, 34, Color.BLACK
                            )
                    if x < maze.height - 1:
                        below_tile = maze.contain[x + 1][y]
                        if not is_wall(False, current_tile, below_tile):
                            img.draw_rect(
                                pos_x + 1, pos_y + 35, 34, 4, Color.BLACK
                            )
                    if current_tile == 16:
                        img.draw_rect(
                            pos_x - 1,
                            pos_y - 1,
                            38,
                            38,
                            maze_colors[coloring][1],
                        )
                        continue
            img.draw_rect_outline(
                start_x - 5,
                start_y - 5,
                maze.width * 36 + 9,
                maze.height * 36 + 9,
                maze_colors[coloring][2],
                thickness=5,
            )
            win.put_image(img)
            option_offset = 0
            for option in options:
                win.string_put(
                    m_width * 30 // 2,
                    m_height * 36 + 60 + option_offset,
                    Color.WHITE,
                    option,
                )
                option_offset += 15

        win.on_close(mlx.loop_end)
        win.on_key(handle_keypress)
        draw_scene()
        mlx.loop()
