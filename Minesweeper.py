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
        # interate through the cells in the board and randomly swtich attribute is_mine to True
        pass
    
    def get_neighbours(self, i, j):
        # interate through the cells in the board and return a list with the cells objects that are adjacent
        pass
    
    def calculate_adjacent_mines(self):
        # interate through the neighbours list of cells and increment when "is_mine" is True
        pass
    
    def reveal_cell(self, i, j):
        # control flow to reveal what is in the cell (if is bomb or the number of ajacent mines)
        pass

    def toogle_flag(self, i, j):
        # add or remove a flag from the specific cell 
        pass
    
    def check_winner(self):
        # check if all non-revealed cells are bombs, if yes then the game is won
        pass
    
    

 #game logic functions 

def game_loop(board):
    # the main function of the game, where it will ask inputs, display board and message status
    pass

def display_board(board):
    # update the board displayed accordingly to the changes made with a control flow
    pass

