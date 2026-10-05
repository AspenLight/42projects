class Node:
    def __init__(self) -> None:
        self.xy: tuple[int, int]
        self.n: bool = False
        self.e: bool = False
        self.s: bool = False
        self.w: bool = False
        self.dist: int = -1

    def set_dir(self, node: int) -> None:
        if node & 1 == 0:
            self.n = True
        if node & 2 == 0:
            self.e = True
        if node & 4 == 0:
            self.s = True
        if node & 8 == 0:
            self.w = True

    def update_dist(self, d: int) -> None:
        if self.dist < 0 or d < self.dist:
            self.dist = d + 1

    def display_data(self) -> None:
        print(f"xy: {self.xy}")
        print(f"N: {self.n}")
        print(f"E: {self.e}")
        print(f"S: {self.s}")
        print(f"W: {self.w}")
        print(f"Dist: {self.dist}")


def maze_convert(
    maze: list[list[int]], nodemaze: list[list[Node]]
) -> list[list[Node]]:
    x = 0
    y = 0
    for lst in maze:
        for _ in lst:
            nodemaze[y][x].xy = (x, y)
            if maze[y][x] == 16:
                nodemaze[y][x].set_dir(15)
            else:
                nodemaze[y][x].set_dir(maze[y][x])
            x = x + 1
        x = 0
        y = y + 1
    # for row in nodemaze:
    #     for j in range(len(row)):
    #         print(row[j].n,row[j].s,row[j].e,row[j].w)
    return nodemaze


def path_reconstruct(
    nodemaze: list[list[Node]], exit: tuple[int, int], entry: tuple[int, int]
) -> str:
    x = exit[0]
    y = exit[1]
    dist: int = nodemaze[y][x].dist
    path: list[int] = []
    result: str = ""
    dir: int = 0
    while x is not entry[0] or y is not entry[1]:
        if nodemaze[y][x].n is True:
            if nodemaze[y - 1][x].dist != -1:
                dist = nodemaze[y - 1][x].dist
                dir = 1
        if nodemaze[y][x].e is True:
            if nodemaze[y][x + 1].dist != -1:
                if dist > nodemaze[y][x + 1].dist:
                    dist = nodemaze[y][x + 1].dist
                    dir = 2
        if nodemaze[y][x].s is True:
            if nodemaze[y + 1][x].dist != -1:
                if dist > nodemaze[y + 1][x].dist:
                    dist = nodemaze[y + 1][x].dist
                    dir = 3
        if nodemaze[y][x].w is True:
            if nodemaze[y][x - 1].dist != -1:
                if dist > nodemaze[y][x - 1].dist:
                    dist = nodemaze[y][x - 1].dist
                    dir = 4
        path.append(dir)
        if dir == 1:
            y = y - 1
        if dir == 2:
            x = x + 1
        if dir == 3:
            y = y + 1
        if dir == 4:
            x = x - 1
        if dir == 0:
            break
        dist = nodemaze[y][x].dist
    for node in path:
        if node == 1:
            result = "S" + result
        if node == 2:
            result = "W" + result
        if node == 3:
            result = "N" + result
        if node == 4:
            result = "E" + result
    return result


def maze_solver(
    entry: tuple[int, int], exit: tuple[int, int], maze: list[list[int]]
) -> str:
    checklist: list[tuple[int, int]] = []
    checked: list[tuple[int, int]] = []
    found_exit: bool = False
    sizey: int = len(maze)
    sizex: int = len(maze[0])
    nodemaze = [[Node() for i in range(sizex)] for j in range(sizey)]
    print("\tstep 1..")
    maze_convert(maze, nodemaze)
    checklist.append(entry)
    nodemaze[entry[1]][entry[0]].dist = 0
    print("\tstep 2..")
    for x, y in checklist:
        print(f"\r\tdest= ({exit[1]},{exit[0]}) pos=({y},{x})", flush=True)
        print(f"\r\tdist={nodemaze[y][x].dist}", flush=True)
        print(f"\r\tchecked={len(checked)+1}", flush=True)
        print(f"\r\tqueued={len(checklist)}", flush=True)
        print(f"\r\tremaining={len(checklist)-len(checked)-1}", flush=True)
        checked.append((x, y))
        if nodemaze[y][x].n is True:
            if (x, y - 1) in checked:
                nodemaze[y][x].update_dist(nodemaze[y - 1][x].dist)
            else:
                checklist.append((x, y - 1))
        if nodemaze[y][x].e is True:
            if (x + 1, y) in checked:
                nodemaze[y][x].update_dist(nodemaze[y][x + 1].dist)
            else:
                checklist.append((x + 1, y))
        if nodemaze[y][x].s is True:
            if (x, y + 1) in checked:
                nodemaze[y][x].update_dist(nodemaze[y + 1][x].dist)
            else:
                checklist.append((x, y + 1))
        if nodemaze[y][x].w is True:
            if (x - 1, y) in checked:
                nodemaze[y][x].update_dist(nodemaze[y][x - 1].dist)
            else:
                checklist.append((x - 1, y))
        if y == exit[1] and x == exit[0]:
            found_exit = True
            break
        else:
            print("\033[5A", end="", flush=True)
    print("\n\tstep 3..")
    if found_exit is False:
        return "Path not found"
    else:
        return path_reconstruct(nodemaze, exit, entry)
