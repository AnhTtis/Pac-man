import pygame
import time
import ghost

# Khởi tạo Pygame và vẽ con ma
pygame.init()
FPS = 60
clock = pygame.time.Clock()

# Kích thước cửa sổ
screen_info = pygame.display.Info()
WIDTH = int(screen_info.current_w * .9)
HEIGHT = int(screen_info.current_h * .8)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ghost Drawing")

# Màu sắc
BACKGROUND_COLOR = (0, 0, 0)  # Màu nền
BLOCK_SIZE = HEIGHT / 40    # Kích thước mỗi ô

blue_ghost = ghost.Blue([50, 50], BLOCK_SIZE, BLOCK_SIZE)
red_ghost = ghost.Red([100, 50], BLOCK_SIZE, BLOCK_SIZE)
pink_ghost = ghost.Pink([150, 50], BLOCK_SIZE, BLOCK_SIZE)
orange_ghost = ghost.Orange([200, 50], BLOCK_SIZE, BLOCK_SIZE)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vẽ nền
    screen.fill(BACKGROUND_COLOR)

    blue_ghost.display(screen)
    red_ghost.display(screen)
    pink_ghost.display(screen)
    orange_ghost.display(screen)
    
    blue_ghost.move(1, 0)

    # Cập nhật màn hình
    pygame.display.flip()

pygame.quit()
