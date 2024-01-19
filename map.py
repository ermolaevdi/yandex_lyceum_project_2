class Map:

    def __init__(self, name_level, data_level):

        # Название уровня
        self.name_lvl = name_level
        # Игровое поле уровня
        self.data_lvl = data_level

    @property
    def data_level(self):
        return self.data_lvl

    @property
    def name_level(self):
        return self.name_lvl


class AddMap:

    def __init__(self):

        self.level = []
        self.level.append(Map("Квадрат", [[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
        self.level.append(Map("Цветок", [[0, 1, 1, 1, 0],
                                       [1, 1, 0, 1, 1],
                                       [1, 0, 0, 0, 1],
                                       [1, 1, 0, 1, 1],
                                       [0, 1, 1, 1, 0]]))
