<<<<<<< HEAD
import time
import threading
from typing import List, Tuple, Dict, Optional, Callable
import copy
from maze import Maze 
from Ghost import Ghost, BlueGhost, OrangeGhost, PinkGhost
from GhostThread import GhostThread 
from Pacman import Pacman
=======
# import time
# import threading
# from typing import List, Tuple, Dict, Optional, Callable
# import copy
# from maze import Maze 
# from Ghost import Ghost, BlueGhost, OrangeGhost, PinkGhost
# from GhostThread import GhostThread 
# from Pacman import Pacman
# import pygame 
>>>>>>> 3005eb358132bb4f2bcd70d001c5d0518c329491

# class GameManager:
#     def __init__(self, maze: Maze, pacman: 'Pacman', 
#                  ghosts: List[Ghost], positions: Dict[str, Tuple[int, int]], cell_size: int):
#         self.load_images = False
#         self.maze = maze
#         self.pacman = pacman  # Không deepcopy để tránh lỗi Lock
#         self.ghosts = copy.deepcopy(ghosts)
#         self.positions = positions
#         self.lock = threading.Lock()
#         self.cell_size = cell_size
#         self.running = threading.Event()
#         self.running.set()
#         self.threads = [
#             GhostThread(ghost, self.pacman, self.lock, self.running, self.positions, self.on_ghost_catch) 
#             for ghost in ghosts
#         ]

#     def on_ghost_catch(self, ghost_name: str, pos: Tuple[int, int]) -> None:
#         print(f"Game Over: {ghost_name} caught Pac-Man at {pos}")
#         # threading.Thread(target=self.stop, daemon=True).start()

#     def start(self):
#         for t in self.threads:
#             t.start()
    
#     def draw(self, pygame, screen):
#         #draw the Board
#         rows = self.maze.get_rows()
#         cols = self.maze.get_cols()

#         for y in range(rows):
#             for x in range(cols):
#                 pos = (x, y)
#                 if self.maze.is_wall(pos):
#                     pygame.draw.rect(screen, (0, 0, 255), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
#                 elif self.maze.is_dot(pos):
#                     pygame.draw.circle(screen, (255, 255, 255), (int(x * self.cell_size + self.cell_size / 2), int(y * self.cell_size + self.cell_size / 2)), 3)
#                 elif self.maze.is_big_dot(pos):
#                     pygame.draw.circle(screen, (255, 255, 255), (int(x * self.cell_size + self.cell_size / 2), int(y * self.cell_size + self.cell_size / 2)), 5)
#                 elif self.maze.is_gate(pos):
#                     pygame.draw.rect(screen, (255, 255, 255), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                    
#         if self.load_images == False:
#             for ghost in self.ghosts:
#                 ghost.load_image(pygame)
#             self.pacman.load_image(pygame)
#             self.load_images = True

#         #draw the ghosts 
#         for ghost in self.ghosts:
#             ghost.set_pos(self.positions[ghost.name])
#             ghost.display(screen)
            
#         # draw pac-man
#         self.pacman.display(screen, self.cell_size)        


#     def stop(self):
#         self.running.clear()
#         for t in self.threads:
#             t.join()

#     def is_running(self) -> bool:
#         return self.running.is_set()

#     def get_pacman_pos(self) -> Tuple[int, int]:
#         return self.pacman.pos

#     def move_pacman(self) -> None:
#         self.pacman.move()
import time
import threading
from typing import List, Tuple, Dict, Optional, Callable
import copy
from maze import Maze 
from Ghost import Ghost, BlueGhost, OrangeGhost, PinkGhost
from GhostThread import GhostThread 
from Pacman import Pacman
from PacmanThread import PacmanThread  # Thêm import
import pygame 

class GameManager:
    def __init__(self, maze: Maze, pacman: 'Pacman', 
                 ghosts: List[Ghost], positions: Dict[str, Tuple[int, int]], cell_size: int):
        self.load_images = False
        self.maze = maze
        self.pacman = pacman
        self.ghosts = copy.deepcopy(ghosts)
        self.positions = positions
        self.lock = threading.Lock()
        self.cell_size = cell_size
        self.running = threading.Event()
        self.running.set()
        self.threads = [
            GhostThread(ghost, self.pacman, self.lock, self.running, self.positions, self.on_ghost_catch) 
            for ghost in ghosts
        ]
        # Thêm thread cho Pacman
        self.pacman_thread = PacmanThread(self.pacman, self.lock, self.running)

    def on_ghost_catch(self, ghost_name: str, pos: Tuple[int, int]) -> None:
        print(f"Game Over: {ghost_name} caught Pac-Man at {pos}")
        self.stop()

    def start(self):
        for t in self.threads:
            t.start()
        self.pacman_thread.start()  # Bắt đầu thread của Pacman

    def draw(self, pygame, screen):
        rows = self.maze.get_rows()
        cols = self.maze.get_cols()

        for y in range(rows):
            for x in range(cols):
                pos = (x, y)
                if self.maze.is_wall(pos):
                    pygame.draw.rect(screen, (0, 0, 255), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                elif self.maze.is_dot(pos):
                    pygame.draw.circle(screen, (255, 255, 255), (int(x * self.cell_size + self.cell_size / 2), int(y * self.cell_size + self.cell_size / 2)), 3)
                elif self.maze.is_big_dot(pos):
                    pygame.draw.circle(screen, (255, 255, 255), (int(x * self.cell_size + self.cell_size / 2), int(y * self.cell_size + self.cell_size / 2)), 5)
                elif self.maze.is_gate(pos):
                    pygame.draw.rect(screen, (255, 255, 255), (x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))
                    
        if not self.load_images:
            for ghost in self.ghosts:
                ghost.load_image(pygame)
            self.pacman.load_image(pygame)
            self.load_images = True

        for ghost in self.ghosts:
            ghost.set_pos(self.positions[ghost.name])
            ghost.display(screen)
            
        self.pacman.display(screen, self.cell_size)        

    def stop(self):
        self.running.clear()
        for t in self.threads:
            t.join()
        self.pacman_thread.join()  # Đợi thread của Pacman kết thúc

    def is_running(self) -> bool:
        return self.running.is_set()

    def get_pacman_pos(self) -> Tuple[int, int]:
        return self.pacman.pos