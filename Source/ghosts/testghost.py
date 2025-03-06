import ghost
import pygame

pygame.init()

width = 900
height = 950

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Ghost test") 

timer = pygame.time.Clock()

fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)


run = True
while run:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False
    pygame.display.update() 
    