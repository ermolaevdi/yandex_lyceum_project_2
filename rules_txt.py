import pygame

from tuning import *


class RulesText:

    def __init__(self, font):
        self.font = font
        self.txt = []
        self.txt.append("Правила игры")
        self.txt.append("")
        self.txt.append("Изображения в игре закодированы числами/примерами, расположенными слева от строк, а также"
                        " сверху")
        self.txt.append("над столбцами. Количество чисел показывает, сколько групп серых клеток находятся в"
                        " соответствующих")
        self.txt.append("строке или столбце, а сами числа — сколько слитных клеток содержит каждая из этих групп")
        self.txt.append("(например, набор из трёх чисел — 4, 1, и 3 означает, что в этом ряду есть три группы:")
        self.txt.append("первая — из четырёх, вторая — из одной, третья — из трёх серых клеток).")
        self.txt.append("В данном кроссворде группы должны быть разделены минимум одной пустой клеткой.")
        self.txt.append("Пользователю необходимо найти единственно правильное размещение групп клеток.")
        self.txt.append("")
        self.txt.append("Удачи и успехов Вам при решении различных головоломок!")
        self.txt.append("")

        self.x = 50

    def draw(self, scene: pygame.surface, deltatime):

        pygame.draw.rect(scene, (37, 37, 37), (self.x, 150, 1000, 430))
        if self.x > 200:
            self.x -= 2000 * deltatime

        len_txt = len(self.txt)
        for i in range(len_txt):
            if i == 0:
                color = COLOR_YELLOW
                txt = self.font.getMediumText(f"PL{i}", self.txt[i], color)
            else:
                color = COLOR_GRAY
                txt = self.font.getSmallText(f"PL{i}", self.txt[i], color)

            scene.blit(txt, (self.x + 30, 220 + 30 * i))
