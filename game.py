import random

import pygame

import tuning
from tuning import *
from square import Square
from horizontal import Horizontal
from vertical import Vertical
from errors import Error
from font import Font
from label_text import LabelText
from label_text_central import LabelTextCentral
from helper import Helper
from creator_text import CreatorText
from play_txt import PlayTxt
from sound import Sound
from final_text import FinalText


class Game:
    PLAY_GAME = 0
    END_GAME = 1
    WIN_GAME = 2

    def __init__(self, maps, sound):
        self.gamestate = Game.PLAY_GAME

        # Текст для победы или поражения игрока
        self.final_text = None

        self.width = None
        self.height = None
        self.maps = maps
        self.current_map = None
        self.sound = sound
        self.fields = None
        self.horizontal = None
        self.vertical = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.i_line_cells = None
        self.j_line_cells = None
        self.size_field = None
        self.field_i = None
        self.field_j = None
        self.fill = True
        self.blocked = True
        self.end_round_effect = None

        # Подключаем шрифты
        self.font = Font()
        # Анимация ошибок
        self.errors = []
        # Анимация подсказок
        self.helper = []
        # "Об авторе"
        self.author = CreatorText(self.font)
        # Правила игры
        self.rules_play = PlayTxt(self.font)
        # Текстовые сообщения на экране
        self.label_text = LabelText(self.font)
        # Ведём подсчёт кадров
        self.frame = 0
        # Предотвращаем повторение ошибок на одни и те же клетки
        self.i_error = -1
        self.j_error = -1
        # Текстовые сообщения в конце уровня
        self.label_text_central = None

        self.start_level()


    # Очищаем экран
    def clear_lists(self, tmp):
        if tmp is not None:
            for i in range(len(tmp) - 1, -1, -1):
                del tmp[i]
        return []

    # "Старт" уровня головоломки
    def start_level(self):
        self.final_text = None
        # Сбрасываем надпись на экране
        self.label_text_central = self.clear_lists(self.label_text_central)
        # Сбрасываем все использующиеся эффекты
        self.end_round_effect = self.clear_lists(self.end_round_effect)

        if tuning.level >= len(self.maps.level):
            tuning.reset()

        # Текущая карта
        self.current_map = self.maps.level[tuning.level].data_level
        self.fields = [p[:] for p in self.current_map]

        # В зависимости от количества клеток на экране определяем размер клетки
        self.size_field = game_sizes[max(len(self.fields), len(self.fields[0])) - 1]

        # Ширина и высота игрового поля в клетках
        self.field_i = len(self.current_map)
        self.field_j = len(self.current_map[0])

        # Вся подсчитанная ширина и высота поля
        self.width = self.field_j * self.size_field
        self.height = self.field_i * self.size_field

        self.start_x = (795 - self.width) // 2
        self.start_y = (HEIGHT - self.height) // 2 + 100

        self.horizontal = Horizontal(self.current_map, self.start_x, self.start_y, self.size_field, self.font)
        self.vertical = Vertical(self.current_map, self.start_x, self.start_y, self.size_field, self.font)

        self.start_x = (795 - self.width + self.vertical.width) // 2
        self.start_y = (HEIGHT - self.height - self.horizontal.height) // 2 + 100
        self.end_x = self.start_x + self.size_field * self.field_j
        self.end_y = self.start_y + self.size_field * self.field_i

        self.start_y = (tuning.HEIGHT - self.height + 50) // 2

        for i in range(len(self.fields)):
            for j in range(len(self.fields[i])):
                self.fields[i][j] = Square(self.start_x + j * self.size_field,
                                           self.start_y + i * self.size_field,
                                           self.size_field)
                # ЧИТ
                # self.fields[i][j].enabled = self.current_map[i][j]

        self.horizontal = Horizontal(self.current_map, self.start_x, self.start_y, self.size_field, self.font)
        self.vertical = Vertical(self.current_map, self.start_x, self.start_y, self.size_field, self.font)

        score = [1, 2, 3, 4, 5]

        for i in score:
            if len(self.fields) % i == 0:
                self.i_line_cells = i

        for j in score:
            if len(self.fields) % j == 0:
                self.j_line_cells = j

        # Проверка на количество ошибок
        if tuning.error >= 8:
            self.end_game()

    # Обработка и получение координат
    def getCoord(self, b, a):
        if (b < self.start_x) or (b >= self.end_x) or (a < self.start_y) or (a >= self.end_y):
            return -1, -1

        a = min(len(self.fields) - 1, (a - self.start_y) // self.size_field)
        b = min(len(self.fields[0]) - 1, (b - self.start_x) // self.size_field)

        return b, a

    # Используем функционал основного поля (и "мышки")
    def press_mouse_1(self, x, y):
        if not (self.vertical is None):
            self.vertical.press_mouse_1(x, y)
        if not (self.horizontal is None):
            self.horizontal.press_mouse_1(x, y)

    def mouse_3_button_down(self, mouse, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False
        self.fields[i][j].blocked = self.blocked

    def set_blocked(self, j, i):
        j, i = self.getCoord(j, i)
        if j == -1 and i == -1:
            return False

        self.blocked = not self.fields[i][j].blocked

    # Диагностика
    def act(self, deltatime, x, y):
        self.frame += 1
        if self.frame > 100000:
            self.frame = 1

        if not (self.vertical is None):
            self.vertical.check_mouse(x, y)

        if not (self.horizontal is None):
            self.horizontal.check_mouse(x, y)

        if self.frame % 30 == 0:
            # Удаляем ошибочные квадраты после нажатия
            for i in range(len(self.errors) - 1, -1, -1):
                if not self.errors[i].enabled:
                    del self.errors[i]

            # Удаляем квадраты с подсказками
            for i in range(len(self.helper) - 1, -1, -1):
                if not self.helper[i].enabled:
                    del self.helper[i]

            if not (self.label_text_central is None):
                for i in range(len(self.label_text_central) - 1, -1, -1):
                    if not self.label_text_central[i].enabled:
                        del self.label_text_central[i]
            if not (self.end_round_effect is None):
                for i in range(len(self.end_round_effect) - 1, -1, -1):
                    if not self.end_round_effect[i].enabled:
                        del self.end_round_effect[i]

    # Обрабатываем и выводим на экран наполнение вложенных
    # объектов классов в зависимости от состояния игры
    def draw(self, scene: pygame, deltatime):

        """ --------------- ВРЕМЯ ИГРЫ --------------- """
        if self.gamestate == Game.PLAY_GAME:

            for i in range(len(self.fields)):
                for j in range(len(self.fields[i])):
                    self.fields[i][j].drawIJ(scene, j, i, self.i_line_cells, self.j_line_cells)

            if self.end_round_effect is not None:
                for effect in self.end_round_effect:
                    effect.draw(scene, deltatime)

            # Анимация ошибок
            if len(self.errors) > 0:
                for err in self.errors:
                    err.draw(scene, deltatime)

            # Анимация клеток с подсказками
            if len(self.helper) > 0:
                for cell_help in self.helper:
                    cell_help.draw(scene, deltatime)

            pygame.draw.rect(scene, Square.color_fill, (self.start_x - 3, self.start_y - 3,
                                                        self.width + 6, self.height + 6), 1)
            if not (self.vertical is None):
                self.vertical.draw(scene)
            if not (self.horizontal is None):
                self.horizontal.draw(scene)

            """ --------------- ПРОИГРЫШ --------------- """
        elif self.gamestate == Game.END_GAME:
            if self.final_text is not None:
                self.final_text.draw(scene, deltatime)

            """ --------------- ПОБЕДА --------------- """
        elif self.gamestate == Game.WIN_GAME:
            if self.final_text is not None:
                self.final_text.draw(scene, deltatime)

        self.label_text.draw(scene)
        if self.label_text_central is not None:
            for txt_cntr in self.label_text_central:
                txt_cntr.draw(scene, deltatime)

    # Установка и изменение состояния заливки
    def set_filling(self, b, a):
        b, a = self.getCoord(b, a)
        if b == -1 and a == -1:
            return False
        self.fill = not self.fields[a][b].enabled

    # Подсчёт ошибок при нажатии мышкой по игровому полю
    def mouse_1_button_down(self, mouse, b, a):
        b, a = self.getCoord(b, a)
        if b == -1 and a == -1:
            return False

        if self.fields[a][b].blocked:
            return False
        if mouse == 1:
            self.fields[a][b].enabled = self.fill

            if self.fill:
                if self.i_error != a or self.j_error != b:
                    self.i_error = a
                    self.j_error = b
                    if self.current_map[a][b] == 0:
                        self.sound.play(Sound.CLICK_BAD)
                        self.errors.append(Error(self.fields[a][b], FPS / 2))
                        tuning.error += 1
                        self.fields[a][b].blocked = True
                        self.fields[a][b].enabled = False
                        self.i_error = -1
                        self.j_error = -1
                        if tuning.error >= 8:
                            # Удаляем квадратов с ошибками
                            self.end_game()

    # Вывод клеток с подсказками
    # Важно: количество незакрашенных клеток / 3, но их количество больше или равно 1
    def run_help(self):
        if len(self.helper) > 0:
            return False
        if tuning.advice == 0:
            return False

        clean_field = []

        for i in range(len(self.current_map)):
            for j in range(len(self.current_map[i])):
                if self.current_map[i][j] == 1 and self.fields[i][j].enabled == False:
                    clean_field.append([self.fields[i][j], i, j])

        if len(clean_field) > 0:
            tuning.advice -= 1

            random.shuffle(clean_field)
            count = min(max(len(clean_field) // 3, 1), 3)
            for i in range(count):
                self.helper.append(Helper(clean_field[i][0], tuning.FPS // 2))
                self.fields[clean_field[i][1]][clean_field[i][2]].enabled = True

    # Кнопка "Проверить"
    # Дополнительно вывод количества ошибок и текстовое уведомление
    def check_end_round(self):
        cnt_clear = 0
        cnt_fill = 0
        cnt_block = 0
        for i in range(len(self.current_map)):
            for j in range(len(self.current_map[i])):
                if self.current_map[i][j] == 1 and not self.fields[i][j].enabled and self.fields[i][j].blocked:
                    cnt_block += 1
                elif self.current_map[i][j] == 1 and not self.fields[i][j].enabled:
                    cnt_fill += 1
                elif self.current_map[i][j] == 0 and self.fields[i][j].enabled:
                    cnt_clear += 1

        if cnt_fill + cnt_clear + cnt_block > 0:
            str_err_clear = self.choosePluralMerge(cnt_clear, "поле", "поля", "полей")
            str_err_fill = self.choosePluralMerge(cnt_fill, "поле", "поля", "полей")
            str_err_block = self.choosePluralMerge(cnt_block, "поле", "поля", "полей")

            string_out = ""
            if cnt_block > 0:
                string_out = f"Наобходимо разблокировать {str_err_block}"
            elif cnt_clear > 0 and cnt_fill > 0:
                string_out = f"Необходимо закрасить: {str_err_fill}, а {str_err_clear} очистить"
            elif cnt_clear > 0 and cnt_fill == 0:
                string_out = f"Необходимо очистить {str_err_clear}"
            elif cnt_clear == 0 and cnt_fill > 0:
                string_out = f"Необходимо закрасить {str_err_fill}"

            self.label_text_central.append(
                LabelTextCentral(tuning.HEIGHT - 80, string_out, f"ERR{cnt_fill + cnt_clear + cnt_block}",
                                 tuning.TEXT_LIGHT_BAD,
                                 self.font, tuning.FPS * 3,
                                 2))

            self.sound.play(Sound.CLICK_BAD)
            tuning.error += 1

            if tuning.error >= 8:
                self.end_game()
        else:
            self.sound.play(Sound.UP_OR_DOWN)
            self.win_round()

    def choosePluralMerge(self, num, event_1, event_2, event_5):
        res = f"{num} "
        num = abs(num)
        if num % 10 == 1 and num % 100 != 11:
            res += event_1
        elif num % 10 >= 2 and num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20):
            res += event_2
        else:
            res += event_5

        return res

    # Уровень головоломки пройден - что дальше?
    def win_round(self):
        tuning.max_level = max(tuning.level + 1, tuning.max_level)
        tuning.max_level = min(tuning.max_level, len(self.maps.level) - 1)

        # Ограничение на использование подсказок
        tuning.advice += 1
        if tuning.advice > 3:
            tuning.advice = 3

        if tuning.level + 1 == len(self.maps.level):
            self.final_text = FinalText("Молодцы! Вы смогли одолететь эту головоломку!",
                                        "Поздравляем, Вы решили абсолютно все кросссворды!",
                                        "foto_png/win.png", self.font, 0, 795)
            self.gamestate = Game.WIN_GAME
        else:
            win_txt = 'Нажмите кнопку "Следующая" для продолжения'
            self.label_text_central.append(LabelTextCentral(tuning.HEIGHT - 70, win_txt, f"TEXTWIN",
                                                            tuning.COLOR_GRAY,
                                                            self.font, tuning.FPS * 10,
                                                            1))

            level_txt = f'"{self.maps.level[tuning.level].name_level}"'
            self.label_text_central.append(LabelTextCentral(tuning.HEIGHT - 110, level_txt, f"TEXTNAME",
                                                            tuning.TEXT_LIGHT_GOOD,
                                                            self.font, tuning.FPS * 20,
                                                            2))

        if len(self.end_round_effect) > 300:
            return False

        count = 0
        interval = tuning.FPS
        line = 0
        augment = tuning.FPS / 30
        for j in range(self.field_j):
            for i in range(self.field_i):
                if (line % 2) == 0:
                    if self.current_map[i][j] == 1:
                        self.end_round_effect.append(Helper(self.fields[i][j], interval, int(count), 0, 100, 0))
                        count += augment

                    if self.current_map[self.field_i - 1 - i][self.field_j - 1 - j] == 1:
                        self.end_round_effect.append(
                            Helper(self.fields[self.field_i - 1 - i][self.field_j - 1 - j], interval,
                                   int(count), 0, 100, 0))
                        count += augment

                else:
                    if self.current_map[self.field_i - 1 - i][j] == 1:
                        self.end_round_effect.append(
                            Helper(self.fields[self.field_i - 1 - i][j], interval, int(count), 0, 100, 0))
                        count += augment

                    if self.current_map[i][self.field_j - 1 - j] == 1:
                        self.end_round_effect.append(
                            Helper(self.fields[i][self.field_j - 1 - j], interval, int(count), 0, 100, 0))
                        count += augment
            line += 1

    def draw_play(self, scene, deltatime):
        self.rules_play.draw(scene, deltatime)

    def draw_authors(self, scene, deltatime):
        self.author.draw(scene, deltatime)

    # Окончание игры
    def end_game(self):
        if self.errors is not None:
            for i in range(len(self.errors) - 1, -1, -1):
                del self.errors[i]
        self.errors = []

        # Удаляем квадраты с подсказками
        if self.helper is not None:
            for i in range(len(self.helper) - 1, -1, -1):
                del self.helper[i]
        self.helper = []

        if self.label_text_central is not None:
            for i in range(len(self.label_text_central) - 1, -1, -1):
                del self.label_text_central[i]
        self.label_text_central = []

        if self.end_round_effect is not None:
            for i in range(len(self.end_round_effect) - 1, -1, -1):
                del self.end_round_effect[i]
        self.end_round_effect = []

        self.sound.play(Sound.GAME_OVER)

        self.final_text = FinalText("К сожалению, Вы проиграли...", "Превышен лимит 8 ошибок. "
                                                                "Нажмите \"Сбросить прогресс\", чтобы начать заново!",
                                    "foto_png/game_over.png", self.font, 0, 795)

        self.gamestate = Game.END_GAME
