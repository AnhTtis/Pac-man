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


class OrangeGhost(Ghost): # Level 3: UCS
    def move(self, pacman_pos):
        path = self.ucs(pacman_pos)
        return path
    
    def ucs(self, target):
        # Initialize the root node and cost
        root = self.pos
        cost = 0
        
        # Initialize the priority queue with the root node
        frontier = [(cost, root, [root])]
        heapq.heapify(frontier)
        
        # Initialize the explored set as empty
        explored = set()
        
        while frontier:
            # Pop the node with the lowest cost from the frontier
            cost, node, path = heapq.heappop(frontier)
            print(f"Visiting: {node}, Current cost: {cost}")
            
            # If the node is the goal, return the solution
            if node == target:
                print(f"Goal reached! Path: {path}")
                return path
            
            # Add the node to the explored set
            explored.add(node)
            
            # For each neighbor of the node
            for neighbor in self.maze.get_neigh(node):
                if neighbor not in explored:
                    # Calculate the cost to move to the neighbor
                    move_cost = self.get_cost(neighbor)
                    total_cost = cost + move_cost
                    
                    # Check if the neighbor is in the frontier with a higher cost
                    in_frontier = False
                    for i, (f_cost, f_node, f_path) in enumerate(frontier):
                        if f_node == neighbor:
                            in_frontier = True
                            if total_cost < f_cost:
                                # Replace the existing node with the neighbor
                                frontier[i] = (total_cost, neighbor, path + [neighbor])
                                heapq.heapify(frontier)
                            break
                    
                    # If the neighbor is not in the frontier, add it to the frontier
                    if not in_frontier:
                        heapq.heappush(frontier, (total_cost, neighbor, path + [neighbor]))
        
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
    
