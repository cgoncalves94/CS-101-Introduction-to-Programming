# Building a Minesweeper Game with Python

Welcome to my portfolio project for CS 101: Introduction to Programming! In this project, I've built a fully functional, interactive Minesweeper game that can be played in the terminal.

![Minesweeper Gameplay](https://github.com/cgoncalves94/Minesweeper/blob/main/minesweeper-mine.gif)


## How To Play

Minesweeper is a single-player puzzle game. The game is started on a grid of unrevealed cells. Some randomly selected cells are designated as containing mines. Most cells, however, are devoid of mines. When a cell is revealed, it shows the number of mines that are in the eight cells surrounding it. If none of these eight cells have mines, then they will also be automatically revealed. The game is won when all cells not containing a mine have been revealed.

The interactive feature of the game, powered by Python's `input()` function, allows players to reveal or flag cells, providing a fully interactive game experience right in the terminal.

## Prerequisites

To run this game, you need Python 3.x installed. If you don't have Python installed, you can download it from [here](https://www.python.org/downloads/).

## Installation and Running the Game

1. Clone this repository by copying the URL `https://github.com/cgoncalves94/Minesweeper.git` and using it with your preferred Git client.
2. Once the repository is cloned to your local machine, navigate to the directory containing the `Minesweeper.py` file.
3. To run the game, execute the `Minesweeper.py` file with Python.

## Game Rules

- If a cell containing a mine is revealed, the player loses the game.
- If all cells not containing a mine are revealed, the player wins the game.
- The number on a cell shows the number of mines in the eight cells surrounding it.

In this project, I've used Python's fundamental concepts extensively:

- **Strings**: Used to create user prompts and messages.
- **Control Flow**: `if`, `elif`, and `else` statements control the flow of the game based on user input and game status.
- **Loops**: `For` and `while` loops iterate over cells and control game progress.
- **Lists**: Used to create the game board and handle cells.
- **Functions**: Various functions handle different aspects of the game, from setting up the game to validating user input.
- **Object-Oriented Programming (OOP)**: Defined two classes, `Cell` and `Board`, to encapsulate related data and behaviors.

By using Git for version control, I was able to keep track of my progress and revert back to previous versions when necessary. This project was a great opportunity to practice using the command line for file navigation and running Python scripts.

Feel free to check out the code and try the game for yourself! Don't forget to read my detailed blog post on the project [here](https://dev.to/cgoncalves94/unearthing-logic-and-fun-building-a-minesweeper-game-with-python-5740).


Enjoy the game and happy coding!



