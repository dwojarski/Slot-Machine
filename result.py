import random


class Result(object):

    def __init__(self):
        self.__bonusStreak = 0
        self.__win = False
        self.__symbol = -1

    def calculate_win(self, bet):
        self.__symbol = random.randint(0, 4)
        chances = [15, 25, 30, 32, 32.1]
        symbolChance = chances[self.__symbol] - (0 if self.__symbol == 0 else chances[self.__symbol - 1])
        bonusBet = 1.0
        if 1 < bet < 5:
            bonusBet = 1.1
        elif 5 <= bet < 10:
            bonusBet = 1.5
        elif 10 <= bet < 20:
            bonusBet = 1.75
        elif 20 <= bet < 30:
            bonusBet = 2.0
        elif 30 <= bet < 40:
            bonusBet = 2.5
        elif 40 <= bet < 50:
            bonusBet = 3.5
        elif bet >= 50:
            bonusBet = 5.0
        win = symbolChance * bonusBet + self.__bonusStreak

        house = random.random() * 100
        if win >= house:
            self.__bonusStreak = 0
            self.__win = True
        else:
            self.__bonusStreak += (1 if self.__bonusStreak < 10 else 0)
            self.__win = False

    def get_win(self):
        return self.__win

    def get_symbol(self):
        return self.__symbol

    def reset(self):
        self.__win = False
        self.__symbol = -1

    """
        setter for testing purposes
    """
    def set_bonus_streak(self, bonus: int):
        self.__bonusStreak = bonus
