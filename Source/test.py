from maze import Maze
from Ghost import Ghost
import time
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
start_time = time.perf_counter()
path = ghost.move((0, 0))
end_time = time.perf_counter()
print("Time: ", end_time - start_time)
print(path)