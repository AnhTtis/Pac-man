# search time, memory usage, and number of expanded nodes
import time
import tracemalloc
from typing import Tuple, List
from ghost import Ghost
import pygame

class Record:
    def __init__(self, pos: Tuple[int, int]):
        self.pos = pos
        
        self.start_memory_usage = tracemalloc.get_traced_memory()[0]
    
    def get_memory_usage(self, start_memory_usage):
        self.memory_usage = tracemalloc.get_traced_memory()[1]
        return f"Peak memory usage: {self.memory_usage / 1024:.2f} KB"
    
    def draw(self, ghosts: List[Ghost], pixel_size: int, font, start_memory_usage):
        x, y = self.pos
        
        for ghost in ghosts:
            name_surface = font.render(f"Ghost: {ghost.name}", True, (255, 255, 0))
            pygame.display.get_surface().blit(name_surface, (x, y))
            y += pixel_size

            info = (
                f"Search Time: {ghost.search_time:.2f} ms\n"
                f"Number of Expanded Nodes: {ghost.n_expanded_nodes}\n"
            )
            lines = info.split('\n')
            for line in lines:
                text_surface = font.render(line, True, (255, 255, 255))
                pygame.display.get_surface().blit(text_surface, (x, y))
                y += pixel_size
            y += pixel_size

        memory_info = self.get_memory_usage(start_memory_usage)
        memory_surface = font.render(memory_info, True, (0, 255, 0))
        pygame.display.get_surface().blit(memory_surface, (x, y))
