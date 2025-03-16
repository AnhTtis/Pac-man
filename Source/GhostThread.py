import threading
import time
from typing import Dict, Tuple, Optional, Callable

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
        while self.running.is_set():
            with self.lock:
                self.ghost.maze.set_element(self.last_pos, '!')
                self.ghost.find_path(self.pacman.pos)
                self.ghost.maze.set_element(self.last_pos, '.') 
            time.sleep(0.1)

    def run(self) -> None:
        while self.running.is_set():
            # if not self.ghost.paused:
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
                            # self.ghost.paused = True
                            self.pacman.paused = True
                            if self.on_catch:
                                self.on_catch(self.ghost.name, self.ghost.pos)
                            self.running.clear()
                else:
                    direction = (self.ghost.pos[0] - self.last_pos[0], self.ghost.pos[1] - self.last_pos[1])
                    next_pos = (self.ghost.pos[0] + direction[0], self.ghost.pos[1] + direction[1])
                    # Check if all neighboring positions are walls or occupied by ghosts
                    neighbors = self.ghost.maze.get_neigh(self.ghost.pos)
                    all_walls_or_ghosts = all(self.ghost.maze.is_wall(neighbor) or neighbor in self.positions.values() for neighbor in neighbors)
                    
                    if all_walls_or_ghosts:
                        # If all neighboring positions are walls or occupied by ghosts, do not move
                        continue
                    
                    if (0 <= next_pos[0] < self.ghost.maze.get_cols() and 
                        0 <= next_pos[1] < self.ghost.maze.get_rows() and 
                        not self.ghost.maze.is_wall(next_pos) and 
                        next_pos not in self.positions.values()):
                                                
                        self.last_pos = self.ghost.pos
                        self.ghost.set_pos(next_pos)
                        self.positions[self.ghost.name] = self.ghost.pos
                    else:
                        # Try to find an alternative valid move
                        for neighbor in neighbors:
                            if (0 <= neighbor[0] < self.ghost.maze.get_cols() and 
                                0 <= neighbor[1] < self.ghost.maze.get_rows() and 
                                not self.ghost.maze.is_wall(neighbor) and 
                                neighbor not in self.positions.values()):
                                
                                self.last_pos = self.ghost.pos
                                self.ghost.set_pos(neighbor)
                                self.positions[self.ghost.name] = self.ghost.pos
                                break
                        
            time.sleep(self.move_interval)
            