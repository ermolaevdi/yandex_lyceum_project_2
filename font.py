import pygame


class Font:
    """Генерирует поверхности с текстом для вывода на экран"""

    def __init__(self):
        """Определяет шрифты"""

        self.__font_medium = pygame.font.Font("RobotoRegular.ttf", 24)
        self.__font_small = pygame.font.Font("RobotoRegular.ttf", 18)
        self.__font_system = pygame.font.Font("RubikBold.ttf", 20)
        self.__font_big = pygame.font.Font("RubikBold.ttf", 30)
        self.__surfaces = {}
        self.__texts = {}

    def getSystemText(self, key, txt, color):
        """Вернёт поверхность с текстом"""

        if key in self.__texts:
            if txt == self.__texts[key]:
                return self.__surfaces[key]
        self.__texts[key] = txt
        self.__surfaces[key] = self.__font_system.render(txt, True, color)
        return self.__surfaces[key]

    def getMediumText(self, key, txt, color):
        """Вернёт поверхность с текстом"""

        if key in self.__texts:
            if txt == self.__texts[key]:
                return self.__surfaces[key]
        self.__texts[key] = txt
        self.__surfaces[key] = self.__font_medium.render(txt, True, color)
        return self.__surfaces[key]

    def getSmallText(self, key, txt, color):
        """Вернёт поверхность с текстом"""

        if key in self.__texts:
            if txt == self.__texts[key]:
                return self.__surfaces[key]
        self.__texts[key] = txt
        self.__surfaces[key] = self.__font_small.render(txt, True, color)
        return self.__surfaces[key]

    def getBigText(self, key, txt, color):
        """Вернёт поверхность с текстом"""

        if key in self.__texts:
            if txt == self.__texts[key]:
                return self.__surfaces[key]
        self.__texts[key] = txt
        self.__surfaces[key] = self.__font_big.render(txt, True, color)
        return self.__surfaces[key]