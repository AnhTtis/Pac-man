# search time, memory usage, and number of expanded nodes
import time
import tracemalloc
from typing import Tuple, List
from Ghost import Ghost
import pygame

class Record:
    def __init__(self, pos: Tuple[int, int]):
        self.pos = pos
    
    def draw(self, ghosts: List[Ghost], pixel_size: int, font):
        x, y = self.pos
        
        for ghost in ghosts:
            name_surface = font.render(f"Ghost: {ghost.name}", True, (255, 255, 0))
            pygame.display.get_surface().blit(name_surface, (x, y))
            y += pixel_size
            memory_usage_mb = ghost.searched_memory / 10**6
            info = (
                f"Search Time: {ghost.searched_time:.6f} s\n"
                f"Number of Expanded Nodes: {ghost.searched_nodes}\n"
                f"Memory Usage: {memory_usage_mb:.6f} MB\n"
            )
            lines = info.split('\n')
            for line in lines:
                text_surface = font.render(line, True, (255, 255, 255))
                pygame.display.get_surface().blit(text_surface, (x, y))
                y += pixel_size
            y += pixel_size
