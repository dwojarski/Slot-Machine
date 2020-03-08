import pygame
import string
from rectangle import Rectangle

from pkg_resources import resource_filename


class Text(object):

    def __init__(self, content: string, size: int, pos: [int, int], color: [int, int, int], justify: int,
                 make_field=False, field_rect_size=[0,0,0,0], field_color=[0,0,0]):
        pygame.init()
        self.__font_obj = pygame.font.Font(resource_filename(__name__, 'assets/font/freesansbold.ttf'), size)
        self.__content = content
        self.__pos = pos
        self.__color = color
        self.__make_field = make_field
        self.__justify = justify
        if make_field:
            self.__field = Rectangle(field_rect_size, field_color)

    def render(self, window):
        text_obj = self.__font_obj.render(self.__content, True, self.__color)
        text_rect = text_obj.get_rect()
        if self.__justify == 1:
            text_rect.topleft = (self.__pos[0], self.__pos[1])
        elif self.__justify == 2:
            text_rect.center = (self.__pos[0], self.__pos[1])
        elif self.__justify == 3:
            text_rect.topright = (self.__pos[0], self.__pos[1])
        if self.__make_field:
            self.__field.render(window)
        window.blit(text_obj, text_rect)

    def set_content(self, content: string):
        self.__content = content
