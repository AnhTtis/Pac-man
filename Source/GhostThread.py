import threading
import time
from typing import Dict, Tuple, Optional, Callable

from Maze import Maze
from Ghost import Ghost
from Pacman import Pacman

class GhostThread(threading.Thread):
    """A thread that controls a ghost's movement to chase Pac-Man."""
    def __init__(self, ghost: Ghost, pacman: 'Pacman', lock: threading.Lock, 
                 running: threading.Event, positions: Dict[str, Tuple[int, int]], 
                 on_catch: Optional[Callable[[str, Tuple[int, int]], None]] = None):
        """
        Initialize the ghost thread with its ghost and shared game state.

        Args:
            ghost: The Ghost object (e.g., BlueGhost, PinkGhost) to control
            pacman: The Pacman object to chase, shared across threads
            lock: Threading lock to synchronize access to shared resources
            running: Threading event to control the thread's execution
            positions: Dictionary mapping ghost names to their current (x, y) positions
            on_catch: Optional callback function to call when Pac-Man is caught
        """
        threading.Thread.__init__(self)
        self.ghost: Ghost = ghost
        self.pacman: 'Pacman' = pacman
        self.lock: threading.Lock = lock
        self.running: threading.Event = running
        self.positions: Dict[str, Tuple[int, int]] = positions
        self.on_catch: Optional[Callable[[str, Tuple[int, int]], None]] = on_catch
        self.move_interval: float = 0.5

    def run(self) -> None:
        """
        Execute the ghost's movement loop until stopped or Pac-Man is caught.

        Updates the ghost's position based on its move algorithm and checks for
        collision with Pac-Man. Calls the on_catch callback if provided when
        Pac-Man is caught. Runs until the running event is cleared.
        """
        while self.running.is_set():
            with self.lock:
                next_pos: Optional[Tuple[int, int]] = self.ghost.move(self.pacman.pos)
                if next_pos and next_pos not in self.positions.values():
                    self.ghost.pos = next_pos
                    self.positions[self.ghost.name] = self.ghost.pos
                    print(f"{self.ghost.name} moved to {self.ghost.pos}")
                    
                    # Check if ghost caught Pac-Man
                    if self.ghost.pos == self.pacman.pos:
                        print(f"{self.ghost.name} caught Pac-Man at {self.ghost.pos}!")
                        if self.on_catch:
                            self.on_catch(self.ghost.name, self.ghost.pos)
                        self.running.clear()
                # else:
                #     print(f"{self.ghost.name} couldn't move to {next_pos}")
            time.sleep(self.move_interval)