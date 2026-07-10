import math


class CoordsError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def valid_coords(coords: list[str]) -> None:
    if len(coords) != 3:
        raise CoordsError("Invalid Syntax")
    for coord in coords:
        try:
            float(coord)
        except ValueError as err:
            print(f"Error on parameter '{coord}': ", end="")
            raise CoordsError(str(err))


def get_player_pos() -> tuple[float, ...]:
    while True:
        coords: str = input(
            "Enter new coordinates as floats in format ’x,y,z’: ")
        lst: list[str] = coords.split(",")
        try:
            valid_coords(lst)
        except CoordsError as err:
            print(err)
        else:
            return tuple(float(coord) for coord in lst)


def get_coords(coords: tuple[float, ...]) -> str:
    return f"X={coords[0]}, Y={coords[1]}, Z={coords[2]}"


def get_distance(
        coords1: tuple[float, ...], coords2: tuple[float, ...]) -> float:
    x1: float = coords1[0]
    y1: float = coords1[1]
    z1: float = coords1[2]
    x2: float = coords2[0]
    y2: float = coords2[1]
    z2: float = coords2[2]
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)


def main() -> None:
    center: tuple[float, float, float] = (0, 0, 0)
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    first: tuple[float, ...] = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: {get_coords(first)}")
    print(f"Distance to center: {get_distance(center, first)}")
    print()
    print("Get a second set of coordinates")
    second: tuple[float, ...] = get_player_pos()
    print(
          f"Distance between the 2 sets of coordinates: "
          f"{get_distance(second, first)}"
         )


if __name__ == "__main__":
    main()
