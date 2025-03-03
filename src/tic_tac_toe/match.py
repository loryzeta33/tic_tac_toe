# TicTacToeMatch.py

PLAYER_ONE = 1
PLAYER_TWO = 2
EMPTY = 0


class TicTacToeMatch:
    """
    Class representing a Tic Tac Toe match.

    Attributes:
        board (list[int]): A list of 9 integers representing the game board.
        current_player (int): The current player (PLAYER_ONE or PLAYER_TWO).
        winner (int | None): The winner (PLAYER_ONE, PLAYER_TWO, or 0 for a tie; None if the game is ongoing).
    """

    def __init__(self, player: int = PLAYER_ONE) -> None:
        self.board = [EMPTY for _ in range(9)]
        self.current_player = player
        self.winner = None

    def update(self, pos: int) -> None:
        """
        Updates the board with the current player's move.

        Args:
            pos (int): Position (0-8) where to place the move.

        Raises:
            ValueError: If the game is already over, or if the position is invalid or already taken.
        """
        if self.winner is not None:
            raise ValueError("Game is over")
        if pos < 0 or pos > 8:
            raise ValueError("Invalid position: choose a number between 0 and 8")
        if self.board[pos] != EMPTY:
            raise ValueError("Position already taken")

        self.board[pos] = self.current_player
        self.check_winner()
        # Change turn only if the game is still in progress
        if self.winner is None:
            self.current_player = PLAYER_TWO if self.current_player == PLAYER_ONE else PLAYER_ONE

    def check_winner(self) -> None:
        """
        Checks for a winner or a tie on the board.
        """
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != EMPTY:
                self.winner = self.board[a]
                return
        if EMPTY not in self.board:
            self.winner = 0  # 0 indicates a tie

    def get_current_player(self) -> int:
        """
        Returns the current player's identifier.
        """
        return self.current_player

    def reset(self) -> None:
        """
        Resets the match to the initial state.
        Alternates the starting player.
        """
        self.board = [EMPTY for _ in range(9)]
        self.winner = None
        self.current_player = PLAYER_TWO if self.current_player == PLAYER_ONE else PLAYER_ONE

    def __str__(self) -> str:
        """
        Returns a string representation of the game board.
        """
        symbols = {EMPTY: ' ', PLAYER_ONE: 'X', PLAYER_TWO: 'O'}
        board_lines = []
        for i in range(3):
            row = " | ".join(symbols[self.board[j]] for j in range(i * 3, (i + 1) * 3))
            board_lines.append(row)
        return "\n--+---+--\n".join(board_lines)

    def __eq__(self, other: object) -> bool:
        """
        Checks equality between two TicTacToeMatch instances.
        """
        if not isinstance(other, TicTacToeMatch):
            return NotImplemented
        return (self.board == other.board and
                self.current_player == other.current_player and
                self.winner == other.winner)
