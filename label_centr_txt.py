import pygame

from tuning import *



class LabelTextCentral:
    def __init__(self, y, text, id, clr, font, max_frame, size):

        self.text = text

        # Если size == 2, то шрифт больше, чем когда size == 1
        if size == 2:
            self.surface_text = font.getBigText(id, text, clr)
        elif size == 1:
            self.surface_text = font.getMediumText(id, text, clr)

        self.enabled = True
        self.x = (WIDTH - self.surface_text.get_width()) // 2
        self.y = y
        self.max_frame = max_frame
        self.increase_alpha = 1024
        self.frame = 0
        self.alpha = 0

    def draw(self, scene: pygame.Surface, delta_time):
        if self.enabled:
            self.surface_text.set_alpha(self.alpha)

            if self.frame > self.max_frame * 0.6:
                self.alpha -= self.increase_alpha * delta_time
            else:
                self.alpha += self.increase_alpha * delta_time

            if self.alpha < 0:
                self.alpha = 0
            elif self.alpha > 255:
                self.alpha = 255

            scene.blit(self.surface_text, (self.x, self.y))
            self.frame += 1

            if self.frame > self.max_frame:
                self.enabled = False
