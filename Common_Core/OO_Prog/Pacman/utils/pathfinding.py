from .consts import Node
# integration: run on each ghost

# secondary_target takes the player position, the ghost position, and the direction priority
# it returns a direction string for the ghost's next movement
def secondary_target(player_pos: tuple[int, int], ghost_pos: tuple[int, int], priority: str) -> str:
    if priority == "EW":
        dir = player_pos[0] - ghost_pos[0]
        if dir > 0:
            direction = "E"
        elif dir < 0:
            direction = "W"
    elif priority == "NS":
        dir = player_pos[1] - ghost_pos[1]
        if dir > 0:
            direction = "S"
        elif dir < 0:
            direction = "N"
    return direction

# intersect_move takes a list of available directions, the player position, and the ghost position
# it returns a tuple coordinate of where the ghost should move
def intersect_move(dirs: list[str], player_pos: tuple[int, int], ghost_pos: tuple[int, int]) -> tuple[int, int] | None:
    dir_NS = player_pos[1] - ghost_pos[1]
    dir_EW = player_pos[0] - ghost_pos[0]
    if dir_NS == 0 and dir_EW == 0:
        return
    if len(dirs) != 3:
        return
    priority = "NS"
    direction = "N"

    if abs(dir_NS) < abs(dir_EW):
        priority = "EW"
        direction = "E"

    if priority == "NS":
        if dir_NS > 0:
            direction = "S"
        if dir_NS < 0:
            direction = "N"
        if dir_NS == 0:
            priority = "EW"
    if priority == "EW":
        if dir_EW > 0:
            direction = "E"
        if dir_EW < 0:
            direction = "W"
        if dir_EW == 0:
            priority = "NS"
    if priority == "NS" and direction == ("E" | "W"):
        if dir_NS > 0:
            direction = "S"
        if dir_NS < 0:
            direction = "N"

    if direction == "N" and direction in dirs:
        return (ghost_pos[0], ghost_pos[1] - 1)
    if direction == "S" and direction in dirs:
        return (ghost_pos[0], ghost_pos[1] + 1)
    if direction == "E" and direction in dirs:
        return (ghost_pos[0] + 1, ghost_pos[1])
    if direction == "W" and direction in dirs:
        return (ghost_pos[0] - 1, ghost_pos[1])
    if priority == "NS":
        priority = "EW"
    elif priority == "EW":
        priority = "NS"
    direction = secondary_target(player_pos, ghost_pos, priority)
    if direction == "N" and direction in dirs:
        return (ghost_pos[0], ghost_pos[1] - 1)
    if direction == "S" and direction in dirs:
        return (ghost_pos[0], ghost_pos[1] + 1)
    if direction == "E" and direction in dirs:
        return (ghost_pos[0] + 1, ghost_pos[1])
    if direction == "W" and direction in dirs:
        return (ghost_pos[0] - 1, ghost_pos[1])

# hallway_move takes a list of available directions, the player position, and the ghost position
# it returns a tuple coordinate of where the ghost should move
def hallway_move(dirs: list[str], player_pos: tuple[int, int], ghost_pos: tuple[int, int]) -> tuple[int, int] | None:
    dir_NS = player_pos[1] - ghost_pos[1]
    dir_EW = player_pos[0] - ghost_pos[0]
    if dir_EW == 0 and dir_NS == 0:
        return

    if "N" in dirs and "S" in dirs:
        if dir_NS > 0:
            return (ghost_pos[0], ghost_pos[1] - 1)
        elif dir_NS < 0:
            return (ghost_pos[0], ghost_pos[1] + 1)
        else:
            return (ghost_pos[0], ghost_pos[1] - 1)
    elif "E" in dirs and "W" in dirs:
        if dir_EW > 0:
            return (ghost_pos[0] - 1, ghost_pos[1])
        elif dir_EW < 0:
            return (ghost_pos[0] + 1, ghost_pos[1])
        else:
            return (ghost_pos[0] - 1, ghost_pos[1])
    else:
        if (abs(dir_NS) > abs(dir_EW)) and dir_NS != 0:
            if dir_NS > 0 and "N" in dirs:
                return (ghost_pos[0], ghost_pos[1] - 1)
            elif dir_NS < 0 and "S" in dirs:
                return (ghost_pos[0], ghost_pos[1] + 1)
        if abs(dir_NS) < abs(dir_EW) and dir_EW != 0:
            if dir_EW > 0 and "E" in dirs:
                return (ghost_pos[0] + 1, ghost_pos[1])
            if dir_EW < 0 and "W" in dirs:
                return (ghost_pos[0] - 1, ghost_pos[1])
        if dir_NS == 0 and ("E" | "W") in dirs:
            if dir_EW > 0 and "E" in dirs:
                return (ghost_pos[0] + 1, ghost_pos[1])
            elif dir_EW < 0 and "W" in dirs:
                return (ghost_pos[0] - 1, ghost_pos[1])
            else:
                if "E" in dirs:
                    return (ghost_pos[0] + 1, ghost_pos[1])
                if "W" in dirs:
                    return (ghost_pos[0] - 1, ghost_pos[1])
        if dir_EW == 0 and ("N" | "S") in dirs:
            if dir_NS > 0 and "N" in dirs:
                return (ghost_pos[0], ghost_pos[1] - 1)
            elif dir_NS < 0 and "S" in dirs:
                return (ghost_pos[0], ghost_pos[1] + 1)
            else:
                if "N" in dirs:
                    return (ghost_pos[0], ghost_pos[1] - 1)
                if "S" in dirs:
                    return (ghost_pos[0], ghost_pos[1] + 1)

# free_move takes the player position and the ghost position
# and returns the coordinate of where the ghost should go next
def free_move(player_pos: tuple[int, int], ghost_pos: tuple[int, int]) -> tuple[int, int] | None:
    dir_NS = player_pos[1] - ghost_pos[1]
    dir_EW = player_pos[0] - ghost_pos[0]
    if dir_NS == 0 and dir_EW == 0:
        return

    if abs(dir_NS) > abs(dir_EW) and dir_NS != 0:
        if dir_NS > 0:
            return (ghost_pos[0], ghost_pos[1] - 1)
        if dir_NS < 0:
            return (ghost_pos[0], ghost_pos[1] + 1)
    if abs(dir_NS) < abs(dir_EW) and dir_EW != 0:
        if dir_EW > 0:
            return (ghost_pos[0] + 1, ghost_pos[1])
        if dir_EW < 0:
            return (ghost_pos[0] - 1, ghost_pos[1])
    if dir_NS > 0:
        return (ghost_pos[0], ghost_pos[1] - 1)
    if dir_NS < 0:
        return (ghost_pos[0], ghost_pos[1] + 1)

# pathfind takes the node the ghost is on, the player position, and the ghost position
# and returns the new position the ghost should be at. 
def pathfind(node: Node, player_pos: tuple[int, int], ghost_pos: tuple[int, int]) -> tuple[int, int] | None:
    dirs: list[str]
    newpos: tuple[int, int]

    if node.n == True:
        dirs.append("N")
    if node.e == True:
        dirs.append("E")
    if node.s == True:
        dirs.append("S")
    if node.w == True:
        dirs.append("W")

    if len(dirs) == 2:
        newpos = hallway_move(dirs, player_pos, ghost_pos)
        return newpos
    if len(dirs) == 3:
        newpos = intersect_move(dirs, player_pos, ghost_pos)
        return newpos
    if len(dirs) == 4:
        newpos = free_move(player_pos, ghost_pos)
    else:
        return
