import random

from utils import (
    maze_generator,
    app_maze_visuals,
    maze_terminal_visu,
    ArgError,
    InvArgError,
    InvValError,
    maze_to_txt,
    maze_solver,
)

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


def maze_gestion(args: tuple) -> None:
    width, height, output_file, perfect, entry, exit, has_seed = args
    maze = maze_generator(perfect, (height, width))
    path: str = maze_solver(entry, exit, maze.contain)
    maze_to_txt(maze, output_file)
    maze_terminal_visu(maze)
    app_maze_visuals(maze, perfect, maze.height, maze.width, args)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: main.py <arguments file>.txt")
    else:
        arguments = sys.argv[1]
        dict_of_args = config_extract(arguments)
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
                width = int(dict_of_args["WIDTH"])
                height = int(dict_of_args["HEIGHT"])
            except BaseException as e:
                raise BaseException(f"width/height value problem: {e}")
            count = 0
            for dim_val in (width, height):
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
                if len(point) != 2:
                    raise InvValError(
                        f"'{name[dim_count]}' doesn't have the correct number of values"
                    )
                count = 0
                for coord in point:
                    if not (0 <= coord <= dimentions[count] - 1):
                        raise InvValError(
                            f"'{name[dim_count]}' = {point} value n°{count+1} = {coord} is out of bound of {dim[count]} = {dimentions[count]}"
                        )
                    count += 1
                dim_count += 1
            maze_gestion(
                (width, height, output_file, perfect, entry, exit, has_seed)
            )

        except ArgError as e:
            print(e)
            print(
                "please add the missing argument in your <arguments file>.txt\n"
            )
        except InvArgError as e:
            print(e)
            print(
                "please remove the invalid argument in your <arguments file>.txt\n"
            )
        except InvValError as e:
            print(e)
            print(
                "please change the argument value in your <arguments file>.txt\n"
            )
        except Exception as e:
            print(e)
        except BaseException as e:
            print(e)
            print(
                "please change the argument value in your <arguments file>.txt\n"
            )
