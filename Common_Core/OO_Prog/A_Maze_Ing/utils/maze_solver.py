import numpy as np


class Node:
    def __init__(self):
        self.xy: tuple[int, int]
        self.n: bool
        self.e: bool
        self.s: bool
        self.w: bool
        self.dist: int = -1

    def set_xy(self, x: int, y:int):
        self.xy = tuple(x, y)

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
