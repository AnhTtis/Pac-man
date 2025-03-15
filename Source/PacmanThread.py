import threading
import time
from pacman import Pacman

class PacmanThread(threading.Thread):
    def __init__(self, pacman: Pacman, lock: threading.Lock, running: threading.Event):
        super().__init__()
        self.pacman = pacman
        self.lock = lock
        self.running = running
        self.move_interval = 0.2

    def run(self) -> None:
        while self.running.is_set():
            if not self.pacman.paused:
                with self.lock:
                    if self.pacman.direction != "None":
                        self.pacman.move()
            time.sleep(self.move_interval)
