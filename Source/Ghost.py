from collections import deque
import heapq

class Ghost:
    def __init__(self, maze, start_pos):
        self.maze = maze
        self.pos = start_pos
    
    def move(self, pacman_pos):
        raise NotImplementedError("This method should be implemented by a subclass")
    
class BlueGhost(Ghost):  #level 1: BFS
    def move(self, pacman_pos):
        path = self.bfs(pacman_pos)
        return path

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
            for next_pos in self.maze.get_neigh(pos):
                if next_pos not in visited:
                    visited.add(next_pos)
                    # adding update the path
                    queue.append((next_pos, path + [next_pos]))
        return None
    
    