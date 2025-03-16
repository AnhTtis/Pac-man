class Maze:
    def __init__(self, board):
        self.__grid = board
        self.__rows = len(board)
        self.__cols = len(board[0])
                
    def get_neigh(self, pos):
        x, y = pos
        neiboors = []
        if x > 0 and self.__grid[y][x - 1] != '#' and self.__grid[y][x - 1] != '!':
            neiboors.append((x - 1, y))
        if x < self.__cols - 1 and self.__grid[y][x + 1] != '#' and self.__grid[y][x + 1] != '!':
            neiboors.append((x + 1, y))
        if y > 0 and self.__grid[y - 1][x] != '#' and self.__grid[y - 1][x] != '!':
            neiboors.append((x, y - 1))
        if y < self.__rows - 1 and self.__grid[y + 1][x] != '#' and self.__grid[y + 1][x] != '!':
            neiboors.append((x, y + 1))
        return neiboors
    
    def get_rows(self):
        return self.__rows
    
    def get_cols(self):
        return self.__cols
    
    def get_grid(self, rows, cols):
        return self.__grid[rows][cols]
    
    def set_grid(self, rows, cols, value):
        self.__grid[rows][cols] = value

    def is_wall(self, pos):
        x, y = pos
        return self.__grid[y][x] == '#'
    
    def is_not_go(self, pos):
        x, y = pos
        return self.__grid[y][x] == '!'
    
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
    def set_element(self, pos, element):
        x, y = pos
        self.__grid[y][x] = element
        