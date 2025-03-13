# from Maze import Maze
# from Ghost import Ghost, BlueGhost, OrangeGhost, PinkGhost, RedGhost
# from GameManager import GameManager
# from Pacman import Pacman
# import pygame

# import copy
# import threading
# import time


# # maze_grid = [
# # ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
# # ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
# # ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#'],
# # ['#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
# # ['#', '#', '*', '#', ' ', ' ', '#', '.', '#', ' ', ' ', ' ', '#', '.', '#', '#', '.', '#', ' ', ' ', ' ', '#', '.', '#', ' ', ' ', '#', '*', '#', '#'],
# # ['#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
# # ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#'],
# # ['#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
# # ['#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
# # ['#', '#', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#'],
# # ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
# # ['#', ' ', ' ', ' ', ' ', ' ', '#', '.', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#', '.', '#', ' ', ' ', ' ', ' ', ' ', '#'],
# # ['#', ' ', ' ', ' ', ' ', ' ', '#', '.', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '.', '#', ' ', ' ', ' ', ' ', ' ', '#'],
# # ['#', ' ', ' ', ' ', ' ', ' ', '#', '.', '#', '#', ' ', '#', '#', '#', 'G', 'G', '#', '#', '#', ' ', '#', '#', '.', '#', ' ', ' ', ' ', ' ', ' ', '#'],
# # ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
# # [' ', ' ', ' ', ' ', ' ', ' ', ' ', '.', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '.', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
# # ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
# # ['#', ' ', ' ', ' ', ' ', ' ', '#', '.', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '.', '#', ' ', ' ', ' ', ' ', ' ', '#'],
# # ['#', ' ', ' ', ' ', ' ', ' ', '#', '.', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '.', '#', ' ', ' ', ' ', ' ', ' ', '#'],
# # ['#', ' ', ' ', ' ', ' ', ' ', '#', '.', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '.', '#', ' ', ' ', ' ', ' ', ' ', '#'],
# # ['#', '#', '#', '#', '#', '#', '#', '.', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#'],
# # ['#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#'],
# # ['#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
# # ['#', '#', '.', '#', '#', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '.', '#', '#', '#', '#', '.', '#', '#'],
# # ['#', '#', '*', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '*', '#', '#'],
# # ['#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
# # ['#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
# # ['#', '#', '.', '.', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '#', '#', '.', '.', '.', '.', '.', '.', '#', '#'],
# # ['#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '.', '#', '#'],
# # ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
# # ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
# #     ]

# pygame.init()

# WINDOW_WIDTH = 400
# WINDOW_HEIGHT = 300
# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Test Arrow Keys")

# # Màu sắc
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)


# maze_grid = [
#     ["#", "#", "#", "#", "#"],
#     ["#", ".", ".", ".", "#"],
#     ["#", ".", "#", ".", "#"],
#     ["#", ".", ".", "P", "#"],
#     ["#", "#", "#", "#", "#"]
# ]

# # maze = Maze(maze_grid)
# # # Add pacman and all ghosts to the game, ghosts have name and position
# # ghosts = [BlueGhost(maze, (14, 1), "BlueGhost")]
# # #positions = {'BlueGhost': (3, 4), 'PinkGhost': (5, 3)}
# # positions = {"BlueGhost": (14, 1)}
# # game = GameManager(maze, (14, 24), ghosts, positions)
# # print(game.get_pacman_pos())

# maze = Maze(maze_grid)
# #test blue ghost
# pacman = Pacman(maze, (3, 3))
# ghosts = [BlueGhost(maze, (1, 2), "BlueGhost")]
# positions = {"BlueGhost": (1, 2)}
# #test orange ghost
# # pacman = Pacman(maze, (3, 3))
# # ghosts = [OrangeGhost(maze, (1, 2), "OrangeGhost")]
# # positions = {"OrangeGhost": (1, 2)}
# #test pink ghost
# # pacman = Pacman(maze, (3, 3))
# # ghosts = [PinkGhost(maze, (1, 2), "PinkGhost")]
# # positions = {"PinkGhost": (1, 2)}
# #test red ghost
# # pacman = Pacman(maze, (3, 3))
# # ghosts = [RedGhost(maze, (1, 2), "RedGhost")]
# # positions = {"RedGhost": (1, 2)}
# game = GameManager(maze, pacman, ghosts, positions)
# game.start()

# clock = pygame.time.Clock()
# running = True

# print("testtest")

# while running and game.is_running():
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 game.move_pacman("up")
#                 print(f"Pac-Man moved to {game.get_pacman_pos()}")
#             elif event.key == pygame.K_DOWN:
#                 game.move_pacman("down")
#                 print(f"Pac-Man moved to {game.get_pacman_pos()}")
#             elif event.key == pygame.K_LEFT:
#                 game.move_pacman("left")
#                 print(f"Pac-Man moved to {game.get_pacman_pos()}")
#             elif event.key == pygame.K_RIGHT:
#                 game.move_pacman("right")
#                 print(f"Pac-Man moved to {game.get_pacman_pos()}")
#             elif event.key == pygame.K_q:
#                 running = False

# while game.is_running():
#     time.sleep(1)
# game.stop()

import pygame
from maze import Maze
from Ghost import BlueGhost
from GameManager import GameManager
from Pacman import Pacman

# Khởi tạo Pygame
pygame.init()

# Cấu hình cửa sổ
CELL_SIZE = 40  # Kích thước mỗi ô trong mê cung
WINDOW_WIDTH = 5 * CELL_SIZE  # Chiều rộng cửa sổ (5 cột)
WINDOW_HEIGHT = 5 * CELL_SIZE  # Chiều cao cửa sổ (5 hàng)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pac-Man Game")

# Màu sắc
WHITE = (255, 255, 255)  # Nền
BLACK = (0, 0, 0)       # Tường
YELLOW = (255, 255, 0)   # Pac-Man
BLUE = (0, 0, 255)      # BlueGhost
GRAY = (128, 128, 128)   # Điểm

# Mê cung đơn giản
maze_grid = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", "P", "#"],
    ["#", "#", "#", "#", "#"]
]

# Hàm vẽ mê cung, Pac-Man và Ghosts
def draw_game(screen: pygame.Surface, maze: Maze, pacman_pos: tuple, ghost_positions: dict):
    screen.fill(WHITE)  # Nền trắng
    
    # Vẽ mê cung
    for y, row in enumerate(maze._Maze__grid):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if cell == '#':
                pygame.draw.rect(screen, BLACK, rect)  # Tường
            elif cell == '.':
                pygame.draw.circle(screen, GRAY, rect.center, 5)  # Điểm nhỏ
    
    # Vẽ Pac-Man
    px, py = pacman_pos
    pygame.draw.circle(screen, YELLOW, (px * CELL_SIZE + CELL_SIZE // 2, py * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 2)
    
    # Vẽ Ghosts
    for ghost_name, (gx, gy) in ghost_positions.items():
        pygame.draw.circle(screen, BLUE, (gx * CELL_SIZE + CELL_SIZE // 2, gy * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 2)
    
    pygame.display.flip()  # Cập nhật màn hình

# Khởi tạo trò chơi
maze = Maze(maze_grid)
pacman = Pacman(maze, (3, 3))  # Vị trí ban đầu của Pac-Man
ghosts = [BlueGhost(maze, (1, 2), "BlueGhost")]  # BlueGhost bắt đầu tại (1, 2)
positions = {"BlueGhost": (1, 2)}
game = GameManager(maze, pacman, ghosts, positions)

# Bắt đầu trò chơi (khởi động các luồng ghost)
game.start()

# Vòng lặp chính
clock = pygame.time.Clock()
running = True

print("Game started. Use arrow keys to move Pac-Man, 'Q' to quit.")

while running and game.is_running():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.move_pacman("up")
                print(f"Pac-Man moved to {game.get_pacman_pos()}")
            elif event.key == pygame.K_DOWN:
                game.move_pacman("down")
                print(f"Pac-Man moved to {game.get_pacman_pos()}")
            elif event.key == pygame.K_LEFT:
                game.move_pacman("left")
                print(f"Pac-Man moved to {game.get_pacman_pos()}")
            elif event.key == pygame.K_RIGHT:
                game.move_pacman("right")
                print(f"Pac-Man moved to {game.get_pacman_pos()}")
            elif event.key == pygame.K_q:
                running = False
                print("Quitting...")

    # Vẽ trạng thái trò chơi
    draw_game(screen, maze, game.get_pacman_pos(), game.positions)

    # Giới hạn tốc độ khung hình
    clock.tick(30)  # 30 FPS

# Dừng trò chơi
game.stop()
pygame.quit()
print("Game stopped.")