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

Clone the repository and install via pip using the provided setup script.

### Standard Installation

```bash
git clone https://github.com/loryzeta33/tic_tac_toe.git
cd tic_tac_toe
pip install .
```

## Development Setup

For development and testing, it is recommended to install the package in editable mode so that source code changes are immediately reflected.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/loryzeta33/tic_tac_toe.git
   cd tic_tac_toe
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the package in editable mode:**

   ```bash
   pip install -e .
   ```

4. **Run the tests:**

   ```bash
   python -m unittest discover -s tests
   ```

Installing in editable mode ensures that the package (located in the `src/tic_tac_toe/` folder) is correctly added to the Python path, allowing tests to import the module without issues.

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

After installing in editable mode as shown in the Development Setup, run:

```bash
python -m unittest discover -s tests
```

This command will discover and run all tests in the `tests/` directory.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
