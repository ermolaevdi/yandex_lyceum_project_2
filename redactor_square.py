import pygame


BLANK_FIELD = 64
class RedactorSquare:

    color = (100, 100, 100)
    clr_line = (190, 190, 190)
    color_fill = (170, 170, 170)

    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.enabled = False

    def draw(self, scene: pygame):
        if self.enabled:
            pygame.draw.rect(scene, RedactorSquare.color_fill,
                             (self.x + 3, self.y + 3, self.size - 6, self.size - 6))
        else:
            pygame.draw.rect(scene, RedactorSquare.color,
                             (self.x, self.y, self.size, self.size), 1)

        if (((self.x - BLANK_FIELD) / self.size) % 5) == 0:
            pygame.draw.line(scene, RedactorSquare.clr_line, (self.x, self.y),
                             (self.x, self.y + self.size), 2)
        elif (((self.x + self.size - BLANK_FIELD) / self.size) % 5) == 0:
            pygame.draw.line(scene, RedactorSquare.clr_line, (self.x + self.size, self.y),
                             (self.x + self.size, self.y + self.size), 2)

        if (((self.y - BLANK_FIELD) / self.size) % 5) == 0:
            pygame.draw.line(scene, RedactorSquare.clr_line, (self.x, self.y),
                             (self.x + self.size, self.y), 2)
        elif (((self.y + self.size - BLANK_FIELD) / self.size) % 5) == 0:
            pygame.draw.line(scene, RedactorSquare.clr_line, (self.x, self.y + self.size),
                             (self.x + self.size, self.y + self.size), 2)

    def drawIJ(self, scene: pygame, a, b):
        if self.enabled:
            pygame.draw.rect(scene, RedactorSquare.color_fill, (a + 3, b + 3, self.size - 6, self.size - 6))
        else:
            pygame.draw.rect(scene, RedactorSquare.color, (a, b, self.size, self.size), 1)

        if (((a - BLANK_FIELD) / self.size) % 5) == 0:
            pygame.draw.line(scene, RedactorSquare.clr_line, (a, b), (a, b + self.size), 2)
        elif (((a + self.size - BLANK_FIELD) / self.size) % 5) == 0:
            pygame.draw.line(scene, RedactorSquare.clr_line, (a + self.size, b),
                             (a + self.size, b + self.size), 2)

        if (((b - BLANK_FIELD) / self.size) % 5) == 0:
            pygame.draw.line(scene, RedactorSquare.clr_line, (a, b),
                             (a + self.size, b), 2)
        elif (((b + self.size - BLANK_FIELD) / self.size) % 5) == 0:
            pygame.draw.line(scene, RedactorSquare.clr_line, (a, b + self.size),
                             (a + self.size, b + self.size), 2)
