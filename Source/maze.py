class Maze:
    def __init__(self, board):
        self.__grid = board
        self.__rows = len(board)
        self.__cols = len(board[0])
        # self.__pacman_pos_x = 0
        # self.__pacman_pos_y = 0
    
                
    def get_neigh(self, pos):
        x, y = pos
        neiboors = []
        if x > 0 and self.__grid[y][x - 1] != '#':
            neiboors.append((x - 1, y))
        if x < self.__cols - 1 and self.__grid[y][x + 1] != '#':
            neiboors.append((x + 1, y))
        if y > 0 and self.__grid[y - 1][x] != '#':
            neiboors.append((x, y - 1))
        if y < self.__rows - 1 and self.__grid[y + 1][x] != '#':
            neiboors.append((x, y + 1))
        return neiboors
    
    def is_wall(self, pos):
        x, y = pos
        return self.__grid[y][x] == '#'
    
    def is_dot(self, pos):
        x, y = pos
        return self.__grid[y][x] == '.'

    def is_big_dot(self, pos):
        x, y = pos
        return self.__grid[y][x] == '*'
    
    def is_gate(self, pos):
        x, y = pos
        return self.__grid[y][x] == 'G'
    
    def is_pacman(self, pos):
        x, y = pos
        return self.__grid[y][x] == 'P'
    
    # def load_pacman(self):
    #     for y in range(self.__rows):
    #         for x in range(self.__cols):
    #             if self.__grid[y][x] == 'P':
    #                 self.__pacman_pos_x = x
    #                 self.__pacman_pos_y = y
    #                 return