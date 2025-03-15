import threading
import time
from typing import Dict, Tuple, Optional, Callable

from maze import Maze
from Ghost import Ghost
from Pacman import Pacman

class GhostThread(threading.Thread):
    def __init__(self, ghost: Ghost, pacman: 'Pacman', lock: threading.Lock, 
                 running: threading.Event, positions: Dict[str, Tuple[int, int]], 
                 on_catch: Optional[Callable[[str, Tuple[int, int]], None]] = None):
        super().__init__()
        self.ghost = ghost
        self.pacman = pacman
        self.lock = lock
        self.running = running
        self.positions = positions
        self.on_catch = on_catch
        self.last_pos = ghost.pos  
        self.move_interval = 0.3

        self.pathfinding_thread = threading.Thread(target=self.update_path, daemon=True)
        self.pathfinding_thread.start()

    def update_path(self) -> None:
        # last_pacman_pos = None
        #print ghost's statics
        self.ghost.show_search_statistics()
        while self.running.is_set():
            with self.lock:
                self.ghost.maze.set_element(self.last_pos, '#')
                self.ghost.find_path(self.pacman.pos)
                self.ghost.maze.set_element(self.last_pos, '.') 
            time.sleep(0.1)

    def run(self) -> None:
        while self.running.is_set():
            with self.lock:
                if self.ghost.path and len(self.ghost.path) > 1:
                    next_pos = self.ghost.path[1]
                    if next_pos not in self.positions.values():
                        self.last_pos = self.ghost.pos
                        
                        self.ghost.set_pos(next_pos)
                        self.ghost.path.pop(0)
                        self.positions[self.ghost.name] = self.ghost.pos
                        #print(f"{self.ghost.name} moved to {self.ghost.pos}")
                        if self.ghost.pos == self.pacman.pos:
                            print(f"{self.ghost.name} caught Pac-Man at {self.ghost.pos}!")
                            # if self.on_catch:
                            #     self.on_catch(self.ghost.name, self.ghost.pos)
                            # self.running.clear()
                else:
                    direction = (self.ghost.pos[0] - self.last_pos[0], self.ghost.pos[1] - self.last_pos[1])
                    next_pos = (self.ghost.pos[0] + direction[0], self.ghost.pos[1] + direction[1])
                    
                    if (0 <= next_pos[0] < self.ghost.maze.get_cols() and 
                        0 <= next_pos[1] < self.ghost.maze.get_rows() and 
                        self.ghost.maze.is_wall(next_pos) == False and 
                        next_pos not in self.positions.values()):
                        
                        self.last_pos = self.ghost.pos
                        self.ghost.set_pos(next_pos)
                        self.positions[self.ghost.name] = self.ghost.pos
                        
            time.sleep(self.move_interval)