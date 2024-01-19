import random

from tuning import *
from data import Data


class Vertical:
    def __init__(self, maps, x_start, y_start, cell_size, font):

        self.data_lines = []
        self.font = font

        maps_x = 0
        maps_len_1 = len(maps[0])
        maps_len_2 = len(maps)

        for x in range(maps_len_1):
            data = []
            cnt = 0

            for y in range(maps_len_2):
                cnt += maps[y][x]
                if (maps[y][x] == 0) and (cnt > 0):
                    data.append(cnt)
                    cnt = 0

            if cnt > 0:
                data.append(cnt)

            self.data_lines.append(Data(x_start + x * cell_size,
                                        y_start - 30, cell_size,
                                        data, font, TEXT_COLOR[x % 2],
                                        Data.VERTICAL))

            if len(data) > maps_x:
                maps_x = len(data)

        self.width = cell_size * maps_x

        # Определяем выражения для вычисления всех "закрытых" чисел
        self.set_expression_digit()

    # Активируем пример нажатием мыши
    def press_mouse_1(self, x, y):
        for i in range(len(self.data_lines)):
            self.data_lines[i].press_mouse_1(x, y)

    def check_mouse(self, x, y):
        for i in range(len(self.data_lines)):
            self.data_lines[i].check_mouse(x, y)

    def draw(self, scene):
        for i in range(len(self.data_lines)):
            self.data_lines[i].draw(scene)

    # Преобразовываем выражения
    def set_expression_digit(self):
        res = []
        for data_l in self.data_lines:
            for cell in data_l.cells:
                res.append(cell)

        count = int(len(res) / 100 * percent_numbers[difficulty])

        random.shuffle(res)

        for i in range(count):
            res[i].set_error_digit()
