from vertical import Vertical

import tuning
from data_lines import DataLines


class Horizontal(Vertical):

    def __init__(self, maps, start_x, start_y, cell_size, font):

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

            self.data_lines.append(DataLines(start_x - cell_size,
                                             start_y + cell_size * x + (cell_size - 23) // 2,
                                             cell_size, data,
                                             font,
                                             tuning.TEXT_COLOR[x % 2],
                                             DataLines.HORIZONTAL))
            if len(data) > maps_x:
                maps_x = len(data)

        self.height = maps_x * cell_size

        # Определяем выражения для вычисления всех "закрытых" чисел
        self.set_expression_digit()
