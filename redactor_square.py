import pygame


BLANK_FIELD = 64

class Square:
    color = (100, 100, 100)
    color_line = (190, 190, 190)
    color_fill = (170, 170, 170)

    def __init__(self, x, y, size):

        self.x = x
        self.y = y
        self.size = size
        self.enabled = False

    def draw(self, scene: pygame):
        if self.enabled:
            pygame.draw.rect(scene, Square.color_fill,
                             (self.x + 3, self.y + 3, self.size - 6, self.size - 6))
        else:
            pygame.draw.rect(scene, Square.color,
                             (self.x, self.y, self.size, self.size), 1)

        if ((self.x - BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line,
                             (self.x, self.y), (self.x, self.y + self.size), 2)
        elif ((self.x + self.size - BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line,
                             (self.x + self.size, self.y),
                             (self.x + self.size, self.y + self.size), 2)

        if ((self.y - BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line,
                             (self.x, self.y), (self.x + self.size, self.y), 2)
        elif ((self.y + self.size - BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line,
                             (self.x, self.y + self.size),
                             (self.x + self.size, self.y + self.size), 2)

    def drawIJ(self, scene: pygame, i, j):
        if self.enabled:
            pygame.draw.rect(scene, Square.color_fill, (i + 3, j + 3, self.size - 6, self.size - 6))
        else:
            pygame.draw.rect(scene, Square.color, (i, j, self.size, self.size), 1)

        if ((i - BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line,
                             (i, j), (i, j + self.size), 2)
        elif ((i + self.size - BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line,
                             (i + self.size, j), (i + self.size, j + self.size), 2)

        if ((j - BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line,
                             (i, j), (i + self.size, j), 2)
        elif ((j + self.size - BLANK_FIELD) / self.size) % 5 == 0:
            pygame.draw.line(scene, Square.color_line,
                             (i, j + self.size), (i + self.size, j + self.size), 2)
