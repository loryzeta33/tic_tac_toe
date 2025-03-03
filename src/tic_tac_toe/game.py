# TicTacToeGame.py

from random import choice
from tic_tac_toe.match import TicTacToeMatch, PLAYER_ONE, PLAYER_TWO


def default_starting_player_policy(current_player: int) -> int:
    """
    Default policy that alternates the starting player.
    Returns PLAYER_TWO if the current player is PLAYER_ONE, and vice versa.
    """
    return PLAYER_TWO if current_player == PLAYER_ONE else PLAYER_ONE


class TicTacToeGame:
    """
    Class representing a Tic Tac Toe game session with score tracking.

    Attributes:
        match (TicTacToeMatch): The current match.
        current_starting_player (int): The player who starts the current match.
        scores (list[int]): List tracking the scores for each player.
                              Index 0 is for PLAYER_ONE, index 1 for PLAYER_TWO.
        starting_player_policy (Callable[[int], int]): Function determining the starting player for each match.
    """

    def __init__(self, player: int = None, starting_player_policy=default_starting_player_policy) -> None:
        if player is None:
            player = choice([PLAYER_ONE, PLAYER_TWO])
        self.current_starting_player = player
        self.starting_player_policy = starting_player_policy
        self.match = TicTacToeMatch(player=self.current_starting_player)
        self.scores = [0, 0]  # [PLAYER_ONE score, PLAYER_TWO score]

    def play(self, pos: int) -> int | None:
        """
        Plays a move at the given position and returns the winner if the game has ended.

        Args:
            pos (int): The board position (0-8) where the current player makes a move.

        Returns:
            int | None: The winner (PLAYER_ONE, PLAYER_TWO, or 0 for a tie) if the match is over; None otherwise.

        Raises:
            ValueError: Propagated from TicTacToeMatch.update if the move is invalid.
        """
        self.match.update(pos)
        if self.match.winner is not None:
            if self.match.winner in (PLAYER_ONE, PLAYER_TWO):
                self.scores[self.match.winner - 1] += 1
            # You can also handle tie cases (e.g., count as a half-point for both players) if desired.
            return self.match.winner
        return None

    def get_current_player(self) -> int:
        """
        Returns the identifier of the current player.
        """
        return self.match.get_current_player()

    def reset(self) -> None:
        """
        Resets the current match and updates the starting player based on the defined policy.
        """
        self.current_starting_player = self.starting_player_policy(self.current_starting_player)
        self.match = TicTacToeMatch(player=self.current_starting_player)

    def __str__(self) -> str:
        """
        Returns a string representation of the current score.
        """
        return f"Player {PLAYER_ONE}: {self.scores[0]} - Player {PLAYER_TWO}: {self.scores[1]}"

    def __eq__(self, other: object) -> bool:
        """
        Checks equality between two TicTacToeGame instances.
        """
        if not isinstance(other, TicTacToeGame):
            return NotImplemented
        return (self.current_starting_player == other.current_starting_player and
                self.scores == other.scores and
                self.match == other.match)
