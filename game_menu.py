from colors import Colors
from text import Text


class Menu(object):

    def __init__(self):

        header = 'MENU:'
        space = '[SPACJA] - otworz/zamknij menu'
        one = '[1] - obstaw 1 zeton'
        two = '[2] - obstaw 5 zetonow'
        three = '[3] - obstaw 20 zetonow'
        four = '[4] - obstaw 50 zetonow'
        enter = '[ENTER] - rozpocznij losowanie'

        headerText = Text(str(header), 30, [100, 20], Colors.WHITE.value, 2, True, [0, 0, 200, 200], Colors.GREY.value)
        spaceText = Text(str(space), 12, [5, 40], Colors.WHITE.value, 1)
        oneText = Text(str(one), 12, [5, 60], Colors.WHITE.value, 1)
        twoText = Text(str(two), 12, [5, 80], Colors.WHITE.value, 1)
        threeText = Text(str(three), 12, [5, 100], Colors.WHITE.value, 1)
        fourText = Text(str(four), 12, [5, 120], Colors.WHITE.value, 1)
        enterText = Text(str(enter), 12, [5, 140], Colors.WHITE.value, 1)
        self.__menuContent = [headerText, spaceText, oneText, twoText, threeText, fourText, enterText]

    def render(self, window):
        for content in self.__menuContent:
            content.render(window)
