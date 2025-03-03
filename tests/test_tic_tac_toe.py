import unittest
from tic_tac_toe.match import TicTacToeMatch, PLAYER_ONE, PLAYER_TWO, EMPTY
from tic_tac_toe.game import TicTacToeGame


class TestTicTacToeMatch(unittest.TestCase):
    def test_initial_state(self):
        match = TicTacToeMatch(PLAYER_ONE)
        self.assertEqual(match.board, [EMPTY] * 9)
        self.assertEqual(match.current_player, PLAYER_ONE)
        self.assertIsNone(match.winner)

    def test_invalid_move(self):
        match = TicTacToeMatch(PLAYER_ONE)
        with self.assertRaises(ValueError):
            match.update(10)  # Invalid position
        match.update(0)
        with self.assertRaises(ValueError):
            match.update(0)  # Position already taken

    def test_winner(self):
        match = TicTacToeMatch(PLAYER_ONE)
        # PLAYER_ONE wins on the top row: positions 0, 1, 2
        match.update(0)  # PLAYER_ONE
        match.update(3)  # PLAYER_TWO
        match.update(1)  # PLAYER_ONE
        match.update(4)  # PLAYER_TWO
        match.update(2)  # PLAYER_ONE wins
        self.assertEqual(match.winner, PLAYER_ONE)

    def test_tie(self):
        # Simulate a tie game
        match = TicTacToeMatch(PLAYER_ONE)
        # Sequence of moves resulting in a tie:
        # Board state: X O X
        #              X X O
        #              O X O
        moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]
        for move in moves:
            try:
                match.update(move)
            except ValueError:
                pass
        self.assertEqual(match.winner, 0)


class TestTicTacToeGame(unittest.TestCase):
    def test_score_update(self):
        game = TicTacToeGame(PLAYER_ONE)
        # Simulate a win for PLAYER_ONE (top row win)
        moves = [0, 3, 1, 4, 2]
        for move in moves:
            result = game.play(move)
        self.assertEqual(result, PLAYER_ONE)
        self.assertEqual(game.scores[PLAYER_ONE - 1], 1)

    def test_reset(self):
        game = TicTacToeGame(PLAYER_ONE)
        # Play a full game resulting in a tie
        moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]
        for move in moves:
            game.play(move)
        prev_starting = game.current_starting_player
        game.reset()
        # After reset, the starting player should be updated according to the policy
        self.assertNotEqual(game.match.current_player, prev_starting)


if __name__ == '__main__':
    unittest.main()
