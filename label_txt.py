import pygame

from tuning import *


class LabelText:

    def __init__(self, font):
        self.font = font

    def draw(self, scene: pygame.surface):
        scene.blit(self.font.getSystemText("ERROR", f"Ошибки: {error}",
                                           TEXT_COLOR[0]), (10, 10))
        scene.blit(self.font.getSystemText("LEVEL", f"Головоломка: {level + 1}/{max_level + 1}",
                                           TEXT_COLOR[0]), (200, 10))
        #print(max_level + 1)
        scene.blit(self.font.getSystemText("ADVICE", f"Подсказки: {advice}",
                                           TEXT_COLOR[0]), (480, 10))
        scene.blit(self.font.getSystemText("MAX_LEVEL", f"Пройдено уровней: {max_level}",
                                           TEXT_COLOR[0]), (710, 10))
