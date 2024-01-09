import pygame

from tuning import *


class RulesText:

    def __init__(self, font):
        self.font = font
        self.txt = []
        self.txt.append("Правила игры")
        self.txt.append("")
        self.txt.append("При нажатии на кнопку '?' необходимо правильно решить простой пример для тренировки устного")
        self.txt.append("счёта :) Чем больше решённых примеров, тем больше шансов решить головоломку полностью")
        self.txt.append("")
        self.txt.append("Головоломка решается путём сопоставления чисел, находящихся как в строке (слева от строки), ")
        self.txt.append("так и в столбцах (вверху каждого столбца).")
        self.txt.append("Данные числа показывают, сколько должно быть закрашенных клеток в строке/в столбце.")
        self.txt.append("Если в строке/в столбце указано только одно число, следовательно, в строке/в столбце")
        self.txt.append("закрашенные клетки идут подряд друг за другом. Если в строке/в столбце указано больше одного")
        self.txt.append("числа, значит, есть несколько промежутков закрашенных клеток с неизвестным по длине разрывом.")
        self.txt.append("В ином случае в строке/в столбце закрашенные клетки отсутствуют :)")
        self.txt.append("В ином случае в строке/в столбце закрашенные клетки отсутствуют :)")
        self.txt.append("")
        self.txt.append("")
        self.txt.append("Удачи и успехов Вам при решении различных головоломок!")

        self.x = 900

    def draw(self, scene: pygame.surface, deltatime):

        pygame.draw.rect(scene, (37, 37, 37), (self.x, 150, 1000, 430))
        if self.x > 200:
            self.x -= 2000 * deltatime

        len_txt = len(self.txt)
        for i in range(len_txt):
            if i == 0:
                color = COLOR_YELLOW
                surftext = self.font.getMediumText(f"PL{i}", self.txt[i], color)
            else:
                color = COLOR_GRAY
                surftext = self.font.getSmallText(f"PL{i}", self.txt[i], color)

            scene.blit(surftext, (self.x + 30, 220 + 30 * i))
