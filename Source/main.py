# Mê cung đơn giản
from maze import Maze
import time

# file ghost.py in folder ghosts
from Ghost import Ghost, BlueGhost, OrangeGhost, PinkGhost, RedGhost
from GameManager import GameManager
from Pacman import Pacman, PacmanState
import copy
import threading
import pygame

# Khởi tạo trò chơi
maze_grid = [
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
['#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '.', '.', '#', '#', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '#', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '#', '#', '#', '.', '#', '.', '.', '.', '.', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '#', '#', '#'],
['#', '.', '*', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.', '.', '#', '.', '#', '.', '*', '.', '#'],
['#', '.', '.', '#', '#', '#', '.', '.', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '#', '#', '.', '#'],
['#', '.', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '#', '.', '#', '#', '.', '.', '.', '.', '#', '#', '#', '.', '.', '.', '#'],
['#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '.', '#', '.', '#', '.', '#', '.', '#', '#', '.', '#', '#', '.', '.', '.', '#', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '#', '#', '#', '.', '#', '#', '.', '#', '.', '.', '#', '#', '.', '.', '#', '.', '#', '.', '#', '.', '#', '.', '#', '#', '.', '.', '#', '.', '#'],
['#', '.', '.', '#', '.', '.', '.', '.', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '.', '#', '.', '#', '.', '.', '.', '#', '.', '#'],
['#', '.', '#', '#', '.', '.', '#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '#', '#', '#', '.', '#'],
['#', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#'],
['#', '#', '#', '#', '.', '.', '#', '.', '#', '#', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '#', '#', '.', '#', '#', '#', '.', '#', '#', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '#', '#', '#', '.', '#', '#'],
['#', '.', '#', '.', '#', '.', '.', '.', '#', '.', '.', '#', '#', '#', '.', '.', '#', '#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '.', '.', '#'],
['#', '.', '.', '.', '#', '.', '#', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '#'],
['#', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '.', '#'],
['#', '.', '#', '#', '#', '#', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '.', '#', '#', '.', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
['#', '.', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '.', '#', '.', '#', '.', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
['#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '#', '.', '#', '#', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#'],
['#', '.', '*', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '*', '.', '#'],
['#', '.', '#', '#', '.', '.', '.', '#', '.', '#', '.', '#', '.', '#', '#', '.', '.', '#', '.', '.', '#', '#', '.', '#', '.', '.', '.', '#', '.', '#'],
['#', '.', '#', '.', '.', '#', '#', '#', '.', '#', '.', '#', '.', '.', '#', '.', '#', '#', '.', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '#'],
['#', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '#'],
['#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '.', '.', '#', '.', '.', '.', '.', '#', '#', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '#'],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]

pygame.init()
 
# get the width and height of the screen
infoObject = pygame.display.Info()
screen_width, screen_height = infoObject.current_w, infoObject.current_h
screen_height *= 0.9
screen_width *= 0.9

if screen_width > screen_height:
    screen_width = int(screen_height)
else:
    screen_height = int(screen_width)

color = 'blue'
PI = 3.14159265358979323846
#draw the Board
rows = len(maze_grid)
cols = len(maze_grid[0])
cell_width = int(screen_width / cols)
cell_height = int(screen_height / rows)

# Restrist it to a square
if cell_width > cell_height:
    cell_size = cell_height
else: 
    cell_size = cell_width

# Set the figures of the game
maze = Maze(maze_grid_2)
pacman = Pacman(maze, (15, 15), cell_size, cell_size)  # Vị trí ban đầu của Pac-Man
ghosts = [BlueGhost(maze, (1, 1), "BlueGhost", (cell_size, cell_size)), PinkGhost(maze, (28, 1), "PinkGhost", (cell_size, cell_size)), OrangeGhost(maze, (1, 29), "OrangeGhost", (cell_size, cell_size)), RedGhost(maze, (28, 29), "RedGhost",(cell_size, cell_size))]  # BlueGhost bắt đầu tại (1, 2)
positions = {"BlueGhost": (1, 1), "PinkGhost": (28, 1), "OrangeGhost": (1, 29), "RedGhost": (28, 29)}  # Vị trí ban đầu của các Ghost
game = GameManager(maze, pacman, ghosts, positions, cell_size)
pacman_closed = False
pacman_state = "None"
switch_interval = 0.2
last_switch_time = time.time()
# create the screen

screen = pygame.display.set_mode((cell_size * cols, cell_size * rows))
timer = pygame.time.Clock()
 
fps = 800
font = pygame.font.Font('freesansbold.ttf', 32)

# Game states
MENU = "menu"
PLAYING = "playing"
game_state = MENU

# Menu button properties
button_width, button_height = 200, 50
button_x = (screen_width - button_width) // 2
button_y = (screen_height - button_height) // 2
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
button_color = (0, 255, 0)  # Green
button_hover_color = (0, 200, 0)  # Darker green on hover

game.start()

running = True
while running:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    game.draw(pygame, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pacman_closed = False
                pacman_state = PacmanState.UP
                game.pacman.set_direction(pacman_state)
                game.move_pacman()
                print(f"Pac-Man moved to {game.get_pacman_pos()}")
            elif event.key == pygame.K_DOWN:
                pacman_closed = False
                pacman_state = PacmanState.DOWN
                game.pacman.set_direction(pacman_state)
                game.move_pacman()
                print(f"Pac-Man moved to {game.get_pacman_pos()}")
            elif event.key == pygame.K_LEFT:
                pacman_closed = False
                pacman_state = PacmanState.LEFT
                game.pacman.set_direction(pacman_state)
                game.move_pacman()
                print(f"Pac-Man moved to {game.get_pacman_pos()}")
            elif event.key == pygame.K_RIGHT:
                pacman_closed = False
                pacman_state = PacmanState.RIGHT
                game.pacman.set_direction(pacman_state)
                game.move_pacman()
                print(f"Pac-Man moved to {game.get_pacman_pos()}")
            elif event.key == pygame.K_q:
                running = False
                print("Quitting...")
    # Switch Pac-Man sprite
    current_time = time.time()
    if current_time - last_switch_time > switch_interval:
        if pacman_closed == False:
            game.pacman.set_direction("None")
            pacman_closed = True
        else:
            game.pacman.set_direction(pacman_state)
            pacman_closed = False
        last_switch_time = current_time
    score_text = font.render(f"Score: {game.pacman.score}", True, (255, 255, 255))  # White text
    score_rect = score_text.get_rect(center=(screen_width // 2, 200 // 2))
    screen.blit(score_text, score_rect)
 
    pygame.display.flip()
 
pygame.quit()

# Bắt đầu trò chơi (khởi động các luồng ghost)

#while running and game.is_running():
    # for event in pygame.event.get():
    #     

game.stop()

