import pygame

import tuning
from redactor_square import Square


# Отдельная клетка на поле
class Square(Square):
    # Цвета для оформления каждой клетки
    color_line_outline = "#7A7E7A"
    color_line = "#777777"
    color_fill = "#ACACAC"
    # Ширина линии
    width_line = 2

    def __init__(self, x, y, size):
        super(Square, self).__init__(x, y, size)
        self.blocked = False

    def drawIJ(self, scene, i, j, i_cells, j_cells):
        pygame.draw.rect(scene, self.color, (self.x, self.y, self.size, self.size), 1)

        if self.enabled:
            inline = self.size // 5
            pygame.draw.rect(scene, self.color_fill,
                             (self.x + 2, self.y + 2, self.size - 4, self.size - 4))
            pygame.draw.rect(scene, self.color_line,
                             (self.x + inline, self.y + inline, self.size - inline * 2, self.size - inline * 2))

        if i % i_cells == 0:
            pygame.draw.line(scene, self.color_line_outline,
                             (self.x - 1, self.y), (self.x - 1, self.y + self.size), self.width_line)
        elif (i + 1) % i_cells == 0:
            pygame.draw.line(scene, self.color_line_outline,
                             (self.x  - 1 + self.size, self.y),
                             (self.x + self.size - 1, self.y + self.size), self.width_line)

        if j % j_cells == 0:
            pygame.draw.line(scene, self.color_line_outline,
                             (self.x, self.y - 1), (self.x + self.size, self.y - 1), self.width_line)
        elif (j + 1) % j_cells == 0:
            pygame.draw.line(scene, self.color_line_outline,
                             (self.x, self.y + self.size - 1),
                             (self.x + self.size, self.y + self.size - 1), self.width_line)

        if self.blocked:
            pygame.draw.line(scene,
                             tuning.COLOR_RED,
                             (self.x + self.size // 4, self.y + self.size // 4),
                             (self.x + self.size - self.size // 4, self.y + self.size - self.size // 4),
                             self.size // 5)
            pygame.draw.line(scene,
                            tuning.COLOR_RED,
                            (self.x + self.size - self.size // 4, self.y + self.size // 4),
                            (self.x + self.size // 4, self.y + self.size - self.size // 4),
                            self.size // 5)
