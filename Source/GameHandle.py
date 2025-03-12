import time
import threading
from maze import Maze
from ghosts.ghost import Ghost, BlueGhost, OrangeGhost, PinkGhost, RedGhost
from GhostThread import GhostThread
from pacman.pacman import Pacman
import pygame
import copy

class GameManager:
    def __init__(self, maze, pacman_start, ghosts, positions, cell_size):
        self.cell_size = cell_size
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

    def draw(self, pygame, screen):

        #draw the Board
        rows = self.maze.get_rows()
        cols = self.maze.get_cols()

        for y in range(rows):
            for x in range(cols):
                pos = (x, y)
                if self.maze.is_wall(pos):
                    pygame.draw.rect(screen, (0, 0, 255), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                elif self.maze.is_dot(pos):
                    pygame.draw.circle(screen, (255, 255, 255), (int(x * self.cell_size + self.cell_size / 2), int(y * self.cell_size + self.cell_size / 2)), 3)
                elif self.maze.is_big_dot(pos):
                    pygame.draw.circle(screen, (255, 255, 255), (int(x * self.cell_size + self.cell_size / 2), int(y * self.cell_size + self.cell_size / 2)), 5)
                elif self.maze.is_gate(pos):
                    pygame.draw.rect(screen, (255, 255, 255), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                elif self.maze.is_pacman(pos):
                    pygame.draw.circle(screen, (255, 255, 0), (int(x * self.cell_size + self.cell_size / 2), int(y * self.cell_size + self.cell_size / 2)), 10)

    def move_pacman(self, direction): self.pacman.move(direction)
    def stop(self):
        self.running.clear()
        for t in self.threads: t.join()
    
