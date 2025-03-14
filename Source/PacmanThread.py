import threading
import time
from Pacman import Pacman

class PacmanThread(threading.Thread):
    def __init__(self, pacman: Pacman, lock: threading.Lock, running: threading.Event):
        super().__init__()
        self.pacman = pacman
        self.lock = lock
        self.running = running
        self.move_interval = 0.2

    def run(self) -> None:
        last_move_time = time.time()
        while self.running.is_set():
            current_time = time.time()
            if current_time - last_move_time >= self.move_interval:
                with self.lock:
                    if self.pacman.direction != "None":
                        self.pacman.move()  # Move Pac-Man based on current direction
                last_move_time = current_time
            time.sleep(0.001)  # 1ms sleep to yield control