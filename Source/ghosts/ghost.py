import pygame

class Ghost:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.face_left = True
        self.appearance = None

    def flip(self):
        if self.appearance:
            self.appearance = pygame.transform.flip(self.appearance, True, False)

    def move(self, dx, dy):
        if dx != 0:
            self.x += dx
            if dx > 0 and self.face_left:
                self.flip()
                self.face_left = False
            elif dx < 0 and not self.face_left:
                self.flip()
                self.face_left = True
        self.y += dy

    def display(self, screen):
        if self.appearance:
            screen.blit(self.appearance, (self.x, self.y))


class Blue(Ghost):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, (0, 0, 255))
        self.appearance = pygame.transform.scale(pygame.image.load("blue1.png"), (self.width, self.height))


class Red(Ghost):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, (255, 0, 0))
        self.appearance = pygame.transform.scale(pygame.image.load("red1.png"), (self.width, self.height))


class Pink(Ghost):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, (255, 105, 180))
        self.appearance = pygame.transform.scale(pygame.image.load("pink1.png"), (self.width, self.height))


class Yellow(Ghost):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, (255, 255, 0))
        self.appearance = pygame.transform.scale(pygame.image.load("yellow1.png"), (self.width, self.height))
