import random

from utils import (
    app_maze_visuals,
    ArgError,
    InvArgError,
    InvValError,
    maze_to_txt,
)
from src.mazegen import MazeGenerator, maze_solver

import sys


def config_extract(args: str) -> dict:
    print("Arguments extraction .....\n")
    dic_args = {}
    try:
        arguments = open(args, "r", encoding="utf-8")
    except Exception as e:
        print(f"Error opening file '{args}': {e}")
        return {}
    for line in arguments:
        print(line)
        arg = line.split("=")
        dic_args[arg[0]] = arg[1].replace("\n", "")
    arguments.close()
    return dic_args


def maze_gestion(args: tuple, seed: int) -> None:
    width, height, output_file, perfect, entry, exit, has_seed = args
    print("Maze creation...")
    maze = MazeGenerator.maze_generator(
        MazeGenerator((height, width)), perfect, entry, exit, seed
    )
    print("Path finding....")
    path: str = maze_solver(
        (entry[1], entry[0]), (exit[1], exit[0]), maze.contain
    )
    maze_to_txt(
        maze,
        output_file,
        path,
        f"\n{entry[0]},{entry[1]}\n{exit[0]},{exit[1]}\n",
    )
    # print("Maze terminal visualisation.....")
    # maze_terminal_visu(maze)
    print("Maze app visualisation.....")
    app_maze_visuals(maze, perfect, args, path, seed)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: main.py <arguments file>.txt")
    else:
        arguments = sys.argv[1]
        dict_of_args = config_extract(arguments)
        file_name = f"{arguments}\n"
        try:
            valid_args = [
                "WIDTH",
                "HEIGHT",
                "OUTPUT_FILE",
                "PERFECT",
                "ENTRY",
                "EXIT",
                "SEED",
            ]
            dim = ["HEIGTH", "WIDTH"]
            name = ["ENTRY", "EXIT"]

            for key in valid_args:
                if key not in dict_of_args:
                    raise ArgError(key)
            for arg in list(dict_of_args):
                if arg not in valid_args:
                    raise InvArgError(arg)
            try:
                height = int(dict_of_args["HEIGHT"])
                width = int(dict_of_args["WIDTH"])
            except BaseException as e:
                raise BaseException(f"width/height value problem: {e}")
            count = 0
            for dim_val in (height, width):
                if dim_val < 5:
                    raise InvValError(f"{dim[count]} value too low: {dim_val}")
                count += 1
            output_file = str(dict_of_args["OUTPUT_FILE"])
            dimentions = (height, width)
            if dict_of_args["PERFECT"] not in ["True", "False"]:
                raise InvValError(f"'PERFECT' = {dict_of_args["PERFECT"]}")
            else:
                perfect = dict_of_args["PERFECT"] == "True"
            try:
                entry = tuple(
                    [int(coord) for coord in dict_of_args["ENTRY"].split(",")]
                )
                exit = tuple(
                    [int(coord) for coord in dict_of_args["EXIT"].split(",")]
                )
            except BaseException as e:
                raise BaseException(f"entry/exit value problem: {e}")
            has_seed = False
            if dict_of_args["SEED"]:
                seed = dict_of_args["SEED"]
                random.seed(seed)
                has_seed = True
            else:
                seed = random.randint(0, 1000000)
                random.seed(seed)
            dim_count = 0
            for point in (entry, exit):
                err_msg = "doesn't have the correct number of values"
                if len(point) != 2:
                    raise InvValError(
                        f"'{name[dim_count]}' {err_msg}"
                    )
                count = 0
                for coord in point:
                    msg_1 = f"{point} value n°{count+1} = {coord}"
                    msg_2 = f"'{name[dim_count]}' = {msg_1}"
                    msg_3 = f"{dim[count]} = {dimentions[count]}"
                    if not (0 <= coord <= dimentions[count] - 1):
                        raise InvValError(
                            f"'{msg_2} is out of bound of {msg_3}"
                        )
                    count += 1
                dim_count += 1
            maze_gestion(
                (width, height, output_file, perfect, entry, exit, has_seed),
                seed,
            )
        except ArgError as e:
            print(e)
            print(
                f"please add the missing argument in {file_name}"
            )
        except InvArgError as e:
            print(e)
            print(
                f"please remove the invalid argument in {file_name}"
            )
        except InvValError as e:
            print(e)
            print(
                f"please change the argument value in {file_name}"
            )
        except Exception as e:
            print(e)
        except BaseException as e:
            print(e)
            print(
                f"please change the argument value in {file_name}"
            )
