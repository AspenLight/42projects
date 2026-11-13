*This activity has been created as part of the 42 curriculum by aspthiba, crouyrr*

## Description
The Pacman 42 project is a project dedicated to recreating a basic version of the game "Pac-Man" using python.

## Instructions
This project can be run using a makefile or found on Itch.io at (https://aspenlight.itch.io/42-pacman-project).

To run with makefile, run these commands in order:
`make env`
`source /mazeenv/bin/activate`
`make run`

## Resources
[Pyinstaller Manual](https://pyinstaller.org/en/stable/usage.html)
[pygame documentation](https://www.pygame.org/docs/)
AI as a debug tool.



## Configuration
The config file contains these variables and defaults:
- scores: contains a dictionary of high scores
- height-width: determines the height and width of the mazes for each level
- pac_gums: determines the number of pacgums spawned
- points_per_pacgum: determines the number of points each pacgum gives
- points_per_super_pacgum: determines the number of points each super pacgum gives
- points_per_ghost: determines the number of points given when a ghost is eaten
- level_max_time: determines the maximum time per level

## Highscore
High scores are stored in the config.json file as a dictionary with the screen name and final score. This was done for ease of use and ease of handling as the config.json file already contained our other permanent variables.

## Maze Generation
The maze generation for this project was implemented based on the previous group project, A_Maze_Ing, and is based on the system of arrays of `Node` classes as developed in the previous project. a maze is an array of Nodes, each Node containing various variables about the permanent and current state of the Node, such as open directions and what the Node contains (e.g. pacgums).

## Implementation
Game logic and graphical rendering is based off the original Pac-Man game.

Ghost pathfinding is based on optimistic as-the-crow-flies projections of their target, with multiple fallbacks for blocked routes, handling for dead-ends, collision between ghosts unless dead, and occasional random movement to lower difficulty and break any pathfinding loops the ghost may find itself in.

Ghosts target the player when alive and invulnerable, escape the player when vulnerable, and target their spawnpoint when dead.

All movements and data are robustly handled with error handling and validation.

## General Software Architecture

### Initialization

Extract game parameters from the config file.

Define sprites from spritesheet.

Load entities, maze and screens.

### Entities

Player

Ghosts

### Events

Handle pressed/held keys for movement and actions

Handle typed keys for name input

### Managers

State manager: handle various miscellaneous data that will be used in various part of the game, from score and maze parameters, to game states.

### Rendering

Main menu with scores and cheats.

Game screen with the game, score, life count, timer and level number.

Pause screen with return to game and return to main menu.

Game over screen with name input and return to main menu.

Win screen with name input and return to main menu.

### Maze

Mazegenerator given by the 42 curriculum.

## Project Management

Cyr was in charge of maze generation and game mechanics, while Aspen was in charge of pathfinding and packaging. This was determined so that the code could be cleanly split, worked on separately, and easily integrated. Bugfixing and integration was done by both teammates. Project coordination was done using Discord, Github, and SwissTransfer.
