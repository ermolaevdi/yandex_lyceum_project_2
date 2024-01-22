import random

import tuning
from data_lines import DataLines


class Vertical:

    def __init__(self, maps, start_x, start_y, cell_size, font):

        self.font = font
        self.data_lines = []

        maps_x = 0

        for x in range(len(maps[0])):
            data = []
            cnt = 0

            for y in range(len(maps)):
                cnt += maps[y][x]
                if maps[y][x] == 0 and cnt > 0:
                    data.append(cnt)
                    cnt = 0

            if cnt > 0:
                data.append(cnt)

            self.data_lines.append(DataLines(start_x + x * cell_size,
                                             start_y - 30, cell_size,
                                             data,
                                             font,
                                             tuning.TEXT_COLOR[x % 2],
                                             DataLines.VERTICAL))

            if len(data) > maps_x:
                maps_x = len(data)

        self.width = maps_x * cell_size

        # Определяем выражения для вычисления всех "закрытых" чисел
        self.set_expression_digit()

    def check_mouse(self, x, y):
        for i in range(len(self.data_lines)):
            self.data_lines[i].check_mouse(x, y)

    def draw(self, scene):
        for i in range(len(self.data_lines)):
            self.data_lines[i].draw(scene)

    # Активируем пример нажатием мыши
    def press_mouse_1(self, x, y):
        for i in range(len(self.data_lines)):
            self.data_lines[i].press_mouse_1(x, y)

    # Преобразовываем выражения
    def set_expression_digit(self):
        res = []
        for data_l in self.data_lines:
            for cell in data_l.cells:
                res.append(cell)

        count = int(len(res) / 100 * tuning.percent_numbers[tuning.difficulty])

        random.shuffle(res)

        for i in range(count):
            res[i].set_error_digit()
