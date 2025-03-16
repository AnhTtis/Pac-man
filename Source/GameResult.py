import pygame
from maze import Maze

class GameResult:
    def __init__(self, screen_width: int, screen_height: int, font, maze : 'Maze'):
        """
        Khởi tạo đối tượng GameOver.

        Args:
            screen_width (int): Chiều rộng của màn hình trò chơi.
            screen_height (int): Chiều cao của màn hình trò chơi.
            font: Font chữ để hiển thị thông báo.
        """
        # Kích thước bảng thông báo (1/3 màn hình)
        self.box_width = screen_width // 3
        self.box_height = screen_height // 3
        self.box_x = (screen_width - self.box_width) // 2  # Căn giữa theo chiều ngang
        self.box_y = (screen_height - self.box_height) // 2  # Căn giữa theo chiều dọc

        # Text "Game Over"
        self.font = font
        if maze.is_no_dot():
            self.text_surface = font.render("You Win", True, (152,251,152))  # Màu xanh cho text
        else:
            self.text_surface = font.render("Game Over", True, (255, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(screen_width // 2, screen_height // 2))  # Căn giữa text
    
    def draw(self, screen):
        """
        Vẽ thông báo "Game Over" ở giữa màn hình.

        Args:
            screen: Màn hình pygame để vẽ.
        """
        # Vẽ hộp màu đen làm nền
        pygame.draw.rect(screen, (0, 0, 0), (self.box_x, self.box_y, self.box_width, self.box_height), border_radius=15)
        
        # Vẽ viền trắng cho hộp
        pygame.draw.rect(screen, (255, 255, 255), (self.box_x, self.box_y, self.box_width, self.box_height), 3, border_radius=15)
        
        # Vẽ text "Game Over"
        screen.blit(self.text_surface, self.text_rect)
