from maze import Maze
from typing import List, Tuple
import threading
from pygame import transform, image
from enum import Enum

class PacmanState(Enum):
    CLOSE   = 0
    UP      = 1
    DOWN    = 2
    LEFT    = 3
    RIGHT   = 4

class Pacman:
    def __init__(self, maze, pos: List[int], size: Tuple[int, int]):
        self.pos = pos #Array of ơx, y)
        self.size = size
        self.score = 0 #score of pacman
        self.maze = maze #maze class
        #avoid many ghost threads to access the same time
        self.lock = threading.Lock()
        self.appearance = [
            transform.scale(image.load("pacman/pacman_close_mouth.png"), self.size),
            transform.scale(image.load("pacman/pacman_open_mouth_top.png"), self.size),
            transform.scale(image.load("pacman/pacman_open_mouth_bot.png"), self.size),
            transform.scale(image.load("pacman/pacman_open_mouth_left.png"), self.size),
            transform.scale(image.load("pacman/pacman_open_mouth_right.png"), self.size)
        ]
        self.direction = PacmanState.CLOSE
        
    def set_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == PacmanState.UP and not self.maze.is_wall((self.pos[0], self.pos[1] - 1)):
            self.maze.set_grid(self.pos[1], self.pos[0], 0)
            self.pos[1] -= 1
        elif self.direction == PacmanState.DOWN and not self.maze.is_wall((self.pos[0], self.pos[1] + 1)):
            self.maze.set_grid(self.pos[1], self.pos[0], 0)
            self.pos[1] += 1
        elif self.direction == PacmanState.LEFT and not self.maze.is_wall((self.pos[0] - 1, self.pos[1])):
            self.maze.set_grid(self.pos[1], self.pos[0], 0)
            self.pos[0] -= 1
        elif self.direction == PacmanState.RIGHT and not self.maze.is_wall((self.pos[0] + 1, self.pos[1])):
            self.maze.set_grid(self.pos[1], self.pos[0], 0)
            self.pos[0] += 1
        if self.maze.is_dot(self.pos):
            self.score += 1
        elif self.maze.is_big_dot(self.pos):
            self.score += 5
        return self.pos
        
    def display(self, screen):
        screen.blit(self.appearance[self.direction.value], (self.pos[0], self.pos[1]))

    def __str__(self):
        return f"Pacman: x={self.pos[0]}, y={self.pos[1]}, score={self.score}"
    
    
    