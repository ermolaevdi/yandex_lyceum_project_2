import pygame

from square import Square


class Helper:
    def __init__(self, field: Square, max_frame, pause=0, r=0, g=0, b=0):

        self.enabled = True
        self.x = field.x
        self.y = field.y
        self.max_frame = max_frame
        self.pause = pause
        self.size = field.size - 4
        self.current_frame = 0

        self.r = r
        self.g = g
        self.b = b

    def draw(self, scene, delta_time):
        self.current_frame += 1

        if self.pause > self.current_frame:
            return False

        if (self.current_frame - self.pause) > self.max_frame:
            self.enabled = False

        if self.enabled:
            pygame.draw.rect(scene, (int(self.r), int(self.g), int(self.b)),
                             (self.x + 2, self.y + 2, self.size, self.size))

            pygame.draw.rect(scene, Square.clr_line_outline,
                             (self.x + 4, self.y + 4, self.size - 4, self.size - 4), 2)

            self.b += delta_time * 5
            self.g += delta_time * 350

            if self.r > 255:
                self.r = 0
            if self.g > 255:
                self.g = 0
            if self.b > 255:
                self.b = 0
