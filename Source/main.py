# Mê cung đơn giản
from maze import Maze
import time

# file ghost.py in folder ghosts
from Ghost import Ghost, BlueGhost, OrangeGhost, PinkGhost, RedGhost
from GameManager import GameManager
from Pacman import Pacman
import copy
import threading
import pygame

# Khởi tạo trò chơi
maze_grid = [
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
['#', '.', '#', '#', '.', '.', '.', '.', '#', '#', '#', '.', '#', '.', '.', '.', '#', '#', '.', '.', '.', '#', '#', '.', '.', '.', '#', '#', '#', '#'],
['#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#'],
['#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '.', '#'],
['#', '.', '*', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '#', '.', '.', '.', '.', '#', ' ', ' ', '#', '*', '.', '#'],
['#', '.', '.', '#', '#', '#', '#', '.', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '#', '#'],
['#', '.', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '.', '.', '.', '#', '#', '#', '#', '.', '#', '#'],
['#', '.', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '#', '#', '#', '.', '.', '#', '.', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#'],
['#', '.', '.', '#', '.', '.', '.', '.', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '.', '#', '.', '.', '.', '.', '.', '#'],
['#', '.', '#', '#', '.', '.', '#', '.', '.', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '.', '#', '.', '.', '.', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '#', '#', '#', '#', ' ', '#', '#', '#', 'G', 'G', '#', '#', '#', ' ', '#', '#', '.', '#', '.', '.', '.', '.', '.', '#'],
['#', '#', '#', '#', '#', '#', '#', '.', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '.', '.', '.', '.', '.', '.', '.', '#'],
['#', '#', '#', '.', '#', '#', '#', '.', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
['#', '#', '#', '.', '#', '.', '.', '.', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '.', '#', '.', '#', '.', '.', '.', '#'],
['#', '#', '.', '.', '#', '.', '#', '.', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '.', '#', '.', '#', '#', '.', '.', '#'],
['#', '.', '.', '#', '#', '.', '#', '.', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '.', '#', '.', '.', '.', '.', '.', '#'],
['#', '#', '#', '#', '#', '#', '#', '.', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
['#', '.', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
['#', '.', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '.', '.', '#', '#', '.', '.', '#'],
['#', '.', '*', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '*', '#', '#'],
['#', '.', '#', '#', '.', '#', '#', '#', '.', '#', '.', '#', '.', '#', '#', '.', '#', '#', '.', '.', '#', '#', '.', '#', '.', '.', '#', '#', '.', '#'],
['#', '.', '.', '#', '.', '#', '#', '.', '.', '#', '.', '#', '#', '.', '#', '.', '#', '#', '.', '.', '#', '.', '.', '#', '.', '.', '#', '#', '.', '#'],
['#', '.', '#', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '#'],
['#', '.', '.', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '.', '#', '#', '.', '#', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '#'],
['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.', '#', '.', '.', '#', '#', '.', '.', '.', '.', '.', '#'],
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
maze = Maze(maze_grid)
pacman = Pacman(maze, (14, 24), cell_size, cell_size)  # Vị trí ban đầu của Pac-Man
ghosts = [BlueGhost(maze, (1, 2), "BlueGhost", (cell_size, cell_size)), PinkGhost(maze, (1, 3), "PinkGhost", (cell_size, cell_size))]  # BlueGhost bắt đầu tại (1, 2)
positions = {"BlueGhost": (1, 2), "PinkGhost": (1, 3)}
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

# ... (phần đầu giữ nguyên)

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
                pacman_state = "up"
                game.pacman.set_direction("up")  # Chỉ thay đổi hướng
                print(f"Pac-Man direction set to up, position: {game.get_pacman_pos()}")
            elif event.key == pygame.K_DOWN:
                pacman_closed = False
                pacman_state = "down"
                game.pacman.set_direction("down")
                print(f"Pac-Man direction set to down, position: {game.get_pacman_pos()}")
            elif event.key == pygame.K_LEFT:
                pacman_closed = False
                pacman_state = "left"
                game.pacman.set_direction("left")
                print(f"Pac-Man direction set to left, position: {game.get_pacman_pos()}")
            elif event.key == pygame.K_RIGHT:
                pacman_closed = False
                pacman_state = "right"
                game.pacman.set_direction("right")
                print(f"Pac-Man direction set to right, position: {game.get_pacman_pos()}")
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

    pygame.display.flip()

pygame.quit()
game.stop()