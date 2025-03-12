import time
import threading
from typing import List, Tuple, Dict, Optional, Callable
import copy
from Maze import Maze 
from Ghost import Ghost, BlueGhost, OrangeGhost, PinkGhost
from GhostThread import GhostThread 
from Pacman import Pacman

class GameManager:
    """Manages the Pac-Man game state and coordinates ghost threads."""
    def __init__(self, maze: Maze, pacman: 'Pacman', 
                 ghosts: List[Ghost], positions: Dict[str, Tuple[int, int]]):
        """
        Initialize the game manager with maze, Pac-Man, and ghost configurations.

        Args:
            maze: The maze object representing the game grid
            pacman_start: Tuple of (x, y) coordinates for Pac-Man's starting position
            ghosts: List of Ghost objects (e.g., BlueGhost, PinkGhost)
            positions: Dictionary mapping ghost names to their current positions
        """
        self.maze: Maze = copy.deepcopy(maze)
        self.pacman: Pacman = pacman
        self.ghosts: List[Ghost] = copy.deepcopy(ghosts)
        self.positions: Dict[str, Tuple[int, int]] = copy.deepcopy(positions)
    
        # Initialize ghost threads
        self.lock: threading.Lock = threading.Lock()
        self.running: threading.Event = threading.Event()
        self.running.set()
        self.on_catch: Optional[Callable[[str, Tuple[int, int]], None]] = None
        self.threads: List[GhostThread] = [GhostThread(ghost, self.pacman, self.lock, self.running, self.positions, self.on_catch) for ghost in ghosts]


    def is_running(self) -> bool:
        """
        Check if the game is currently running.

        Returns:
            True if the game is running, False otherwise
        """
        return self.running.is_set()
    
    def start(self):
        """
        Start the game by starting all ghost threads.
        """
        for t in self.threads:
            t.start()

    def get_pacman_pos(self) -> Tuple[int, int]:
        """
        Get the current position of Pac-Man.

        Returns:
            Tuple of (x, y) coordinates representing Pac-Man's position
        """
        return self.pacman.pos

    def move_pacman(self, direction: str) -> None:
        """
        Move Pac-Man in the specified direction.

        Args:
            direction: String representing the direction ("up", "down", "left", "right")
        """
        self.pacman.move(direction)

    def stop(self) -> None:
        """
        Stop the game and wait for all ghost threads to terminate.
        """
        self.running.clear()
        for t in self.threads:
            t.join()