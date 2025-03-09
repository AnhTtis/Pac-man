import time
import threading
from Maze import Maze
from Source.Ghost import BlueGhost, PinkGhost
from GhostThread import GhostThread
from Pacman import Pacman
import copy

class GameManager:
    def __init__(self, maze, pacman_start, ghosts, positions):
        self.maze = copy.deepcopy(maze)
        self.pacman = Pacman(maze, pacman_start)
        self.ghosts = copy.deepcopy(ghosts)
        self.positions = positions
        self.lock = threading.Lock()
        self.running = threading.Event()
        self.running.set()
        self.threads = [GhostThread(ghost, self.pacman, self.lock, self.running, self.positions) for ghost in ghosts]
        for t in self.threads: t.start()

    def is_running(self): return self.running.is_set()
    def get_pacman_pos(self): return self.pacman.pos


    def move_pacman(self, direction): self.pacman.move(direction)
    def stop(self):
        self.running.clear()
        for t in self.threads: t.join()