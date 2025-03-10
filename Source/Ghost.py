from collections import deque
import time
import heapq

class Ghost:
    def __init__(self, maze, start_pos, name):
        self.maze = maze
        self.pos = start_pos
        self.name = name

    def move(self, pacman_pos):
        raise NotImplementedError("This method should be implemented by a subclass")
    
    # def chase(self, pacman, lock, running, position):
    #     while running.is_set():
    #         with lock:
    #             next_pos = self.move(pacman.pos)
    #             if next_pos:
    #                 self.pos = next_pos
    #                 position[self.name] = self.pos
    #         # time.sleep(0.5)           


class BlueGhost(Ghost):  #level 1: BFS
    def move(self, pacman_pos):
        path = self.bfs(pacman_pos)
        if path and len(path) > 1:
            return path[1]

    def bfs(self, target):
        #tuple of (current position, path python list[])
        queue = deque([(self.pos, [self.pos])])
        visited = set([self.pos])
        while queue:
            pos, path = queue.popleft()
            print(pos)
            #is goal?
            if pos == target:
                return path
            
            neighbors = self.maze.get_neigh(pos)
            for next_pos in neighbors:
                if next_pos not in visited:
                    visited.add(next_pos)
                    # adding update the path
                    queue.append((next_pos, path + [next_pos]))
        return None

class PinkGhost(Ghost):  #level 2: DFS
    def move(self, pacman_pos):
        path = self.dfs(pacman_pos)
        return path


    def dfs(self, target):
        stack = [(self.pos, [self.pos])]
        visited = [self.pos]
        
        while stack:
            pos, path = stack.pop()
            print(pos)
            
            if pos == target:
                return path
            
            neighbors = self.maze.get_neigh(pos)
            for next_pos in neighbors:                
                if next_pos not in visited:
                    visited.append(next_pos)
                    stack.append((next_pos, path + [next_pos]))

        return None
    
    
class OrangeGhost(Ghost):  # Level 3: UCS
    def move(self, pacman_pos):
        path = self.ucs(pacman_pos)
        return path
    
    def ucs(self, target):
        # Priority queue stores tuples of (cost, current position, path)
        queue = [(0, self.pos, [self.pos])]
        visited = set()
        
        while queue:
            cost, pos, path = heapq.heappop(queue)
            print(f"Visiting: {pos}, Current cost: {cost}")
            
            # Check if the goal has been reached
            if pos == target:
                print(f"Goal reached! Path: {path}")
                return path
            
            # Skip if the position has already been visited
            if pos not in visited:
                visited.add(pos)
                
                # Explore neighbors
                for next_pos in self.maze.get_neigh(pos):
                    if next_pos not in visited:
                        # Use get_cost to calculate the cost for the next position
                        move_cost = self.get_cost(next_pos)
                        heapq.heappush(queue, (cost + move_cost, next_pos, path + [next_pos]))
        
        # Return None if no path is found
        return None
    
    def get_cost(self, next_pos):
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
    
