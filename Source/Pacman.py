from maze import Maze
import threading

class Pacman:
    def __init__(self, maze, pos):
        self.pos = pos #tuple of (x, y)
        self.score = 0 #score of pacman
        self.maze = maze #maze class
        #avoid many ghost threads to access the same time
        self.lock = threading.Lock()

    def move(self, direction):
        if direction == "up" and not self.maze.is_wall((self.pos[0] - 1, self.pos[1])):
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif direction == "down" and not self.maze.is_wall((self.pos[0] + 1, self.pos[1])):
            self.pos = (self.pos[0] + 1, self.pos[1])
        elif direction == "left" and not self.maze.is_wall((self.pos[0], self.pos[1] - 1)):
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif direction == "right" and not self.maze.is_wall((self.pos[0], self.pos[1] + 1)):
            self.pos = (self.pos[0], self.pos[1] + 1)
        if self.maze.is_dot(self.pos):
            self.score += 1
        elif self.maze.is_big_dot(self.pos):
            self.score += 5
        return self.pos
    
    def __str__(self):
        return f"Pacman: x={self.x}, y={self.y}, score={self.score}"
    
    
    