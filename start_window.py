import pygame

from tuning import *


class StartScreen:
    def __init__(self):

        self.enabled = True
        self.alpha = 255
        self.frame = 0
        self.img_start = pygame.image.load("png/start_window.png")

    def draw(self, scene, delta_time):
        # Скорость смены стартового кадра
        if self.enabled:
            if self.frame < FPS * 0.1:
                self.frame += FPS * delta_time
            else:
                self.alpha -= 255 * delta_time / 1.5

            if self.alpha <= 0:
                self.enabled = False

            self.img_start.set_alpha(self.alpha)
            scene.blit(self.img_start, (0, 0))
