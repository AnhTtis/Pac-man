import pygame
from collections import deque
import heapq

class Ghost:
    def __init__(self, maze, pos, name, width, height):
        self.pos = pos #[x, y]
        self.maze = maze
        self.name = name
        self.width = width
        self.height = height
        self.face_left = True
        self.moving = False
        self.appearance = None
    
    def loadImange(self):
        return NotImplementedError("This method should be implemented by a subclass")

    def moveScreen(self, dx, dy):
        if dx != 0:
            self.pos[0] += dx
            if dx > 0 and self.face_left:
                self.face_left = False
            elif dx < 0 and not self.face_left:
                self.face_left = True
        self.pos[1] += dy
        self.moving = not self.moving

    def display(self, screen):
        if self.appearance:
            screen.blit(self.appearance[self.face_left][self.moving], (self.pos[0], self.pos[1]))

    def move(self, pacman_pos):
        raise NotImplementedError("This method should be implemented by a subclass")
    
  
class BlueGhost(Ghost):  # level 1: BFS
    def loadImage(self):
        super().__init__(self.pos, self.width, self.height, (0, 0, 255))
        self.appearance = [
            [pygame.transform.scale(pygame.image.load("blue1_flip.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("blue2_flip.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("blue1.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("blue2.png"), (self.width, self.height))]
        ]

    def move(self, pacman_pos):
        path = self.bfs(pacman_pos)
        if path and len(path) > 1:
            self.moveScreen(path[1][0] - self.pos[0], path[1][1] - self.pos[1])


    def bfs(self, target):
        # tuple of (current position, path python list[])
        queue = deque([(self.pos, [self.pos])])
        visited = set([self.pos])
        while queue:
            pos, path = queue.popleft()
            # print(pos)
            # is goal?
            if pos == target:
                return path
            
            neighbors = self.maze.get_neigh(pos)
            for next_pos in neighbors:
                if next_pos not in visited:
                    visited.add(next_pos)
                    # adding update the path
                    queue.append((next_pos, path + [next_pos]))
        return None

class PinkGhost(Ghost):  # level 2: DFS
    def loadImange(self):
        super().__init__(self.pos, self.width, self.height, (255, 105, 180))
        self.appearance = [
            [pygame.transform.scale(pygame.image.load("pink1_flip.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("pink2_flip.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("pink1.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("pink2.png"), (self.width, self.height))]
        ]

    def move(self, pacman_pos):
        path = self.dfs(pacman_pos)
        if path and len(path) > 1:
            self.moveScreen(path[1][0] - self.pos[0], path[1][1] - self.pos[1])

    def dfs(self, target):
        # tuple of (current position, path python list[])
        stack = [(self.pos, [self.pos])]
        visited = set([self.pos])
        
        while stack:
            pos, path = stack.pop()
            # print(pos)
            
            # is goal?
            if pos == target:
                return path
            
            neighbors = self.maze.get_neigh(pos)
            for next_pos in neighbors:
                if next_pos not in visited:
                    visited.add(next_pos)
                    # adding update the path
                    stack.append((next_pos, path + [next_pos]))

        return None

class OrangeGhost(Ghost): # Level 3: UCS
    def loadImange(self):
        super().__init__(self.pos, self.width, self.height, (255, 255, 0))
        self.appearance = [
            [pygame.transform.scale(pygame.image.load("yellow1_flip.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("yellow2_flip.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("yellow1.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("yellow2.png"), (self.width, self.height))]
        ]

    def move(self, pacman_pos):
        path = self.ucs(pacman_pos)
        if path and len(path) > 1:
            self.moveScreen(path[1][0] - self.pos[0], path[1][1] - self.pos[1])

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
          #print(f"Visiting: {node}, Current cost: {cost}")
            
            # If the node is the goal, return the solution
            if node == target:
               # print(f"Goal reached! Path: {path}")
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


class RedGhost(Ghost): # Level 4: A* search
    def loadImange(self):
        super().__init__(self.pos, self.width, self.height, (255, 0, 0))
        self.appearance = [
            [pygame.transform.scale(pygame.image.load("red1_flip.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("red2_flip.png"), (self.width, self.height))],
            [pygame.transform.scale(pygame.image.load("red1.png"), (self.width, self.height)), pygame.transform.scale(pygame.image.load("red2.png"), (self.width, self.height))]
        ]

    def move(self, pacman_pos):
        path = self.a_star(pacman_pos)
        if path and len(path) > 1:
            self.moveScreen(path[1][0] - self.pos[0], path[1][1] - self.pos[1])

    def a_star(self, target):
        start = self.pos
        
        # The set of discovered nodes that may need to be (re-)expanded.
        openSet = [(self.get_heuristic(start, target), start)]
        heapq.heapify(openSet)
        
        # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from the start to n currently known.
        cameFrom = {}
        
        # For node n, gScore[n] is the currently known cost of the cheapest path from start to n.
        gScore = {start: 0}
        
        # For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to how cheap a path could be from start to finish if it goes through n.
        fScore = {start: self.get_heuristic(start, target)}
        
        while openSet:
            # This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
            current_f, current = heapq.heappop(openSet)
            
            # If the current node is the goal, reconstruct and return the path
            if current == target:
                return self.reconstruct_path(cameFrom, current)
            
            # Explore neighbors
            for neighbor in self.maze.get_neigh(current):
                # d(current, neighbor) is the weight of the edge from current to neighbor
                # tentative_gScore is the distance from start to the neighbor through current
                tentative_gScore = gScore[current] + self.get_cost(neighbor)
                
                if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
                    # This path to neighbor is better than any previous one. Record it!
                    cameFrom[neighbor] = current
                    gScore[neighbor] = tentative_gScore
                    fScore[neighbor] = tentative_gScore + self.get_heuristic(neighbor, target)
                    
                    # If neighbor is not in openSet, add it
                    if neighbor not in [n for _, n in openSet]:
                        heapq.heappush(openSet, (fScore[neighbor], neighbor))
        
        # Open set is empty but goal was never reached
        return None
    
    def reconstruct_path(self, cameFrom, current):
        total_path = [current]
        while current in cameFrom:
            current = cameFrom[current]
            total_path.insert(0, current)
        return total_path
    
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
        
    def get_heuristic(self, pos, target):
        x1, y1 = pos
        x2, y2 = target
        return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance