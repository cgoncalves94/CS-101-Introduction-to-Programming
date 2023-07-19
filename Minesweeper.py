class Cell:
    def __init__(self):
        # Cell class constructor. Each cell has four attributes:
        # is_revealed: whether the cell has been revealed by the player.
        # is_flagged: whether the player has placed a flag on the cell.
        # is_mine: whether the cell contains a mine.
        # adjacent_mines: the number of mines in the cells adjacent to this one.
        self.is_revealed = False
        self.is_flagged = False
        self.is_mine = False
        self.adjacent_mines = 0
        
class Board:
    def __init__(self, height, width):
        # Board class constructor. The board has three attributes:
        # height and width: the dimensions of the board.
        # cells: a 2D list of Cell objects that make up the board.
        self.height = height
        self.width = width
        self.cells = []
        for _ in range(height):
            row = []
            for _ in range(width):
                cell = Cell()
                row.append(cell)
            self.cells.append(row)
            
    #class Board methods
    
    def place_mines(self):
        pass
    
    def calculate_adjacent_mines(self):
        pass
    
    def reveal_cell(self):
        pass

    def toogle_flag(self):
        pass
    
    def check_winner(self):
        pass

 #game logic functions 

def game_loop(board):
    pass

def display_board(board):
    pass

