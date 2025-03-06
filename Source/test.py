from maze import Maze
from Ghost import Ghost
from Ghost import BlueGhost

board = [
    "######",
    "#P   #",
    "# #  #",
    "#  # #",
    "#   G#",
    "######"
]

maze = Maze(board)
# maze.load_pacman()
ghost = BlueGhost(maze, (4, 4))
print(ghost.move((1, 1)))  # (4, 3)