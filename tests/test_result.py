import unittest
from result import Result


class TestResult(unittest.TestCase):

    def test_calculate_win(self):
        result = Result()
        result.set_bonus_streak(100)
        result.calculate_win(1)
        self.assertTrue(result.get_win())

    def test_calculate_loss(self):
        result = Result()
        result.set_bonus_streak(-100)
        result.calculate_win(1)
        self.assertFalse(result.get_win())
