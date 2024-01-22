import pygame

from tuning import *


class StartScreen:

    def __init__(self):
        self.frame = 0
        self.enabled = True
        self.alpha = 255
        self.img = pygame.image.load("foto_png/start_window.png")
        self.enabled = True

    def draw(self, scene, deltatime):
        # Скорость смены стартового кадра
        if self.enabled:
            if self.frame < FPS * 0.1:
                self.frame += FPS * deltatime
            else:
                self.alpha -= 255 * deltatime / 1.5

            if self.alpha <= 0:
                self.enabled = False

            self.img.set_alpha(self.alpha)
            scene.blit(self.img, (0, 0))
