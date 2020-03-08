import pygame
import string


class Sprite:

    def __init__(self, filepath: string, starting_pos: [int, int], colorkey: [int, int, int]):
        self.__filepath = filepath
        self.__colorkey = colorkey
        self.__img = None
        self._position = starting_pos

    def load(self):
        try:
            self.__img = pygame.image.load(self.__filepath)
        except:
            print('An error has occurred while the game was loading the image [%s]' % self.__filepath)
            input('Press any key to exit')
            exit(0)

    def render(self, window):
        try:
            self.__img.set_colorkey(self.__colorkey)
            window.blit(self.__img, self._position)
        except:
            print('An error has occurred while the game was rendering the image.')
            input('Press any key to exit')
            exit(0)

    """
    getter for testing purposes
    """
    def get_position_OY(self):
        return self._position[1]
