# search time, memory usage, and number of expanded nodes
import time
import tracemalloc
from typing import Tuple

class Record:
    def __init__(self, name: str, pos: Tuple[int, int], size: Tuple[int, int], font_size: int):
        self.name = name

        self.start_time = time.time()
        self.start_memory_usage = tracemalloc.start()

        self.search_time = self.memory_usage = self.number_expanded_nodes = 0

    def get_search_time(self):
        self.search_time = time.time - self.start_time
        return "Search time: " + str(self.search_time)
    
    def get_memory_usage(self):
        self.memory_usage = tracemalloc.get_traced_memory() - self.start_memory_usage
        return "Memory usage: " + str(self.memory_usage)
    
    def get_number_expanded_nodes(self):
        return "Number of expanded nodes: " + str(self.number_expanded_nodes)