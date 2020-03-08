import pygame


class Rectangle:

    def __init__(self, field_rect_size: [int, int, int, int], field_color: [int, int, int]):
        self.__field_rect_size = field_rect_size
        self.__field_color = field_color

    def render(self, window):
        pygame.draw.rect(window, self.__field_color, self.__field_rect_size)