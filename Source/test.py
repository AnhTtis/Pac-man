from maze import Maze
from Ghost import Ghost
from Ghost import BlueGhost

#lazymingg chao cau nheeeee <3

maze_grid = [
        [' ', ' ', ' ', '#', ' ', ' '],
        [' ', '#', ' ', '#', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', 'P'],
        [' ', ' ', '#', '#', '#', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ']
    ]

maze = Maze(maze_grid)
# maze.load_pacman()
ghost = BlueGhost(maze, (5, 2))
path = ghost.move((1, 4))
print(path)