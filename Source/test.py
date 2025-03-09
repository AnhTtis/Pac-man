from Maze import Maze
from Ghost import Ghost
from Maze import Maze
import time
from Ghost import Ghost, BlueGhost, OrangeGhost, PinkGhost
from GhostHandle import GameManager
from Pacman import Pacman
import copy
import threading

#lazymingg chao cau nheeeee <3

# maze_grid = [
#         [' ', ' ', ' ', '#', ' ', ' '],
#         [' ', '#', ' ', '#', ' ', '#'],
#         [' ', '#', ' ', ' ', ' ', 'P'],
#         [' ', ' ', '#', '#', '#', ' '],
#         [' ', ' ', ' ', ' ', ' ', ' ']
#     ]

# maze = Maze(maze_grid)
# # maze.load_pacman()
# # ghost = BlueGhost(maze, (3, 4))
# ghost = PinkGhost(maze, (5, 3))
# start_time = time.perf_counter()
# path = ghost.move((0, 0))
# end_time = time.perf_counter()
# print("Time: ", end_time - start_time)
# print(path)

maze_grid = [
        [' ', ' ', ' ', '#', ' ', ' '],
        [' ', '#', ' ', '#', ' ', '#'],
        [' ', '#', ' ', ' ', ' ', 'P'],
        [' ', ' ', '#', '#', '#', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ']
    ]
maze = Maze(maze_grid)
pacman = Pacman(maze, (2, 5))
ghosts = [BlueGhost(maze, (3, 4), "BlueGhost"), PinkGhost(maze, (5, 3), "PinkGhost")]
positions = {'BlueGhost': (3, 4), 'PinkGhost': (5, 3)}
game = GameManager(maze, (2, 5), ghosts, positions)
print(game.get_pacman_pos())