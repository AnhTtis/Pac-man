from collections import deque
from typing import List, Tuple, Dict, Set, Optional
import heapq
from maze import Maze
import time
import sys
from logger import ExperimentLogger

class Ghost:
    """Base class for Pac-Man ghost AI behaviors."""
    def __init__(self, maze: 'Maze', start_pos: Tuple[int, int], name: str, size:int):
        """
        Initialize a ghost with its maze, starting position, and name.

        Args:
            maze: The maze object containing the game grid and utility methods
            start_pos: Tuple of (x, y) coordinates for the ghost's starting position
            name: Name of the ghost (e.g., "Blinky", "Pinky")
        """
        self.maze = maze
        self.maze_weighed_grid = [
            ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#'],
            ['#','4','3','#','3','1','2','2','3','2','#','4','#','2','4','4','#','#','1','1','1','#','#','1','1','4','4','2','2','#'],
            ['#','1','1','#','4','1','1','#','3','1','#','3','#','4','#','1','2','3','3','3','2','3','2','1','2','2','2','2','3','#'],
            ['#','3','2','#','#','#','3','#','1','4','1','2','#','1','#','#','4','#','#','3','#','#','3','#','3','#','2','#','#','#'],
            ['#','3','3','4','2','2','3','#','#','#','4','3','4','3','1','#','4','1','#','1','1','3','1','#','4','#','2','4','1','#'],
            ['#','1','1','#','#','#','3','3','4','#','#','#','#','3','#','#','1','#','#','3','#','#','1','#','4','#','3','2','1','#'],
            ['#','3','4','2','1','1','1','2','1','4','4','4','3','2','1','1','2','4','3','2','#','3','3','2','3','#','#','#','4','#'],
            ['#','3','3','#','#','#','#','1','#','#','3','#','4','#','3','#','4','#','#','2','4','1','1','#','#','#','2','2','2','#'],
            ['#','4','2','#','2','4','3','3','4','3','2','#','4','#','3','#','3','#','#','4','#','#','4','2','3','#','3','1','1','#'],
            ['#','3','1','3','2','#','1','3','#','2','4','3','3','4','3','#','1','3','3','1','3','4','4','2','1','4','3','3','2','#'],
            ['#','#','#','#','1','#','#','3','#','3','4','#','#','1','3','#','2','#','2','#','2','#','3','#','#','2','2','#','3','#'],
            ['#','3','2','1','4','1','1','4','#','#','1','#','#','4','#','#','4','#','#','#','2','#','3','#','2','3','4','#','1','#'],
            ['#','3','#','#','3','1','#','2','2','#','3','1','1','1','3','1','3','4','2','3','1','#','3','#','2','#','#','#','3','#'],
            ['#','1','4','2','3','2','#','1','4','#','3','#','#','#','1','4','#','#','#','2','1','1','4','#','1','2','4','4','3','#'],
            ['#','#','#','#','2','1','#','3','#','#','3','#','4','2','2','4','4','3','#','4','#','#','2','#','#','#','#','2','#','#'],
            ['#','3','4','3','3','4','2','1','2','1','1','4','2','1','1','1','3','2','4','2','2','2','4','2','4','4','1','2','2','#'],
            ['#','#','#','2','#','#','#','2','#','#','2','#','3','3','3','2','4','1','#','3','3','4','2','#','#','#','#','1','#','#'],
            ['#','3','#','3','#','3','2','2','#','2','2','#','#','#','4','4','#','#','#','1','#','#','3','#','3','#','1','4','1','#'],
            ['#','1','3','1','#','1','#','4','#','#','1','4','3','3','3','3','2','4','4','1','2','3','4','1','3','#','#','4','3','#'],
            ['#','3','3','4','#','1','#','2','4','3','4','#','#','#','#','#','#','#','2','3','#','#','#','3','3','2','4','3','2','#'],
            ['#','1','#','#','#','#','#','4','2','#','2','#','1','1','4','2','4','#','#','4','#','1','#','1','#','#','#','#','1','#'],
            ['#','1','2','2','4','3','2','3','3','#','3','3','3','4','#','#','1','3','3','2','1','1','1','1','4','2','4','4','1','#'],
            ['#','4','2','#','#','#','#','1','#','#','#','#','#','4','4','#','1','#','4','4','#','#','3','#','#','#','#','3','#','#'],
            ['#','3','4','#','3','4','3','2','4','1','3','3','#','2','#','#','1','#','#','4','4','#','1','2','4','1','#','3','2','#'],
            ['#','2','1','4','3','#','#','#','1','4','4','2','1','4','3','4','2','1','3','2','3','2','1','#','3','4','1','4','4','#'],
            ['#','1','#','#','4','1','1','#','4','#','2','#','3','#','#','1','2','#','4','3','#','#','1','#','1','1','2','#','3','#'],
            ['#','2','#','1','3','#','#','#','2','#','1','#','2','4','#','2','#','#','3','1','#','1','3','#','3','#','#','#','4','#'],
            ['#','2','#','3','4','4','4','4','3','#','4','4','4','1','2','3','1','1','1','3','#','4','3','#','2','#','3','1','3','#'],
            ['#','2','#','#','#','#','#','#','#','#','4','#','#','2','#','#','4','#','3','1','#','3','4','3','1','#','#','4','3','#'],
            ['#','2','1','2','1','4','1','1','1','1','2','4','1','3','2','4','2','2','2','2','3','4','#','#','1','3','4','3','3','#'],
            ['#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#','#']]
        self.pos = start_pos
        self.name = name
        self.size = size
        self.face_right = False
        self.appearance = None
        self.path: List[Tuple[int, int]] = []
        self.first_move = False
        self.searched_nodes = 0
        self.searched_time = 0.0
        self.searched_memory = 0.0
        # self.paused = False
        self.logger = ExperimentLogger()
    
    def show_search_statistics(self):
        """
        Display the search performance statistics.
        """
        memory_usage_mb = self.searched_memory / 10**6  # Convert memory usage to MB
        print(f"Search Time: {self.searched_time:.6f} seconds")
        print(f"Memory Usage: {memory_usage_mb:.6f} MB")
        print(f"Expanded Nodes: {self.searched_nodes}")

    
        
    def load_image(self, pygame):
        # load the image of the ghost
        pass

    def find_path(self, pacman_pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        """
        Calculate the next position for the ghost to move towards Pac-Man.

        Args:
            pacman_pos: Tuple of (x, y) coordinates of Pac-Man's current position

        Returns:
            Tuple of (x, y) coordinates for the next move, or None if no move possible
        """
        raise NotImplementedError("This method should be implemented by a subclass")
    
    def display(self, screen):
        if self.appearance:
            screen.blit(self.appearance[self.face_right], (self.pos[0] * self.size[0], self.pos[1] * self.size[1]))

    def set_pos(self, pos: Tuple[int, int]) -> None:
        """
        Set the ghost's position to a new (x, y) coordinate.

        Args:
            pos: Tuple of (x, y) coordinates for the new position
        """
        
        if pos[0] > self.pos[0] and not self.face_right:
                self.face_right = True
        elif pos[0] != self.pos[0] and self.face_right:
            self.face_right = False
        
        self.pos = pos
        
class BlueGhost(Ghost):
    """Ghost that uses Breadth-First Search to chase Pac-Man."""
    
    def find_path(self, pacman_pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        self.logger.log(
            ghost_name=self.name,
            algorithm="BFS",
            search_time=self.searched_time,
            expanded_nodes=self.searched_nodes,
            memory_usage=self.searched_memory,
            ghost_pos=self.pos,
            pacman_pos=pacman_pos
        )
        if not self.path or self.path[-1] != pacman_pos:
            if not self.first_move:
                self.first_move = True
            else:
                self.path = self.bfs(pacman_pos) or []
        return None
    
    def load_image(self, pygame):
        self.appearance = [pygame.transform.scale(pygame.image.load("Source/ghosts/blue.png"), self.size)]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))
    

    def bfs(self, target: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        self.n_expanded_nodes = 0
        """
        Perform Breadth-First Search to find a path to the target.

        Args:
            target: Tuple of (x, y) coordinates to reach (Pac-Man's position)

        Returns:
            List of (x, y) tuples representing the path, or None if no path found
        """
        start_time = time.time()
        queue: deque[Tuple[Tuple[int, int], List[Tuple[int, int]]]] = deque([(self.pos, [self.pos])])
        visited: Set[Tuple[int, int]] = set([self.pos])
        expanded_nodes = 0
        max_memory = 0
        while queue:
            pos, path = queue.popleft()
            expanded_nodes += 1
            # Measure the size of the containers and the elements they reference
            current_memory_usage = sys.getsizeof(queue) + sum(sys.getsizeof(item) for item in queue)
            current_memory_usage += sys.getsizeof(visited) + sum(sys.getsizeof(item) for item in visited)
            current_memory_usage += sys.getsizeof(path) + sum(sys.getsizeof(item) for item in path)
            max_memory = max(max_memory, current_memory_usage)
        
            if pos == target:
                end_time = time.time()
                self.searched_time = end_time - start_time
                self.searched_nodes = expanded_nodes
                self.searched_memory = max_memory
                return path
            
            neighbors = self.maze.get_neigh(pos)
            for next_pos in neighbors:
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, path + [next_pos]))
        end_time = time.time()
        self.searched_time = end_time - start_time
        self.searched_nodes = expanded_nodes
        self.searched_memory = max_memory
        return None

class PinkGhost(Ghost):
    """Ghost that uses Depth-First Search to chase Pac-Man."""
    def find_path(self, pacman_pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        if not self.path or self.path[-1] != pacman_pos:
            if not self.first_move:
                self.first_move = True
            else:
                self.path = self.dfs(pacman_pos) or []
        self.logger.log(
            ghost_name=self.name,
            algorithm="DFS",
            search_time=self.searched_time,
            expanded_nodes=self.searched_nodes,
            memory_usage=self.searched_memory,
            ghost_pos=self.pos,
            pacman_pos=pacman_pos
        )
        return None
    
    def load_image(self, pygame):
        self.appearance = [pygame.transform.scale(pygame.image.load("Source/ghosts/pink.png"), self.size)]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))

    def dfs(self, target: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        """
        Perform Depth-First Search to find a path to the target.

        Args:
            target: Tuple of (x, y) coordinates to reach (Pac-Man's position)

        Returns:
            List of (x, y) tuples representing the path, or None if no path found
        """
        start_time = time.time()
        stack: List[Tuple[Tuple[int, int], List[Tuple[int, int]]]] = [(self.pos, [self.pos])]
        visited: Set[Tuple[int, int]] = set([self.pos])
        expanded_nodes = 0
        max_memory = 0
        
        while stack:
            pos, path = stack.pop()
            expanded_nodes += 1
            
            # Measure the size of the containers and the elements they reference
            current_memory_usage = sys.getsizeof(stack) + sum(sys.getsizeof(item) for item in stack)
            current_memory_usage += sys.getsizeof(visited) + sum(sys.getsizeof(item) for item in visited)
            current_memory_usage += sys.getsizeof(path) + sum(sys.getsizeof(item) for item in path)
            max_memory = max(max_memory, current_memory_usage)
            
            if pos == target:
                end_time = time.time()
                self.searched_time = end_time - start_time
                self.searched_nodes = expanded_nodes
                self.searched_memory = max_memory
                return path
            
            neighbors = self.maze.get_neigh(pos)
            for next_pos in neighbors:
                if next_pos not in visited:
                    visited.add(next_pos)
                    stack.append((next_pos, path + [next_pos]))
        end_time = time.time()
        self.searched_time = end_time - start_time
        self.searched_nodes = expanded_nodes
        self.searched_memory = max_memory
        return None

class OrangeGhost(Ghost):
    """Ghost that uses Uniform Cost Search to chase Pac-Man."""
    def find_path(self, pacman_pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        if not self.path or self.path[-1] != pacman_pos:
            if not self.first_move:
                self.first_move = True
            else:
                self.path = self.ucs(pacman_pos) or []
        self.logger.log(
            ghost_name=self.name,
            algorithm="UCS",
            search_time=self.searched_time,
            expanded_nodes=self.searched_nodes,
            memory_usage=self.searched_memory,
            ghost_pos=self.pos,
            pacman_pos=pacman_pos
        )
        return None
    
    def load_image(self, pygame):
        self.appearance = [pygame.transform.scale(pygame.image.load("Source/ghosts/yellow.png"), self.size)]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))

    def ucs(self, target: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        """
        Perform Uniform Cost Search to find a path to the target.

        Args:
            target: Tuple of (x, y) coordinates to reach (Pac-Man's position)

        Returns:
            List of (x, y) tuples representing the path, or None if no path found
        """
        start_time = time.time()
        root = self.pos
        cost = 0
        frontier: List[Tuple[float, Tuple[int, int], List[Tuple[int, int]]]] = [(cost, root, [root])]
        heapq.heapify(frontier)
        explored: Set[Tuple[int, int]] = set()
        expanded_nodes = 0
        max_memory = 0
        
        while frontier:
            cost, node, path = heapq.heappop(frontier)
            expanded_nodes += 1
            
            # Measure the size of the containers and the elements they reference
            current_memory_usage = sys.getsizeof(frontier) + sum(sys.getsizeof(item) for item in frontier)
            current_memory_usage += sys.getsizeof(explored) + sum(sys.getsizeof(item) for item in explored)
            current_memory_usage += sys.getsizeof(path) + sum(sys.getsizeof(item) for item in path)
            max_memory = max(max_memory, current_memory_usage)
            
            if node == target:
                end_time = time.time()
                self.searched_time = end_time - start_time
                self.searched_nodes = expanded_nodes
                self.searched_memory = max_memory
                return path
            
            explored.add(node)
            for neighbor in self.maze.get_neigh(node):
                if neighbor not in explored:
                    move_cost = self.get_cost(node, neighbor)
                    total_cost = cost + move_cost
                    
                    in_frontier = False
                    for i, (f_cost, f_node, f_path) in enumerate(frontier):
                        if f_node == neighbor:
                            in_frontier = True
                            if total_cost < f_cost:
                                frontier[i] = (total_cost, neighbor, path + [neighbor])
                                heapq.heapify(frontier)
                            break
                    
                    if not in_frontier:
                        heapq.heappush(frontier, (total_cost, neighbor, path + [neighbor]))
        end_time = time.time()
        self.searched_time = end_time - start_time
        self.searched_nodes = expanded_nodes
        self.searched_memory = max_memory
        return None
    
    def get_cost(self, current_pos: Tuple[int, int], next_pos: Tuple[int, int]) -> float:
        """
        Calculate the cost of moving to the next position based on the weighed maze.

        Args:
            current_pos: Tuple of (x, y) coordinates of the current position
            next_pos: Tuple of (x, y) coordinates of the next position

        Returns:
            Float representing the movement cost
        """
        if self.maze.is_wall(next_pos):
            return float('inf')  # Impassable
        current_weight = int(self.maze_weighed_grid[current_pos[1]][current_pos[0]])
        next_weight = int(self.maze_weighed_grid[next_pos[1]][next_pos[0]])
        return abs(next_weight - current_weight) + 1
 

class RedGhost(Ghost):
    """Ghost that uses A* Search to chase Pac-Man."""
    def find_path(self, pacman_pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        if not self.path or self.path[-1] != pacman_pos:
            if not self.first_move:
                self.first_move = True
            else:
                self.path = self.a_star(pacman_pos) or []
        self.logger.log(
            ghost_name=self.name,
            algorithm="A*",
            search_time=self.searched_time,
            expanded_nodes=self.searched_nodes,
            memory_usage=self.searched_memory,
            ghost_pos=self.pos,
            pacman_pos=pacman_pos
        )
        return None

    def load_image(self, pygame):
        self.appearance = [pygame.transform.scale(pygame.image.load("Source/ghosts/red.png"), self.size)]
        self.appearance.append(pygame.transform.flip(self.appearance[0], True, False))
    
    def a_star(self, target: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
        """
        Perform A* Search to find an optimal path to the target.

        Args:
            target: Tuple of (x, y) coordinates to reach (Pac-Man's position)

        Returns:
            List of (x, y) tuples representing the path, or None if no path found
        """
        start_time = time.time()
        start = self.pos
        openSet: List[Tuple[float, Tuple[int, int]]] = [(self.get_heuristic(start, target), start)]
        heapq.heapify(openSet)
        cameFrom: Dict[Tuple[int, int], Tuple[int, int]] = {}
        gScore: Dict[Tuple[int, int], float] = {start: 0}
        fScore: Dict[Tuple[int, int], float] = {start: self.get_heuristic(start, target)}
        expanded_nodes = 0
        max_memory = 0
        
        while openSet:
            current_f, current = heapq.heappop(openSet)
            expanded_nodes += 1
            
            # Measure the size of the containers and the elements they reference
            current_memory_usage = sys.getsizeof(openSet) + sum(sys.getsizeof(item) for item in openSet)
            current_memory_usage += sys.getsizeof(cameFrom) + sum(sys.getsizeof(item) for item in cameFrom)
            current_memory_usage += sys.getsizeof(gScore) + sum(sys.getsizeof(item) for item in gScore)
            current_memory_usage += sys.getsizeof(fScore) + sum(sys.getsizeof(item) for item in fScore)
            max_memory = max(max_memory, current_memory_usage)
            
            if current == target:
                end_time = time.time()
                self.searched_time = end_time - start_time
                self.searched_nodes = expanded_nodes
                self.searched_memory = max_memory
                return self.reconstruct_path(cameFrom, current)
            
            for neighbor in self.maze.get_neigh(current):
                tentative_gScore = gScore[current] + self.get_cost(neighbor)
                if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = tentative_gScore + self.get_heuristic(neighbor, target)
                    if neighbor not in [n for _, n in openSet]:
                        heapq.heappush(openSet, (fScore[neighbor], neighbor))
        end_time = time.time()
        self.searched_time = end_time - start_time
        self.searched_nodes = expanded_nodes
        self.searched_memory = max_memory
        return None
    
    def reconstruct_path(self, cameFrom: Dict[Tuple[int, int], Tuple[int, int]], 
                        current: Tuple[int, int]) -> List[Tuple[int, int]]:
        """
        Reconstruct the path from the start to the target using the cameFrom map.

        Args:
            cameFrom: Dictionary mapping each node to its predecessor
            current: The target node to start reconstruction from

        Returns:
            List of (x, y) tuples representing the full path
        """
        total_path = [current]
        while current in cameFrom:
            current = cameFrom[current]
            total_path.insert(0, current)
        return total_path
    
    def get_cost(self, next_pos: Tuple[int, int]) -> float:
        """
        Calculate the cost of moving to a position based on maze features.

        Args:
            next_pos: Tuple of (x, y) coordinates to evaluate

        Returns:
            Float representing the movement cost (inf for walls)
        """
        if self.maze.is_wall(next_pos):
            return float('inf')  # Impassable
        elif self.maze.is_big_dot(next_pos):
            return 0.5  # Lower cost for big dots
        elif self.maze.is_gate(next_pos):
            return 2  # Higher cost for gates
        elif self.maze.is_dot(next_pos):
            return 1  # Regular cost for dots
        else:
            return 1  # Default cost for other positions
        
    def get_heuristic(self, pos: Tuple[int, int], target: Tuple[int, int]) -> float:
        """
        Calculate the Manhattan distance heuristic between two positions.

        Args:
            pos: Current position as (x, y) tuple
            target: Target position as (x, y) tuple

        Returns:
            Float representing the estimated cost to reach the target
        """
        x1, y1 = pos
        x2, y2 = target
        return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance