import pygame
import sys
import random
from sprite import Sprite
from segment import Segment
from text import Text
from result import Result
from game_menu import Menu
from colors import Colors

from pkg_resources import resource_filename


class Game(object):

    def __init__(self):
        self.clock = pygame.time.Clock()

        pygame.init()
        self.account = 100
        self.bet = 0
        pygame.display.set_caption('Jednoreki Bandyta')
        self.window = pygame.display.set_mode((800, 600))
        self.window.fill(Colors.BLACK.value)

        segmentL = Segment(resource_filename(__name__, 'assets/img/segment.bmp'), [242, 45], Colors.BLACK.value)
        segmentM = Segment(resource_filename(__name__, 'assets/img/segment.bmp'), [352, 45], Colors.BLACK.value)
        segmentR = Segment(resource_filename(__name__, 'assets/img/segment.bmp'), [462, 45], Colors.BLACK.value)
        machineL = Sprite(resource_filename(__name__, 'assets/img/maszynaL.bmp'), [200, 230], Colors.BLACK.value)
        machineR = Sprite(resource_filename(__name__, 'assets/img/maszynaR.bmp'), [562, 230], Colors.BLACK.value)
        machineB1 = Sprite(resource_filename(__name__, 'assets/img/maszynaB.bmp'), [230, 230], Colors.BLACK.value)
        machineB2 = Sprite(resource_filename(__name__, 'assets/img/maszynaB.bmp'), [230, 357], Colors.BLACK.value)

        self.spritesTable = [segmentL, segmentM, segmentR, machineL, machineR, machineB1, machineB2]
        self.accountText = Text(str(self.account), 30, [50, 575], Colors.WHITE.value, 2, True, [0, 550, 100, 50], Colors.GREY.value)
        self.betText = Text(str(self.bet), 30, [400, 400], Colors.WHITE.value, 2, True, [300, 375, 200, 50], Colors.GREY.value)
        self.bankruptText = Text('BANKRUT!', 100, [400, 300], Colors.RED.value, 2, True, [50, 200, 700, 200], Colors.BLACK.value)
        self.accountDescText = Text('KONTO', 25, [50, 540], Colors.WHITE.value, 2)
        self.menu = Menu()
        self.startTicks = 0
        self.result = Result()
        self.soundboard = (resource_filename(__name__, 'assets/sound/erro.mp3'),
                           resource_filename(__name__, 'assets/sound/money.mp3'),resource_filename(__name__, 'assets/sound//how.mp3'))
        self.playSound = False
        self.space = True
        self.enter = False
        self.setM = False
        self.setR = False
        self.bankrupt = False

        self.load()

    def game_loop(self):
        while True:
            self.event_handling()
            self.render()
            pygame.display.flip()
            fps = 60
            self.clock.tick(fps)
            if not self.enter:
                continue
            time = (pygame.time.get_ticks() - self.startTicks) / 1000
            if time < 3:
                if self.result.get_symbol() == -1:
                    self.result.calculate_win(self.bet)
                self.spritesTable[0].move_OY_down(fps)
                self.spritesTable[1].move_OY_down(fps)
                self.spritesTable[2].move_OY_down(fps)
            elif 3 < time <= 5:
                self.spritesTable[0].move_OY_down(int(fps/3))
                self.spritesTable[1].move_OY_down(fps)
                self.spritesTable[2].move_OY_down(fps)
            elif 5 < time <= 7:
                self.spritesTable[0].stop_at(self.result.get_symbol())
                self.spritesTable[1].move_OY_down(int(fps/3))
                self.spritesTable[2].move_OY_down(fps)
            elif 7 < time <= 10:
                if not self.setM:
                    if self.result.get_win():
                        self.spritesTable[1].stop_at(self.result.get_symbol())
                    else:
                        self.spritesTable[1].stop_at(random.randint(0, 4))
                self.setM = True
                self.spritesTable[2].move_OY_down(int(fps/3))
            elif time > 10:
                if not self.setR:
                    if not self.result.get_win():
                        stop = random.randint(0, 4)
                        if stop != self.result.get_symbol():
                            self.spritesTable[2].stop_at(stop)
                            self.setR = True
                            self.enter = False
                    else:
                        self.spritesTable[2].stop_at(self.result.get_symbol())
                        self.setR = True
                        self.enter = False
            self.outcome()

    def event_handling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.space = not self.space
                if not self.enter:
                    if event.key == pygame.K_RETURN:
                        if self.bet > 0:
                            self.enter = True
                            self.startTicks = pygame.time.get_ticks()
                    elif event.key == pygame.K_1:
                        if self.account >= 5:
                            self.update_values(1, -5)
                    elif event.key == pygame.K_2:
                        if self.account >= 25:
                            self.update_values(5, -25)
                    elif event.key == pygame.K_3:
                        if self.account >= 100:
                            self.update_values(20, -100)
                    elif event.key == pygame.K_4:
                        if self.account >= 250:
                            self.update_values(50, -250)

    def load(self):
        for sprite in self.spritesTable:
            sprite.load()

    def render(self):
        self.window.fill(Colors.BLACK.value)
        for sprite in self.spritesTable:
            sprite.render(self.window)
        if not self.enter:
            pygame.draw.polygon(self.window, Colors.SILVER.value, [(600, 290), (600, 310), (650, 210), (650, 190)])
            pygame.draw.circle(self.window, Colors.RED.value, [650, 200], 25)
        else:
            pygame.draw.polygon(self.window, Colors.SILVER.value, [(600, 290), (600, 310), (650, 430), (650, 410)])
            pygame.draw.circle(self.window, Colors.RED.value, [650, 420], 25)
        pygame.draw.rect(self.window, Colors.ORANGE.value, [225, 0, 355, 230])
        pygame.draw.rect(self.window, Colors.ORANGE.value, [225, 371, 355, 230])
        self.accountText.render(self.window)
        self.accountDescText.render(self.window)
        self.betText.render(self.window)
        if self.space:
            self.menu.render(self.window)
        if self.bankrupt:
            self.bankruptText.render(self.window)
            if self.playSound:
                pygame.mixer.music.load(self.soundboard[2])
                pygame.mixer.music.play(0)
                self.playSound = False
            time = (pygame.time.get_ticks() - self.startTicks) / 1000
            if time > 15.5:
                sys.exit(0)

    def update_values(self, bet, account):
        self.bet += bet
        self.betText.set_content(str(self.bet))
        self.account += account
        self.accountText.set_content(str(self.account))

    def outcome(self):
        if not self.enter:
            if self.result.get_win():
                multiplier = [2, 3, 4, 5, 10]
                self.update_values(-self.bet, self.bet * 5 * multiplier[self.result.get_symbol()])
                pygame.mixer.music.load(self.soundboard[1])
                pygame.mixer.music.play(0)
            else:
                self.update_values(-self.bet, 0)
                pygame.mixer.music.load(self.soundboard[0])
                pygame.mixer.music.play(0)
                if self.account == 0:
                    self.bankrupt = True
                    self.playSound = True
            self.reset_flags()

    def reset_flags(self):
        self.setM = False
        self.setR = False
        self.result.reset()

    """
    getters and setters  for testing purposes
    """
    def get_bet(self):
        return self.bet

    def get_account(self):
        return self.account

    def set_result(self, result: Result):
        self.result = result


if __name__ == "__main__":
    Game.game_loop(Game())
