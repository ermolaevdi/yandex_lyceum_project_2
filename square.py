import pygame

from tuning import *
from redactor_square import RedactorSquare


# Отдельная клетка на поле
class Square(RedactorSquare):

    # Цвета для оформления каждой клетки
    clr_line_outline = "#7A7E7A"
    clr_line = "#777777"
    color_fill = "#ACACAC"
    # Ширина линии
    width_line = 2

    def __init__(self, x, y, size):
        super(Square, self).__init__(x, y, size)

        self.blocked = False

    def drawIJ(self, scene, a, b, cells_a, cells_b):
        pygame.draw.rect(scene, self.color, (self.x, self.y, self.size, self.size), 1)
        if self.enabled:
            in_appliance = self.size // 5
            pygame.draw.rect(scene, self.color_fill, (self.x + 2, self.y + 2, self.size - 4, self.size - 4))
            pygame.draw.rect(scene, self.clr_line, (self.x + in_appliance,
                                                    self.y + in_appliance, self.size - in_appliance * 2,
                                                    self.size - in_appliance * 2))

        if (a % cells_a) == 0:
            pygame.draw.line(scene, self.clr_line_outline, (self.x - 1, self.y),
                             (self.x - 1, self.y + self.size), self.width_line)
        elif ((a + 1) % cells_a) == 0:
            pygame.draw.line(scene, self.clr_line_outline, (self.x - 1 + self.size, self.y),
                             (self.x + self.size - 1, self.y + self.size), self.width_line)

        if (b % cells_b) == 0:
            pygame.draw.line(scene, self.clr_line_outline, (self.x, self.y - 1),
                             (self.x + self.size, self.y - 1), self.width_line)
        elif ((b + 1) % cells_b) == 0:
            pygame.draw.line(scene, self.clr_line_outline, (self.x, self.y + self.size - 1),
                             (self.x + self.size, self.y + self.size - 1), self.width_line)

        if self.blocked:
            pygame.draw.line(scene, COLOR_RED,
                             (self.x + self.size // 4, self.y + self.size // 4),
                             (self.x + self.size - self.size // 4, self.y + self.size - self.size // 4),
                             self.size // 5)
            pygame.draw.line(scene, COLOR_RED,
                            (self.x + self.size - self.size // 4, self.y + self.size // 4),
                            (self.x + self.size // 4, self.y + self.size - self.size // 4),
                            self.size // 5)
v
