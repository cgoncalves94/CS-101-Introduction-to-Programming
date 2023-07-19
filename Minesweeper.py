class Cell:
    def __init__(self):
        self.is_revealed = False
        self.is_flagged = False
        self.is_mine = False
        self.adjacent_mines = 0
        
class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = []
        for _ in range(height):
            row = []
            for _ in range(width):
                cell = Cell()
                row.append(cell)
            self.cells.append(row)

            
board = Board(5,5)
print(board.cells[0][0].is_revealed)
