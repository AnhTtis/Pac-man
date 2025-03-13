import pygame
from typing import List, Tuple, Dict, Set, Optional
from maze import Maze
import copy

class Ghost:
    def __init__(self, name: str, maze: Maze, pos: List[int], size: Tuple[int, int], color):
        self.name = name
        self.maze = maze
        self.pos = pos #[x, y]
        self.size = size
        
        self.color = color
        self.face_right = False
        self.moving = False
        self.appearance = None

    def move(self, dx, dy, screen_width, screen_height):
        if (dx == dy == 0):
            return
        
        newPos = [self.pos[0] + dx, self.pos[1] + dy]
        if (newPos[0] < 0 or newPos[0] > screen_width or
            newPos[1] < 0 or newPos[1] > screen_height):
                return
        
        self.pos = newPos

        if dx != 0:
            if dx < 0 and self.face_right:
                self.face_right = False
            elif dx > 0 and not self.face_right:
                self.face_right = True
        self.moving = not self.moving

    def display(self, screen):
        if self.appearance:
            screen.blit(self.appearance[self.face_right], self.pos)

class BlueGhost(Ghost):
    def __init__(self, name: str, maze: Maze, pos: List[int], size: Tuple[int, int]):
        super().__init__(name, maze, pos, size, (0, 0, 255))
        self.appearance = [pygame.transform.scale(pygame.image.load("blue.png"), self.size)]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))

class RedGhost(Ghost):
    def __init__(self, name: str, maze: Maze, pos: List[int], size: Tuple[int, int]):
        super().__init__(name, maze, pos, size, (255, 0, 0))
        self.appearance = [pygame.transform.scale(pygame.image.load("red.png"), self.size)]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))

class PinkGhost(Ghost):
    def __init__(self, name: str, maze: Maze, pos: List[int], size: Tuple[int, int]):
        super().__init__(name, maze, pos, size, (255, 105, 180))
        self.appearance = [pygame.transform.scale(pygame.image.load("pink.png"), self.size)]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))

class OrangeGhost(Ghost):
    def __init__(self, name: str, maze: Maze, pos: List[int], size: Tuple[int, int]):
        super().__init__(name, maze, pos, size, (255, 255, 0))
        self.appearance = [pygame.transform.scale(pygame.image.load("yellow.png"), self.size)]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))
