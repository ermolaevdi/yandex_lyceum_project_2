from tuning import *

from vertcl_maps import Vertical
from data import Data


class Horizontal(Vertical):
    def __init__(self, maps, x_start, y_start, cell_size, font):

        self.data_lines = []
        self.font = font

        maps_x = 0

        for x in range(len(maps)):
            data = []
            cnt = 0

            for y in range(len(maps[0])):
                cnt += maps[x][y]
                if (maps[x][y] == 0) and (cnt > 0):
                    data.append(cnt)
                    cnt = 0

            if cnt > 0:
                data.append(cnt)

            self.data_lines.append(Data(x_start - cell_size,
                                        y_start + cell_size * x + (cell_size - 23) // 2,
                                        cell_size, data, font,
                                        TEXT_COLOR[x % 2],
                                        Data.HORIZONTAL))

            if len(data) > maps_x:
                maps_x = len(data)

        self.height = cell_size * maps_x

        # Определяем выражения для вычисления всех "закрытых" чисел
        self.set_expression_digit()
