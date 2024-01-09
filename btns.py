import pygame

from font import Font
from tuning import *


class Buttons:

    def __init__(self):

        self.buttons = []
        
        font = Font()

        self.buttons.append(Button(Buttons.CHECK, 780, 110, ["4.png", "3.png"], "Проверить правильность решения? Помни, что счётчик ошибок может увеличиться :)", font))
        self.buttons.append(Button(Buttons.RESTART, 780, 230, ["24.png", "23.png"], "Начать прохождение уровня заново", font))
        self.buttons.append(Button(Buttons.ADVICE, 780, 290, ["8.png", "7.png"], "Открыть любые 1-3 клетки", font))

        self.buttons.append(Button(Buttons.NEXT, 780, 440, ["16.png", "15.png"], "Следующий уровень", font))
        self.buttons.append(Button(Buttons.PREV, 780, 470, ["18.png", "17.png"], "Предыдущий уровень", font))
        self.buttons.append(Button(Buttons.RULES, 780, 530, ["20.png", "19.png"], "Правила игры", font))
        self.buttons.append(Button(Buttons.EXIT, 780, 590, ["6.png", "5.png"], "Выйти из головоломки", font))
        self.buttons.append(Button(Buttons.RESET, 780, 620, ["22.png", "21.png"], "Сбросить весь прогресс", font))

        # Кнопки для выставления сложности
        self.buttons_difficulty = []
        self.buttons_difficulty.append(Button(Buttons.D30, 780, 320, ["10.png", "9.png"],
                                              "Меньше половины чисел скрыто выражениями", font))
        self.buttons_difficulty.append(Button(Buttons.D60, 780, 320, ["12.png", "11.png"],
                                              "Больше половины чисел скрыто выражениями", font))
        self.buttons_difficulty.append(Button(Buttons.D100, 780, 320, ["14.png", "13.png"],
                                              "Все числа скрыты выражениями", font))

        self.buttons.append(Button(Buttons.AUTHOR, 780, 740, ["2.png", "1.png"], "Разработчик игры", font))

    # Номера кнопок
    RULES = 0
    CHECK = 1
    RESTART = 2
    ADVICE = 3
    D30 = 4
    D60 = 5
    D100 = 6
    NEXT = 7
    PREV = 8
    EXIT = 9
    RESET = 10
    AUTHOR = 11

    def draw(self, scene, mouse_x, mouse_y, pressed):
        res = "NONE"
        ret_button_id = "NONE"

        for btn in self.buttons:
            if btn.id_button == Buttons.ADVICE and advice > 0 and error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressed)
            elif btn.id_button == Buttons.NEXT and level < max_level and error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressed)
            elif btn.id_button == Buttons.PREV and level > 0 and error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressed)
            elif btn.id_button != Buttons.ADVICE and \
                 btn.id_button != Buttons.NEXT and \
                 btn.id_button != Buttons.PREV and error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressed)
            elif error >= 8 and (btn.id_button == Buttons.EXIT or btn.id_button == Buttons.RESET):
                res = btn.draw(scene, mouse_x, mouse_y, pressed)

            if res != "NONE":
                ret_button_id = res

        if error < 8:
            res = self.buttons_difficulty[difficulty].draw(scene, mouse_x, mouse_y, pressed)

        if res != "NONE":
            ret_button_id = res

        return ret_button_id


class Button:

    def __init__(self, id_btn, x, y, im_name_file, advice, font):

        self.id_button = id_btn
        self.x = x
        self.y = y
        self.images = []
        self.advice = advice
        self.font = font
        self.demonstrable = True

        for file in im_name_file:
            self.images.append(pygame.image.load(f"foto_png/{file}"))

        self.w = self.images[0].get_width()
        self.h = self.images[0].get_height()

    def draw(self, scene, mouse_x, mouse_y, pressed):
        # Номер нажатой кнопки
        pressed_id_button = "NONE"
        if not self.demonstrable:
            return pressed_id_button

        # Если нажали...
        if self.get_mouse_btn(mouse_x, mouse_y) and pressed:
            scene.blit(self.images[1], (self.x - 25, self.y))
            self.write_advice(scene)
            pressed_id_button = self.id_button
        else:
            scene.blit(self.images[0], (self.x, self.y))

        if pressed:
            return pressed_id_button

        return "NONE"

    # Появление внизу подсказки при наведении курсора на кнопку
    def write_advice(self, scene):
        sc = self.font.getSystemText(f"N{self.y}", f"{self.hint}", COLOR_YELLOW_DARK)
        x = (WIDTH - sc.get_width()) // 2
        scene.blit(sc, (x, 80))
        ######scene.blit(sc, (x, HEIGHT - 40))

    # Местонахождение мыши по отношению к кнопке
    def get_mouse_btn(self, x, y):
        if self.x < x < self.x + self.w and self.y < y < self.y + self.h:
            return True
        return False
