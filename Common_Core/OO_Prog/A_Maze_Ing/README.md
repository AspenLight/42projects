*This activity has been created as part of the 42 curriculum by aspthiba, crouyrr*

## Description
A_Maze_Ing is a program designed to generate and solve randomized mazes of arbitrary size when provided with certain variables. The variables are:
- `WIDTH`: Integer value, determines the width of the generated maze.
- `HEIGHT`: Integer value, determines the height of the generated maze.
- `ENTRY`: Tuple of integers, determines the starting position for the shortest path search algorithm.
- `EXIT`: Tuple of integers, determines the ending position for the shortest path search algorithm.
- `OUTPUT_FILE`: String, contains the filename of the file to output the results to.
- `PERFECT`: Boolean, False by default, determines how a maze is generated. False for Pacman-like open ended maze, True for a classic one-true-path maze
- `SEED`: Integer, allows the reproduction of an exact maze by using the same seed.

The program will generate a randomized map using the provided parameters, run a shortest path search algorithm to find the path between `ENTRY` and `EXIT`, display the map graphically, then output the map as a block of hexadecimal text with a string of letters underneath representing the cardinal directions taken by the discovered shortest path (eg. NEESESWSS)

When generating the maze, the program first checks if the maze is of size 8x9 or larger. If so, the central nodes in the shape of a '42' are blocked out. The program then mozes to node (0,0), where it unblocks the directions of south, east, or both. The program then goes across each opened node, checking to see if any nodes have already been opened for different paths to avoid connecting to them, then randomly opens some or all of the available directions. This continues for every node until a full maze has been generated. If `PERFECT` is false (Pac-man), the maze finds every cul-de-sac and forms one additional connection (while avoiding the central 42) to eliminate dead ends.

The shortest path algorithm functions based on a modified Dijkstra algorithm for equal-distance nodes. The program first runs a Breadth first search, updating the distance of each found node to be one more than the distance of the adjacent node with the smallest distance. The search algorithm works by scanning around the current node based on whichever directions are open to it. If it finds an adjacent node that is not yet on the node checklist, it adds that node to the checklist, then continues checking. The program then moves to the next available node on the checklist until the `EXIT` position is found or the checklist is empty. If the `EXIT` node is found, the program then moves on to the peth reconstruction step. The path reconstruction algorithm starts from the `EXIT` node and searches all accessible adjacent nodes for the node with the smallest distance. The algorithm then moves to this node and repeats the search, hopping to nodes of smaller and smaller distance until the `ENTRY` node is reached. During this process, the inverse of each move is being stored at the start of a string `result`, thus reconstructing the proper path to follow to reach `EXIT` from `ENTRY`. Finally, the program returns this string to be read for display and added to the output file.

Once the program has all the required data for the math and the path, it uses `minilibx-python` and `python-xlib` to generate a graphical interface of the maze.

## Instructions
To initialize the environment, use `make env`
Once the environment is initialized, use `make run` to run the project.
To create the compressed file, use `make build`
To clean the space of files and data produced by running the program, use `make clean`
To check for mypy or flake8 errors, use `make lint-lint-strict`

## Resources
[This Manual](https://github.com/noradefitero/42_MiniLibX_Python_Manual) for minilibx-python 

[This Manual](https://pypi.org/project/python-xlib/) for python-xlib

[This Article](https://www.geeksforgeeks.org/python/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/) was useful in reaching an understanding of how a Dijkstra algorithm functions.

AI was used to simplify and clean parts of the maze generation and display code.

## Project Management
Cyr was in charge of Maze Generation, Aspen was in charge of Maze Solving 
Our planning revolved around each of us writing our code as best we could, then integrating each others' code outputs to function together. Aspen wrote a function to convert the Maze type of `list[list[int]]` to `list[list[Node]]`, where Node is a custom class containing variables with necessary details, such as open directions and distance, while Cyr wrote their code to take the returned string of letters from Aspen's code and parse it for display.
Some more communication during the code writing process may have helped somewhat but overall the code integration went rather smoothly, and having 2 blocks of clear code allowed for minimal confusion when integrating, rather than attempting to code every part together.
Most tools used were the simple tools used in every project, Git and a code editor. SwissTransfer was also used to transfer the project when working at home.
