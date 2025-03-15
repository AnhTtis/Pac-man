# Mê cung đơn giản
from maze import Maze
import time
import tracemalloc

# file ghost.py in folder ghosts
from Ghost import Ghost, BlueGhost, OrangeGhost, PinkGhost, RedGhost
from GameManager import GameManager
from Pacman import Pacman, PacmanState
import copy
import threading
import pygame
from record import Record

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
    ['#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '#', '.', '#', '#', '.', '#', '#', '.', '.', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '.', '#', '#', '.', '#', '.', '.', '#', '#', '.', '.', '#', '.', '#', '.', '#', '.', '#', '.', '#', '#', '.', '.', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '.', '#', '.', '#', '.', '.', '.', '#', '.', '#'],
    ['#', '.', '#', '#', '.', '.', '#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '.', '.', '#', '.', '#', '#', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#', '#', '#', '.', '#', '#', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '#', '#', '#', '.', '#', '#'],
    ['#', '.', '#', '.', '#', '.', '.', '.', '#', '.', '.', '#', '#', '#', '.', '.', '#', '#', '#', '.', '#', '#', '.', '#', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '.', '.', '#', '.', '#', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '#'],
    ['#', '.', '.', '.', '#', '.', '#', '.', '.', '.', '.', '#', '#', '#', '#', '#', '#', '#', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '.', '.', '#', '.', '#', '.', '.', '.', '.', '.', '#', '#', '.', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '.', '#', '.', '#', '.', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
    ['#', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '#', '#', '.', '#', '#', '.', '.', '#', '.', '.', '.', '.', '#', '.', '.', '#'],
    ['#', '.', '*', '.', '.', '#', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '*', '.', '#'],
    ['#', '.', '#', '#', '.', '.', '.', '#', '.', '#', '.', '#', '.', '#', '#', '.', '.', '#', '.', '.', '#', '#', '.', '#', '.', '.', '.', '#', '.', '#'],
    ['#', '.', '#', '.', '.', '#', '#', '#', '.', '#', '.', '#', '.', '.', '#', '.', '#', '#', '.', '.', '#', '.', '.', '#', '.', '#', '#', '#', '.', '#'],
    ['#', '.', '#', '.', '.', '.', '.', '.', '.', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '.', '.', '#', '.', '#', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '.', '.', '#', '.', '.', '.', '.', '#', '#', '.', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

pygame.init()
 
# get the width and height of the screen
infoObject = pygame.display.Info()
screen_width, screen_height = infoObject.current_w, infoObject.current_h
screen_height *= 0.8
screen_width *= 0.8

game_board_size = int(screen_height) if screen_width > screen_height else int(screen_height)

color = 'blue'
PI = 3.14159265358979323846
#draw the Board
rows = len(maze_grid)
cols = len(maze_grid[0])
cell_width = int(game_board_size / cols)
cell_height = int(game_board_size / rows)

# Restrist it to a square
if cell_width > cell_height:
    cell_size = cell_height
else: 
    cell_size = cell_width

# Set the figures of the game
maze = Maze(maze_grid)
pacman = Pacman(maze, (15, 15), cell_size, cell_size)  # Vị trí ban đầu của Pac-Man

ghosts = [
    BlueGhost(maze, (1, 1), "BlueGhost", (cell_size, cell_size)), 
    PinkGhost(maze, (28, 1), "PinkGhost", (cell_size, cell_size)),
    OrangeGhost(maze, (1, 29), "OrangeGhost", (cell_size, cell_size)), 
    RedGhost(maze, (28, 29), "RedGhost",(cell_size, cell_size))
]  # BlueGhost bắt đầu tại (1, 2)

positions = {"BlueGhost": (1, 1), "PinkGhost": (28, 1), "OrangeGhost": (1, 29), "RedGhost": (28, 29)}  # Vị trí ban đầu của các Ghost
game = GameManager(maze, pacman, ghosts, positions, cell_size)
pacman_closed = False
pacman_state = PacmanState.CLOSE
switch_interval = 0.2
last_switch_time = time.time()
# create the screen

screen = pygame.display.set_mode((screen_width, screen_height))
timer = pygame.time.Clock()
 
fps = 800
font = pygame.font.Font('freesansbold.ttf', cell_size)

game.start()
record = Record((cell_size * (cols + 1), cell_size))

running = True
while running:
    timer.tick(fps)
    screen.fill((0, 0, 0))
    game.draw(pygame, screen)
    record.draw(game.ghosts, cell_size, font)

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
            game.pacman.set_direction(PacmanState.CLOSE)
            pacman_closed = True
        else:
            game.pacman.set_direction(pacman_state)
            pacman_closed = False
        last_switch_time = current_time

 
    pygame.display.flip()
 
pygame.quit()

# Bắt đầu trò chơi (khởi động các luồng ghost)

#while running and game.is_running():
    # for event in pygame.event.get():
    #     

game.stop()
