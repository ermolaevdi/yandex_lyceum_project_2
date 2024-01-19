import pygame

from square import Square


class Error:

    def __init__(self, field: Square, max_frame):

        self.enabled = True
        self.size = field.size
        self.x = field.x
        self.y = field.y
        self.radius = 0
        self.max_frame = max_frame
        self.operating_frame = 0
        self.max_radius = field.size - 4

        self.r = 0
        self.g = 0
        self.b = 0

    def draw(self, scene, delta_time):
        self.operating_frame += 1

        if self.operating_frame > self.max_frame:
            self.enabled = False

        if self.enabled:
            pygame.draw.rect(scene, (int(self.r), int(self.g), int(self.b)),
                             (self.x + 2, self.y + 2, self.max_radius, self.max_radius))

            pygame.draw.rect(scene, Square.clr_line_outline,
                             (self.x + 2, self.y + 2, self.max_radius, self.max_radius), 2)

            self.radius += delta_time * 20
            if self.radius > self.max_radius:
                self.radius = 0

            self.r += delta_time * 512
            self.g += delta_time * 100
            self.b += delta_time * 500

            if self.r > 200:
                self.r = 0
            if self.g > 200:
                self.g = 0
            if self.b > 200:
                self.b = 0
