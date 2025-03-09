import pygame
import copy
from ghost_appearance import ghost_appearance_matrix

# Lớp cha Ghost
class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.face_left = True
        self.color = color
        self.apperance = copy.deepcopy(ghost_appearance_matrix)
    
    def flip(self):
        if not self.apperance:
            return

        self.face_left = not self.face_left
        size = len(self.apperance[0])        
        for i in range (size):
            for j in range (int(size/ 2)):
                self.apperance[i][j], self.apperance[i][size - j - 1] = self.apperance[i][size - j - 1], self.apperance[i][j]
                
    def move(self, dx, dy):
        if dx != 0:
            self.x += dx
            
            if (dx > 0):
                if (self.face_left):
                    self.flip()
            else:
                if (not self.face_left):
                    self.flip()
                    
        self.y += dy
        
    def move_left(self, d):
        self.x -= d
        if (not self.face_left):
            self.flip()
        
    def move_right(self, d):
        self.x += d
        if (self.face_left):
            self.flip()
        
    def move_up(self, d):
        self.y -= d
    def move_down(self, d):
        self.y += d
        
    def display(self, screen, pixel):
        for row_idx, row in enumerate(self.apperance):
            for col_idx, cell in enumerate(row):
                if cell == 1:
                    rect = pygame.Rect(self.x + col_idx * pixel, self.y + row_idx * pixel, pixel, pixel)
                    pygame.draw.rect(screen, self.color, rect)
        
class Blue(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, (0, 0, 255))
    
class Red(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, (255, 0, 0))
        
class Pink(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, (255, 105, 180))

class Yellow(Ghost):
    def __init__(self, x, y):
        super().__init__(x, y, (255, 255, 0))