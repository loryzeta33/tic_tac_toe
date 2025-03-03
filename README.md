# Tic Tac Toe

A minimal and flexible Tic Tac Toe game implementation in Python.

## Overview

This package provides two main classes:

- **TicTacToeMatch** – Manages a single match of Tic Tac Toe (game board, moves, winner detection).
- **TicTacToeGame** – Manages a game session with score tracking and customizable starting-player policies.

## Features

- Fully documented and PEP8 compliant code.
- Customizable starting player policy (default: alternating players).
- Basic error handling and board state management.
- Unit tests to ensure proper functionality.

## Installation

Clone the repository and install via pip (if using `setup.py`):

```bash
git clone https://github.com/loryzeta33/tic_tac_toe.git
cd tic_tac_toe
pip install .
```

Alternatively, if using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

A simple example:

```python
from tic_tac_toe.game import TicTacToeGame, PLAYER_ONE, PLAYER_TWO

game = TicTacToeGame()
print("Initial board:")
print(game.match)

# Simulate some moves:
moves = [0, 3, 1, 4, 2]  # This should make PLAYER_ONE win (top row)
for move in moves:
    result = game.play(move)
    print(game.match)
    if result is not None:
        print(f"Winner: {'Tie' if result == 0 else 'Player ' + str(result)}")
        break

print("Scores:", game)
```

## Running Tests

Tests are provided using Python's `unittest` framework. To run them, execute:

```bash
python -m unittest discover -s tests
```

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
