import pygame
from typing import List, Tuple, Dict, Set, Optional
from maze import Maze

class Ghost:
    def __init__(self, name, maze: 'Maze', pos: List[int, int], size: Tuple[int, int], color):
        self.name = name
        self.maze = maze

        self.pos = pos #[x, y]
        self.sie = size
        
        self.color = color
        self.face_right = False
        self.moving = False
        self.appearance = None

    def move(self, dx, dy):
        if dx != 0:
            self.pos[0] += dx
            if dx < 0 and self.face_right:
                self.face_right = False
            elif dx > 0 and not self.face_right:
                self.face_right = True
        self.pos[1] += dy
        self.moving = not self.moving

    def display(self, screen):
        if self.appearance:
            screen.blit(self.appearance[self.face_right], self.pos)


class Blue(Ghost):
    def __init__(self, pos, width, height):
        super().__init__(pos, width, height, (0, 0, 255))
        self.appearance = [pygame.transform.scale(pygame.image.load("blue1.png"), (20,20))]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))

class Red(Ghost):
    def __init__(self, pos, width, height):
        super().__init__(pos, width, height, (255, 0, 0))
        self.appearance = [pygame.transform.scale(pygame.image.load("red1.png"), (20,20))]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))


class Pink(Ghost):
    def __init__(self, pos, width, height):
        super().__init__(pos, width, height, (255, 105, 180))
        self.appearance = [pygame.transform.scale(pygame.image.load("pink1.png"), (20,20))]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))



class Orange(Ghost):
    def __init__(self, pos, width, height):
        super().__init__(pos, width, height, (255, 255, 0))
        self.appearance = [pygame.transform.scale(pygame.image.load("yellow1.png"), (20,20))]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))
