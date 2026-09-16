from .maze_gen import Maze


def hexa_trad(dec: int) -> str:
    hexa_table = "0123456789ABCDEF"
    hex = dec % 16
    return hexa_table[hex]


def maze_to_txt(maze: Maze, file_name: str) -> None:
    output_file = file_name
    buffer = ""
    for x in range(maze.height):
        for y in range(maze.width):
            if maze.contain[x][y] == 16:
                buffer += "F"
            else:
                buffer += hexa_trad(maze.contain[x][y])
        buffer += "\n"
    with open(output_file, "w", encoding="utf-8") as outfile_file:
        outfile_file.write(buffer)
    #     print(f"Data saved in file '{output_file}'.")
