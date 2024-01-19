import pygame

import tuning
from tuning import *
from sample import Sample


class Cell:
    """ Выводим пример для решения, чтобы открыть иконку. """

    def __init__(self, value, x, y, size_square, font, text_clr):

        self.value = value
        self.x = x
        self.y = y
        self.size_square = size_square
        self.font = font
        self.text_clr = text_clr

        self.error_digit = False
        self.background = False
        self.screen = f"{value}"

    def set_error_digit(self):
        self.error_digit = True
        self.screen = "?"

    def draw(self, scene: pygame.surface):
        key = f"cell_{self.x}{self.y}"

        if self.screen == "?":
            pygame.draw.rect(scene, TEXT_LIGHT_ATTENTION,
                             (self.x + (self.size_square - self.size_square // 1.5) // 2,
                              self.y, self.size_square // 1.5, 21))

            res = self.font.getSystemText(key, f"{self.screen}", COLOR_DEEP_GRAY)
            coordinates_x0 = (self.size_square - res.get_width()) // 2

        else:
            res = self.font.getSystemText(key, f"{self.screen}", self.text_clr)
            coordinates_x0 = (self.size_square - res.get_width()) // 2

        if self.background:
            if self.error_digit:
                pygame.draw.rect(scene, TEXT_LIGHT_BAD, (self.x, self.y, self.size_square, 21))
            else:
                pygame.draw.rect(scene, TEXT_LIGHT_GOOD, (self.x, self.y, self.size_square, 21))

        scene.blit(res, (self.x + coordinates_x0, self.y))

    def check_mouse(self, x, y):
        if (self.x < x) and (x < self.x + self.size_square) and (self.y < y) and (y < self.y + 31):
            self.background = True
            return True
        else:
            self.background = False
        return False

    def press_mouse_1(self, x, y):
        if self.screen != "?" and not self.error_digit:
            return False

        if self.background:
            if tuning.see_example is None:
                tuning.see_example = Sample(self.x, self.y, self.size_square, self.value, self)

    def delete_view_example(self):
        tuning.view_example = None
