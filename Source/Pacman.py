from maze import Maze
import threading

class Pacman:
    def __init__(self, maze, pos, width, height):
        self.width = width
        self.height = height
        self.pos = pos #tuple of (x, y)
        self.score = 0 #score of pacman
        self.maze = maze #maze class
        #avoid many ghost threads to access the same time
        self.lock = threading.Lock()
        self.appearance = None
        self.direction = "None"
        
    def set_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == "up" and not self.maze.is_wall((self.pos[0], self.pos[1] - 1)):
            self.maze.set_grid(self.pos[1], self.pos[0], 0)
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif self.direction == "down" and not self.maze.is_wall((self.pos[0], self.pos[1] + 1)):
            self.maze.set_grid(self.pos[1], self.pos[0], 0)
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif self.direction == "left" and not self.maze.is_wall((self.pos[0] - 1, self.pos[1])):
            self.maze.set_grid(self.pos[1], self.pos[0], 0)
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif self.direction == "right" and not self.maze.is_wall((self.pos[0] + 1, self.pos[1])):
            self.maze.set_grid(self.pos[1], self.pos[0], 0)
            self.pos = (self.pos[0] + 1, self.pos[1])
        if self.maze.is_dot(self.pos):
            self.score += 1
        elif self.maze.is_big_dot(self.pos):
            self.score += 5
        return self.pos
    
    def load_image(self, pygame):
        self.appearance = [
            [pygame.transform.scale(pygame.image.load("Source/pacman/pacman_close_mouth.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("Source/pacman/pacman_close_mouth.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("Source/pacman/pacman_open_mouth_bot.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("Source/pacman/pacman_open_mouth_bot.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("Source/pacman/pacman_open_mouth_left.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("Source/pacman/pacman_open_mouth_left.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("Source/pacman/pacman_open_mouth_right.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("Source/pacman/pacman_open_mouth_right.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("Source/pacman/pacman_open_mouth_top.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("Source/pacman/pacman_open_mouth_top.png"), (self.width, self.height))]
        ]
        
    def display(self, screen, cell_size):
        x, y = self.pos
        if self.direction == "up":
            screen.blit(self.appearance[4][0], (x * cell_size, y * cell_size))
        elif self.direction == "down":
            screen.blit(self.appearance[1][0], (x * cell_size, y * cell_size))
        elif self.direction == "left":
            screen.blit(self.appearance[2][0], (x * cell_size, y * cell_size))
        elif self.direction == "right":
            screen.blit(self.appearance[3][0], (x * cell_size, y * cell_size))
        else:
            screen.blit(self.appearance[0][0], (x * cell_size, y * cell_size))

    def __str__(self):
        return f"Pacman: x={self.x}, y={self.y}, score={self.score}"
    
    
    