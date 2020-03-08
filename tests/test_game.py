import unittest
from slot_machine import Game
from result import Result


class TestGame(unittest.TestCase):

    def test_game_update_values(self):
        game = Game()
        game.update_values(100, -100)
        self.assertEqual(game.get_bet(), 100)
        self.assertEqual(game.get_account(), 0)

    def test_game_outcome_win(self):
        result = Result()
        result.set_bonus_streak(100)
        result.calculate_win(1)
        game = Game()
        game.set_result(result)
        game.update_values(1, -5)
        game.outcome()
        self.assertGreater(game.get_account(), 100)

    def test_game_outcome_loss(self):
        result = Result()
        result.set_bonus_streak(-100)
        result.calculate_win(1)
        game = Game()
        game.set_result(result)
        game.update_values(1, -5)
        game.outcome()
        self.assertLess(game.get_account(), 100)
