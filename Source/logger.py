import csv
import os
from typing import Tuple

class ExperimentLogger:
    """Class to log experiment data into a CSV file."""
    
    def __init__(self, filename: str = "experiment_results.csv"):
        """
        Initialize the logger with a CSV filename.

        Args:
            filename: Name of the CSV file to write data into (default: 'experiment_results.csv')
        """
        self.filename = filename
        self.fieldnames = [
            'Ghost_Name', 
            'Algorithm', 
            'Search_Time(s)', 
            'Expanded_Nodes', 
            'Memory_Usage(MB)', 
            'Ghost_Pos_X', 
            'Ghost_Pos_Y', 
            'Pacman_Pos_X', 
            'Pacman_Pos_Y'
        ]
        # Kiểm tra và tạo file với header nếu chưa tồn tại
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writeheader()

    def log(self, 
            ghost_name: str, 
            algorithm: str, 
            search_time: float, 
            expanded_nodes: int, 
            memory_usage: float, 
            ghost_pos: Tuple[int, int], 
            pacman_pos: Tuple[int, int]):
        """
        Log experiment data into the CSV file.

        Args:
            test_case: Identifier for the test case
            ghost_name: Name of the ghost (e.g., "BlueGhost")
            algorithm: Search algorithm used (e.g., "BFS")
            search_time: Time taken for the search (in seconds)
            expanded_nodes: Number of nodes expanded during the search
            memory_usage: Memory used during the search (in bytes, will be converted to MB)
            ghost_pos: Tuple of (x, y) coordinates of the ghost
            pacman_pos: Tuple of (x, y) coordinates of Pac-Man
        """
        memory_usage_mb = memory_usage / 10**6  # Convert bytes to MB
        data = {
            'Ghost_Name': ghost_name,
            'Algorithm': algorithm,
            'Search_Time(s)': f"{search_time:.6f}",
            'Expanded_Nodes': expanded_nodes,
            'Memory_Usage(MB)': f"{memory_usage_mb:.6f}",
            'Ghost_Pos_X': ghost_pos[0],
            'Ghost_Pos_Y': ghost_pos[1],
            'Pacman_Pos_X': pacman_pos[0],
            'Pacman_Pos_Y': pacman_pos[1]
        }
        
        with open(self.filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow(data)

# # Ví dụ sử dụng (có thể xóa khi tích hợp vào code chính)
# if __name__ == "__main__":
#     logger = ExperimentLogger("test_results.csv")
#     logger.log(
#         test_case=1,
#         ghost_name="BlueGhost",
#         algorithm="BFS",
#         search_time=0.002345,
#         expanded_nodes=150,
#         memory_usage=123456,
#         ghost_pos=(1, 2),
#         pacman_pos=(14, 24)
#     )