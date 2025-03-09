import pygame

class Ghost:
    def __init__(self, pos, width, height, color):
        self.pos = pos #[x, y]
        self.width = width
        self.height = height
        self.color = color
        self.face_left = True
        self.moving = False
        self.appearance = None

    def move(self, dx, dy):
        if dx != 0:
            self.pos[0] += dx
            if dx > 0 and self.face_left:
                self.face_left = False
            elif dx < 0 and not self.face_left:
                self.face_left = True
        self.pos[1] += dy
        self.moving = not self.moving

    def display(self, screen):
        if self.appearance:
            screen.blit(self.appearance[self.face_left][self.moving], (self.pos[0], self.pos[1]))


class Blue(Ghost):
    def __init__(self, pos, width, height):
        super().__init__(pos, width, height, (0, 0, 255))
        self.appearance = [
            [pygame.transform.scale(pygame.image.load("blue1_flip.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("blue2_flip.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("blue1.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("blue2.png"), (self.width, self.height))]
        ]

class Red(Ghost):
    def __init__(self, pos, width, height):
        super().__init__(pos, width, height, (255, 0, 0))
        self.appearance = [
            [pygame.transform.scale(pygame.image.load("red1_flip.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("red2_flip.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("red1.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("red2.png"), (self.width, self.height))]
        ]

class Pink(Ghost):
    def __init__(self, pos, width, height):
        super().__init__(pos, width, height, (255, 105, 180))
        self.appearance = [
            [pygame.transform.scale(pygame.image.load("pink1_flip.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("pink2_flip.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("pink1.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("pink2.png"), (self.width, self.height))]
        ]


class Yellow(Ghost):
    def __init__(self, pos, width, height):
        super().__init__(pos, width, height, (255, 255, 0))
        self.appearance = [
            [pygame.transform.scale(pygame.image.load("yellow1_flip.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("yellow2_flip.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("yellow1.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("yellow2.png"), (self.width, self.height))]
        ]