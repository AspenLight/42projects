import numpy as np


class Node:
    def __init__(self):
        self.xy: tuple[int, int]
        self.n: bool = False
        self.e: bool = False
        self.s: bool = False
        self.w: bool = False
        self.dist: int = -1

    def set_dir(self, node: int):
        if node & 8:
            self.n = True
        if node & 4:
            self.e = True
        if node & 2:
            self.s = True
        if node & 1:
            self.w = True

    def update_dist(self, d: int):
        if self.dist < 0 or d < self.dist:
            self.dist = d


def maze_convert(maze: list[list[int]], nodemaze: list[list[Node]]) -> list[list[Node]]:
    x = 0
    y = 0
    for lst in maze:
        for element in lst:
            nodemaze[y][x].xy = (x, y)
            nodemaze[y][x].set_dir(maze[y][x])
            x = x + 1
        x = 0
        y = y + 1
    return nodemaze


def path_reconstruct(nodemaze: list[list[Node]], exit: tuple[int, int], entry: tuple[int, int]) -> str:
    x = exit[1]
    y = exit[0]
    dists: list[int]
    path: list[int]
    result: str
    dir: int = 0
    while x != entry[1] and y != entry[0]:
        if nodemaze[y][x].n == True:
            dists.append(nodemaze[y - 1][x].dist)
            dir = 1
        if nodemaze[y][x].e == True:
            if dists[0] > nodemaze[y][x + 1].dist:
                dists.pop(0)
                dists.append(nodemaze[y][x + 1].dist)
                dir = 2
        if nodemaze[y][x].s == True:
            if dists[0] > nodemaze[y + 1][x].dist:
                dists.pop(0)
                dists.append(nodemaze[y + 1][x].dist)
                dir = 3
        if nodemaze[y][x].w == True:
            if dists[0] > nodemaze[y][x - 1].dist:
                dists.pop(0)
                dists.append(nodemaze[y][x - 1].dist)
                dir = 4
        dists.pop(0)
        path.insert(0, dir)
        if dir == 1:
            y = y - 1
        if dir == 2:
            x= x + 1
        if dir == 3:
            y = y + 1
        if dir == 4:
            y = x - 1
    for node in path:
        if node == 1:
            result = result + "S"
        if node == 2:
            result = result + "W"
        if node == 3:
            result = result + "N"
        if node == 4:
            result = result + "E"
    return result



def maze_solver(entry: tuple[int, int], exit: tuple[int, int], maze: list[list[int]]) -> str:
    checklist: list[tuple[int, int]]
    checked: list[tuple[int, int]]
    found_exit: bool = False
    path: str
    sizey: int = len(maze)
    sizex: int = len(maze[0])
    nodemaze = np.empty((sizex, sizey), dtype=Node)
    maze_convert(maze, nodemaze)
    checklist.append(entry)
    nodemaze[entry[0]][entry[1]].dist = 0
    for x, y in checklist and found_exit is not True:
        if y == exit[0] and x == exit[1]:
            found_exit = True
            return
        if nodemaze[y][x].n == True:
            if (y - 1, x) in checked:
                nodemaze[y][x].update_dist(nodemaze[y - 1][x].dist)
            else:
                checklist.append((y - 1, x))
            checked.append((y, x))
            checklist.pop(0)
        if nodemaze[y][x].e == True:
            if (y, x + 1) in checked:
                nodemaze[y][x].update_dist(nodemaze[y][x + 1].dist)
            else:
                checklist.append((y - 1, x))
            checked.append((y, x))
            checklist.pop(0)
        if nodemaze[y][x].s == True:
            if (y + 1, x) in checked:
                nodemaze[y][x].update_dist(nodemaze[y + 1][x].dist)
            else:
                checklist.append((y - 1, x))
            checked.append((y, x))
            checklist.pop(0)
        if nodemaze[y][x].w == True:
            if (y, x - 1) in checked:
                nodemaze[y][x].update_dist(nodemaze[y][x - 1].dist)
            else:
                checklist.append((y - 1, x))
            checked.append((y, x))
            checklist.pop(0)
    if found_exit is False:
        return "Path not found"
    else:
        return path_reconstruct(nodemaze, exit, entry)
