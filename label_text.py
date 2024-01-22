import pygame

import tuning


class LabelText:

    def __init__(self, font):
        self.font = font

    def draw(self, scene: pygame.surface):
        scene.blit(self.font.getSystemText("ERROR", f"Ошибки: {tuning.error}",
                                           tuning.TEXT_COLOR[0]), (10, 10))
        scene.blit(self.font.getSystemText("LEVEL", f"Головоломка: {tuning.level + 1}/{tuning.max_level + 1}",
                                           tuning.TEXT_COLOR[0]), (200, 10))
        #print(max_level + 1)
        scene.blit(self.font.getSystemText("ADVICE", f"Подсказки: {tuning.advice}",
                                           tuning.TEXT_COLOR[0]), (480, 10))
        scene.blit(self.font.getSystemText("MAX_LEVEL", f"Пройдено уровней: {tuning.max_level}",
                                           tuning.TEXT_COLOR[0]), (710, 10))
