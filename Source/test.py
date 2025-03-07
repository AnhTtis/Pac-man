from maze import Maze
from Ghost import Ghost
import time
from Ghost import BlueGhost
from Ghost import OrangeGhost

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
# ghost = BlueGhost(maze, (3, 4))
ghost = OrangeGhost(maze, (5, 3))
start_time = time.perf_counter()
path = ghost.move((0, 0))
end_time = time.perf_counter()
print("Time: ", end_time - start_time)
print(path)