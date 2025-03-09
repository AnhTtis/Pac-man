import pygame
from ghost_appearance import ghost_appearance_matrix
import ghost

# Khởi tạo Pygame và vẽ con ma
pygame.init()

# Kích thước cửa sổ
screen_info = pygame.display.Info()
WIDTH = int(screen_info.current_w * .9)
HEIGHT = int(screen_info.current_h * .8)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ghost Drawing")

# Màu sắc
BACKGROUND_COLOR = (0, 0, 0)  # Màu nền
BLOCK_SIZE = HEIGHT / 40    # Kích thước mỗi ô
PIXEL_SIZE = int(BLOCK_SIZE / len(ghost_appearance_matrix[0]))
print(PIXEL_SIZE)

blue_ghost = ghost.Blue(50, 50)
red_ghost = ghost.Red(100, 50)
pink_ghost = ghost.Pink(150, 50)
yellow_ghost = ghost.Yellow(200, 50)

# Vòng lặp chính
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Vẽ nền
    screen.fill(BACKGROUND_COLOR)

    # Vẽ con ma tại tọa độ (50, 50)
    blue_ghost.display(screen, PIXEL_SIZE)
    red_ghost.display(screen, PIXEL_SIZE)
    pink_ghost.display(screen, PIXEL_SIZE)
    yellow_ghost.display(screen, PIXEL_SIZE)

    # Cập nhật màn hình
    pygame.display.flip()

pygame.quit()
