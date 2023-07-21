import random
import os
import time

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
    
    def place_mines(self, num_mines):
        # Using list comprehension, flatten the 2D list of cells into a 1D list
        all_cells = [cell for row in self.cells for cell in row]

        # Randomly select cells to be mines
        mines = random.sample(all_cells, num_mines)

        # Set the selected cells to be mines
        for mine in mines:
            mine.is_mine = True

    def get_neighbours(self, i, j):
        # Create an empty list for the neighbours
        neighbours = []

        # Iterate over the positions of the neighbour cells
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                # Check if each position is valid and is not the cell itself
                if 0 <= x < self.height and 0 <= y < self.width and (x, y) != (i, j):
                    # Add the neighbour cell to the list
                    neighbours.append(self.cells[x][y])

        # Return the list of neighbours
        return neighbours
    
    def calculate_adjacent_mines(self):
        # interate through the list of cells 
        for i in range(self.height):
            for j in range(self.width):
                # Get the current cell and its neighbours
                cell = self.cells[i][j]
                neighbours = self.get_neighbours(i, j)
                
                # Initialize a counter for the mines
                mines = 0

                # Iterate over each neighbour
                for neighbour in neighbours:
                    # If the neighbour is a mine, increment the counter
                    if neighbour.is_mine:
                        mines += 1

                # Set the number of adjacent mines for the current cell
                cell.adjacent_mines = mines
            
    def reveal_cell(self, i, j):
        # Check if i and j are within the valid range of indices
        if not (0 <= i < self.height and 0 <= j < self.width):
            print("Invalid coordinates! Please enter coordinates within the board.")
            return
        
        # Get the cell
        cell = self.cells[i][j]
        
        # If the cell is flagged, print a message and return
        if cell.is_flagged:
            print("This cell is flagged. Unflag it before revealing.")
            return None

        # Only reveal the cell if it's not already revealed
        if not cell.is_revealed:
            cell.is_revealed = True

            # If the cell is a mine, the game ends
            if cell.is_mine:
                return False

            # If the cell has no adjacent mines, reveal all its neighbours
            if cell.adjacent_mines == 0:
                neighbours = self.get_neighbours(i, j)
                for neighbour in neighbours:
                    neighbour.is_revealed = True
        else:
            print("Cell already revealed!")
        
        # If the function execution reaches this point, it means that a cell was successfully revealed and it was not a mine.
        # Therefore, return True to indicate that the game should continue.
        return True

    def toogle_flag(self, i, j):
        # Check if i and j are within the valid range of indices
        if not (0 <= i < self.height and 0 <= j < self.width):
            print("Invalid coordinates! Please enter coordinates within the board.")
            return
        
        # Get the cell
        cell = self.cells[i][j]
        
        if not cell.is_revealed:
            # If the cell is flagged, unflag it, otherwise flag it
            if cell.is_flagged:
                cell.is_flagged = False
            else:
                cell.is_flagged = True
        else:
            print("Cell already revealed!")
            

    def check_win(self):
        # Iterate over all cells
        for i in range(self.height):
            for j in range(self.width):
                cell = self.cells[i][j]
                # If the cell is not a mine and has not been revealed, return False
                if not cell.is_mine and not cell.is_revealed:
                    return False

        # If all non-mine cells have been revealed, return True
        print("GAME WON!")
        return True

    
 #game logic functions 

def game():
    # Clear the terminal and set up the game
    clear_terminal()
    width, height, mines = setup_game()

    # Create the board
    board = Board(width, height)
    
    # Place mines and calculate the number of adjacent mines for all cells
    board.place_mines(mines)
    board.calculate_adjacent_mines()
    
    # Display board and run game until win or loss
    display_board(board)
    run_game(board, width, height)

def setup_game():
    # Ask the player for the difficulty level and set the board size and mine count based on the difficulty
    difficulty = input("Enter difficulty (easy, medium, hard): ").lower()
    if difficulty == "easy":
        return 9, 9, 10
    elif difficulty == "medium":
        return 16, 16, 40
    elif difficulty == "hard":
        return 30, 16, 99
    else:
        print("Invalid difficulty! Defaulting to easy.")
        return 9, 9, 10

def run_game(board, width, height):
    while not board.check_win():
        # Get the player's move
        action, row, column = get_move(width, height)
        # Perform the move
        if action == "reveal":
            game_continues = board.reveal_cell(row, column)
            if game_continues is False:
                clear_terminal()
                display_board(board)
                print("\nGAME OVER")
                break
            elif game_continues is True:  # only redraw if a cell was revealed
                time.sleep(1)  # delay for 1 second
                clear_terminal()
                display_board(board)
        elif action == "flag":
            board.toogle_flag(row, column)
            time.sleep(1)  # delay for 1 second
            clear_terminal()
            display_board(board)

def get_move(width, height):
    while True:
        # Ask the user for their move
        move = input("\nEnter your move (format: reveal/flag, row number, column): ")
        # Validate and parse the move
        parts = move.split()
        if len(parts) == 3:
            action, row, column = parts[0].lower(), parts[1], parts[2].upper()
            if validate_move(action, row, column, width, height):
                return action, int(row), ord(column) - ord('A')
        print("Invalid input! Please enter your move in the format: action row column")

def validate_move(action, row, column, width, height):
    if action in ("reveal", "flag") and row.isdigit() and 0 <= int(row) <= height and \
        column.isalpha() and 'A' <= column <= chr(ord('A') + width - 1):
        return True
    return False
  
def display_board(self):
    # Create the column labels
    column_labels = ' '.join(chr(i + ord('A')) for i in range(self.width))
    
    # Calculate the number of digits in the highest row number
    num_digits = len(str(self.height))
    
    # Print the column labels with the right spacing
    print(" " * num_digits + " " + column_labels)

    # Iterate over each row in the board
    for i, row in enumerate(self.cells):
        # Print the row label with the right spacing
        print(str(i + 0).rjust(num_digits), end=' ')
        
        # Iterate over each cell in the row
        for j, cell in enumerate(row):
            # Call a helper function to get the character to display for the cell
            print(get_cell_character(cell), end=' ' if j < len(row) - 1 else '\n')
        
def get_cell_character(cell):
    # Check if the cell is revealed
    if cell.is_revealed:
        # If the cell is a mine, return 'M'
        if cell.is_mine:
            return 'M'
        # If the cell is not a mine, return '-'
        else:
            return cell.adjacent_mines
    # If the cell is not revealed
    else:
        # If the cell is flagged, return 'F'
        if cell.is_flagged:
            return 'F'
        # If the cell is not flagged, return '-'
        else:
            return '-'
        
def clear_terminal():
    if os.name == 'posix':  # Linux or Mac
        print('\033c')
    elif os.name == 'nt':  # Windows
        print('\033[2J')


game()