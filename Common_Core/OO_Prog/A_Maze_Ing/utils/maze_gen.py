import random
from enum import Enum


class Maze:
    def __init__(self, maze_size: tuple[int, int]):
        self.height: int = maze_size[0]
        self.width: int = maze_size[1]
        self.contain: list[list[int]] = [
            [15 for _ in range(maze_size[1])] for _ in range(maze_size[0])
        ]


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8


def tile_config(
    x: int,
    y: int,
    hist: dict[tuple[int, int], list[tuple[int, int] | None]],
    maze: Maze,
    visited: list[tuple[int, int]],
) -> int:
    # Parameters
    cont = maze.contain
    lim_w = maze.width - 1
    lim_h = maze.height - 1
    tile = 15
    directions = (
        x != 0 and (x, y) in hist.get((x - 1, y), []),  # Parent/Lien au NORD
        y != 0 and (x, y) in hist.get((x, y - 1), []),  # Parent/Lien à l'OUEST
        x != lim_h
        and (x, y) in hist.get((x + 1, y), []),  # Parent/Lien au SUD
        y != lim_w
        and (x, y) in hist.get((x, y + 1), []),  # Parent/Lien à l'EST
    )
    direction_config = {
        Direction.NORTH.value: (-1, 0, x > 0),
        Direction.SOUTH.value: (1, 0, x < lim_h),
        Direction.EAST.value: (0, 1, y < lim_w),
        Direction.WEST.value: (0, -1, y > 0),
    }
    # historic filling
    if (x, y) not in hist:
        hist[(x, y)] = []
    # tile config
    match (x, y):
        case (0, 0):
            # point of origin
            random_list = random.sample(
                [Direction.EAST.value, Direction.SOUTH.value],
                k=random.randint(1, 2),
            )
            tile = tile & ~sum(random_list)
        case _:
            # connection parents and saving previous path direction
            previous_dir = None
            match directions:
                case (n, w, s, e):
                    if n:
                        tile &= ~Direction.NORTH.value
                        previous_dir = Direction.SOUTH.value
                    if w:
                        tile &= ~Direction.WEST.value
                        previous_dir = Direction.EAST.value
                    if s:
                        tile &= ~Direction.SOUTH.value
                        previous_dir = Direction.NORTH.value
                    if e:
                        tile &= ~Direction.EAST.value
                        previous_dir = Direction.WEST.value

            # possible childrens
            valid_dirs: list[int] = []
            for d, (dx, dy, cond) in direction_config.items():
                nx, ny = dx + x, dy + y
                if cond and (nx, ny) not in visited and cont[nx][ny] != 16:
                    valid_dirs.append(d)
            # if children available
            if valid_dirs:
                # turn management
                turning = [d for d in valid_dirs if d != previous_dir]
                if turning and random.random() < random.uniform(0.4, 0.8):
                    # forced turns
                    random.shuffle(turning)
                    valid_dirs_ordonnes = turning
                else:
                    # turns are as likely as strait paths
                    random.shuffle(valid_dirs)
                    valid_dirs_ordonnes = valid_dirs

                # how many walls on that tile
                murs_restants = bin(tile).count("1")

                for d in valid_dirs_ordonnes:
                    # keep at least 1 wall
                    if murs_restants > 1:
                        tile &= ~d
                        murs_restants -= 1
                    else:
                        break

    for d, (dx, dy, cond) in direction_config.items():
        nx, ny = dx + x, dy + y
        if not (tile & d) and (nx, ny) not in visited:
            hist[(x, y)].append((nx, ny))
    return tile


def wall_destroyer(to_mod: list[tuple[int, int]], maze: Maze):
    cont = maze.contain
    border_x = maze.height - 1
    border_y = maze.width - 1

    voisins_opposes = {
        Direction.NORTH.value: (-1, 0, Direction.SOUTH.value),
        Direction.SOUTH.value: (1, 0, Direction.NORTH.value),
        Direction.EAST.value: (0, 1, Direction.WEST.value),
        Direction.WEST.value: (0, -1, Direction.EAST.value),
    }

    culs_de_sac = (7, 11, 13, 14)

    for tile in to_mod:
        x, y = tile

        if cont[x][y] == 0:
            continue

        perfect_choice = []
        obligatory_zero = []

        for d_val, (dx, dy, d_oppose) in voisins_opposes.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx <= border_x and 0 <= ny <= border_y:
                if cont[x][y] & d_val:
                    # central 42 is untouched
                    if cont[nx][ny] != 16:
                        futur_actuel = cont[x][y] & ~d_val
                        futur_voisin = cont[nx][ny] & ~d_oppose
                        # if a dead end -> become free space
                        if futur_actuel in culs_de_sac:
                            futur_actuel = 0
                        if futur_voisin in culs_de_sac:
                            futur_voisin = 0
                        # save classic tiles and free space separatelly
                        if futur_actuel == 0 or futur_voisin == 0:
                            obligatory_zero.append(
                                (
                                    d_val,
                                    nx,
                                    ny,
                                    d_oppose,
                                    futur_actuel,
                                    futur_voisin,
                                )
                            )
                        else:
                            perfect_choice.append(
                                (
                                    d_val,
                                    nx,
                                    ny,
                                    d_oppose,
                                    futur_actuel,
                                    futur_voisin,
                                )
                            )

        # if a perfect choice exist, use it, else 0
        if perfect_choice:
            chosen_dir, nx, ny, opposed_dir, f_actuel, f_voisin = (
                random.choice(perfect_choice)
            )
        elif obligatory_zero:
            chosen_dir, nx, ny, opposed_dir, f_actuel, f_voisin = (
                random.choice(obligatory_zero)
            )
        else:
            continue

        cont[x][y] = f_actuel
        cont[nx][ny] = f_voisin


def maze_generator(perfect_maze: bool, maze_size: tuple[int, int]) -> Maze:
    a_maze = Maze(maze_size)
    border_x = a_maze.height - 1
    border_y = a_maze.width - 1
    hist: dict[tuple[int, int], list[tuple[int, int] | None]] = {}
    visited = [(0, 0)]
    waiting_room: list[tuple[int, int]] = [(0, 0)]
    cx = (border_x + 1) // 2
    cy = (border_y + 1) // 2
    coord_cibles = {
        # 4
        (cx - 2, cy - 3),
        (cx - 1, cy - 3),
        (cx, cy - 3),
        (cx, cy - 2),
        (cx, cy - 1),
        (cx + 1, cy - 1),
        (cx + 2, cy - 1),
        # 2
        (cx - 2, cy + 1),
        (cx, cy + 1),
        (cx + 1, cy + 1),
        (cx + 2, cy + 1),
        (cx - 2, cy + 2),
        (cx, cy + 2),
        (cx + 2, cy + 2),
        (cx - 2, cy + 3),
        (cx, cy + 3),
        (cx + 2, cy + 3),
        (cx - 1, cy + 3),
    }
    forced_liberation = {
        (cx - 1, cy): [Direction.EAST.value, Direction.SOUTH.value],
        (cx - 1, cy + 1): [Direction.WEST.value, Direction.EAST.value],
        (cx - 1, cy + 2): [Direction.WEST.value],
        (cx + 1, cy + 2): [Direction.EAST.value],
        (cx + 1, cy + 3): [Direction.WEST.value, Direction.EAST.value],
        (cx + 1, cy + 4): [Direction.WEST.value],
    }
    conditional_liberation = {
        (cx, cy): [Direction.NORTH.value, Direction.SOUTH.value],
        (cx + 1, cy):[Direction.NORTH.value, Direction.SOUTH.value],
        (cx + 2, cy):[Direction.NORTH.value, Direction.SOUTH.value],
        (cx + 3, cy):[Direction.NORTH.value, Direction.SOUTH.value],
        (cx + 4, cy):[Direction.NORTH.value],
    }
    # 42 position
    for x in range(border_x + 1):
        for y in range(border_y + 1):
            if ((x, y) in coord_cibles) and (
                a_maze.height > 8 and a_maze.width > 9
            ):
                a_maze.contain[x][y] = 16
    while waiting_room:
        # choosing in the waiting room
        current = random.choice(waiting_room)
        waiting_room.remove(current)
        x, y = current
        a_maze.contain[x][y] = tile_config(x, y, hist, a_maze, visited)
        for child in hist[(x, y)]:
            if child is not None:
                waiting_room.append(child)
                visited.append(child)
    for x in range(border_x + 1):
        for y in range(border_y + 1):
            if a_maze.height > 8 and a_maze.width > 9:
                if (x, y) in forced_liberation:
                    for d in forced_liberation[(x, y)]:
                        a_maze.contain[x][y] &= ~d
    for coord, dir in conditional_liberation.items():
        x,y = coord
        if a_maze.height > 8 and a_maze.width > 9:
            if a_maze.contain[x][y] == 15:
                for d in dir:
                    a_maze.contain[x][y] &= ~d
            elif coord == (cx + 4, cy) and a_maze.contain[x - 1][y] == 15:
                a_maze.contain[x][y] &= ~dir[0]
    # if imperfect maze
    if not perfect_maze:
        tiles_to_modify = []
        # dead end extraction
        for x in range(border_x + 1):
            for y in range(border_y + 1):
                val = a_maze.contain[x][y]
                if val in (
                    7,
                    11,
                    13,
                    14,
                ):  # dead end values
                    tiles_to_modify.append((x, y))
        wall_destroyer(tiles_to_modify, a_maze)
    return a_maze
