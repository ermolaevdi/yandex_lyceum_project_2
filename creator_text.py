import pygame

import tuning


class CreatorText:

    def __init__(self, font):

        self.font = font
        self.txt = []

        self.txt.append("Японские кроссворды")
        self.txt.append("")
        self.txt.append("Разработка игры и дизайн:")
        self.txt.append("Ермолаев Дмитрий (с) 2024")
        self.txt.append("Связаться с разработчиком: cosmosx.ru")
        self.txt.append("")
        self.txt.append("Удачи и успехов Вам при решении различных головоломок!")
        self.txt.append("")
        self.txt.append("***Лицей Академии Яндекса***")

        self.x = 900

    def draw(self, scene: pygame.surface, deltatime):

        pygame.draw.rect(scene, (37, 37, 37), (self.x, 150, 1000, 400))
        if self.x > 200:
            self.x -= 2000 * deltatime

        for i in range(len(self.txt)):
            if i == 0:
                clr = tuning.COLOR_YELLOW
                surftext = self.font.getMediumText(f"AUTH{i}", self.txt[i], clr)
            else:
                clr = tuning.COLOR_GRAY
                surftext = self.font.getSmallText(f"AUTH{i}", self.txt[i], clr)

            scene.blit(surftext, (self.x + 40, 220 + 30 * i))
