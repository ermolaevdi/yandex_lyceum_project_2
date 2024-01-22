import pygame

import tuning
from font import Font


class Buttons:

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

    def __init__(self):

        self.buttons = []
        font = Font()

        self.buttons.append(Button(Buttons.CHECK, 790, 150, ["4.png", "3.png"],
                                   "Проверить правильность решения? "
                                   "Помни, что счётчик ошибок может увеличиться :)", font))
        self.buttons.append(Button(Buttons.RESTART, 790, 230, ["24.png", "23.png"],
                                   "Начать прохождение уровня заново", font))
        self.buttons.append(Button(Buttons.ADVICE, 790, 290, ["8.png", "7.png"],
                                   "Открыть любые 1-3 клетки", font))

        self.buttons.append(Button(Buttons.NEXT, 790, 440, ["16.png", "15.png"],
                                   "Следующий уровень", font))
        self.buttons.append(Button(Buttons.PREV, 790, 470, ["18.png", "17.png"],
                                   "Предыдущий уровень", font))
        self.buttons.append(Button(Buttons.RULES, 790, 530, ["20.png", "19.png"],
                                   "Правила игры", font))
        self.buttons.append(Button(Buttons.EXIT, 790, 570, ["6.png", "5.png"],
                                   "Выйти из головоломки", font))
        self.buttons.append(Button(Buttons.RESET, 790, 600, ["22.png", "21.png"],
                                   "Сбросить весь прогресс", font))

        # Кнопки для выставления сложности
        self.buttons_difficulty = []
        self.buttons_difficulty.append(Button(Buttons.D30, 790, 320, ["10.png", "9.png"],
                                              "Меньше половины чисел скрыто выражениями", font))
        self.buttons_difficulty.append(Button(Buttons.D60, 790, 320, ["12.png", "11.png"],
                                              "Больше половины чисел скрыто выражениями", font))
        self.buttons_difficulty.append(Button(Buttons.D100, 790, 320, ["14.png", "13.png"],
                                              "Все числа скрыты выражениями", font))

        self.buttons.append(Button(Buttons.AUTHOR, 790, 640, ["2.png", "1.png"],
                                   "Разработчик игры", font))

    def draw(self, scene, mouse_x, mouse_y, pressable):
        return_id_button = "NONE"
        res = "NONE"
        for btn in self.buttons:
            if btn.id_button == Buttons.ADVICE and tuning.advice > 0 and tuning.error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressable)
            elif btn.id_button == Buttons.NEXT and tuning.level < tuning.max_level and tuning.error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressable)
            elif btn.id_button == Buttons.PREV and tuning.level > 0 and tuning.error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressable)
            elif btn.id_button != Buttons.ADVICE and \
                 btn.id_button != Buttons.NEXT and \
                 btn.id_button != Buttons.PREV and tuning.error < 8:
                res = btn.draw(scene, mouse_x, mouse_y, pressable)
            elif tuning.error >= 8 and (btn.id_button == Buttons.EXIT or btn.id_button == Buttons.RESET):
                res = btn.draw(scene, mouse_x, mouse_y, pressable)

            if res != "NONE":
                return_id_button = res

        if tuning.error < 8:
            res = self.buttons_difficulty[tuning.difficulty].draw(scene, mouse_x, mouse_y, pressable)

        if res != "NONE":
            return_id_button = res

        return return_id_button

class Button:

    def __init__(self, id_button, x, y, images_file_name, hint, font):
        self.id_button = id_button
        self.x = x
        self.y = y
        self.images = []
        self.hint = hint
        self.font = font
        self.visible = True

        for file in images_file_name:
            self.images.append(pygame.image.load(f"foto_png/{file}"))

        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()

    def get_mouse_in_button(self, x, y):
        if self.x < x < self.x + self.width and \
                self.y < y < self.y + self.height:
            return True
        return False

    def draw(self, scene, mouse_x, mouse_y, pressable):
        # Номер нажатой кнопки
        pressed_id_button = "NONE"
        if not self.visible:
            return pressed_id_button

        # Если нажали...
        if self.get_mouse_in_button(mouse_x, mouse_y) and pressable:
            scene.blit(self.images[1], (self.x - 25, self.y))
            self.draw_hint(scene)
            pressed_id_button = self.id_button
        else:
            scene.blit(self.images[0], (self.x, self.y))

        if pressable:
            return pressed_id_button

        return "NONE"

    # Появление вверху подсказки при наведении курсора на кнопку
    def draw_hint(self, scene):
        sc = self.font.getSystemText(f"N{self.y}",
                                        f"{self.hint}",
                                        tuning.COLOR_YELLOW_DARK)
        x = (tuning.WIDTH - sc.get_width()) // 2
        scene.blit(sc, (x, 80))
