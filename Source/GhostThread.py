import threading
import time

from maze import Maze
from ghosts.ghost import Ghost

class GhostThread(threading.Thread):
    def __init__(self, ghost, pacman, lock, running, position):
        threading.Thread.__init__(self)
        self.ghost = ghost
        
        #golbal pacman object
        #changing pacman position will be reflected in the global object
        self.pacman = pacman
        self.lock = lock
        self.running = running
        self.position = position

    def run(self):
        while self.running.is_set():
            with self.lock:
                next_pos = self.ghost.move(self.pacman.pos)
                if next_pos and next_pos not in self.position.values():
                    self.ghost.pos = next_pos
                    self.position[self.ghost.name] = self.ghost.pos
                    
                    # if ghost caught pacman
                    if self.ghost.pos == self.pacman.pos:
                        print(f"{self.ghost.name} caught Pac-Man at {self.ghost.pos}!")
            time.sleep(0.1)
    