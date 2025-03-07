import pygame 
import copy

from board import boards

pygame.init()

# get the width and height of the screen
infoObject = pygame.display.Info()
screen_width, screen_height = infoObject.current_w, infoObject.current_h
screen_height = screen_height * 9 / 10
screen_width = screen_width * 6 / 10
boardGame = copy.deepcopy(boards)
flicker = False
color = 'blue'
PI = 3.14159265358979323846

def draw_board():
    rows = len(boardGame)
    cols = len(boardGame[0])
    num1 = (screen_width / cols)
    num2 = (screen_height / rows)
    num = int(num2 / 10 + 1)
    print(num1, num2)  
    for i in range(rows):
        for j in range(cols):
            if boardGame[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num1 + 0.5 * num1, i * num2 + 0.5 * num2), num + 1)
            if boardGame[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j * num1 + 0.5 * num1, i * num2 + 0.5 * num2), num * 3 + 1)
            if boardGame[i][j] == 3:
                pygame.draw.line(screen, color, (j * num1 + (0.5 * num1), i * num2),
                                 (j * num1 + (0.5 * num1), i * num2 + num2), num)
            if boardGame[i][j] == 4:
                pygame.draw.line(screen, color, (j * num1, i * num2 + (0.5 * num2)),
                                 (j * num1 + num1, i * num2 + (0.5 * num2)), num)
            if boardGame[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num1 - (num1 * 0.4)) - 2, (i * num2 + (0.5 * num2)), num1, num2],
                                0, PI / 2, num)
            if boardGame[i][j] == 6:
                pygame.draw.arc(screen, color,
                                [(j * num1 + (num1 * 0.5)), (i * num2 + (0.5 * num2)), num1, num2], PI / 2, PI, num)
            if boardGame[i][j] == 7:
                pygame.draw.arc(screen, color, [(j * num1 + (num1 * 0.5)), (i * num2 - (0.4 * num2)), num1, num2], PI,
                                3 * PI / 2, num)
            if boardGame[i][j] == 8:
                pygame.draw.arc(screen, color,
                                [(j * num1 - (num1 * 0.4)) - 2, (i * num2 - (0.4 * num2)), num1, num2], 3 * PI / 2,
                                2 * PI, num)
            if boardGame[i][j] == 9:
                pygame.draw.line(screen, 'white', (j * num1, i * num2 + (0.5 * num2)),
                                 (j * num1 + num1, i * num2 + (0.5 * num2)), num)
       
           

# create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
timer = pygame.time.Clock()

fps = 60
font = pygame.font.Font('freesansbold.ttf', 32)

running = True
while running:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
