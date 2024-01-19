# --------------- ФУНКЦИИ И МЕТОДЫ ---------------

# Загрузка данных из файла
def loading():
    ret = dict()
    try:
        file = open('setup.dat', 'r', encoding="UTF-8")
        data = file.readlines()
        file.close()
        for line in data:
            line = line.split("=")
            ret[line[0]] = line[1]
    except FileNotFoundError:
        reset()

    return ret

# Создание файла с данными по умолчанию
def reset():
    global dataload

    f = open("setup.dat", "w", encoding="UTF-8")

    f.write("level=0\n")
    f.write("max_level=0\n")
    f.write(f"error=0\n")
    f.write(f"difficulty=0\n")
    f.write(f"advice=2\n")
    f.close()

    dataload = loading()
    set_data()

# Установка значений
def set_data():
    global level, max_level, difficulty, error, advice

    #print(dataload)

    level = int(dataload["level"])
    max_level = int(dataload["max_level"])
    difficulty = int(dataload["difficulty"])
    error = int(dataload["error"])
    advice = int(dataload["advice"])

# Сохранение данных в файл
def save():
    f = open("setup.dat", "w", encoding="UTF-8")

    f.write(f"level={level}\n")
    f.write(f"max_level={max_level}\n")
    f.write(f"error={error}\n")
    f.write(f"difficulty={difficulty}\n")
    f.write(f"advice={advice}\n")

    f.close()


# --------------- НАЧАЛО ИГРЫ ---------------

# Цвет линий для текста
TEXT_COLOR = [(150, 190, 150), (150, 190, 50)]

# Подсветка текста
TEXT_LIGHT_BAD = "#A73737"
TEXT_LIGHT_GOOD = "#37A737"
TEXT_LIGHT_ATTENTION = "#936d36"
COLOR_WHITE = "#EFEFEF"
COLOR_GRAY = "#A7A7A7"
COLOR_DEEP_GRAY = "#373737"
COLOR_YELLOW = "#FFFF00"
COLOR_YELLOW_DARK = "#9d933a"
COLOR_RED = "#FF4747"


WIDTH = 1000
HEIGHT = 700
FPS = 120

# Размеры игры
game_sizes = []
for i in range(20):
    game_sizes.append(int(60 - i * 2.2))

# Процент скрытых чисел выражениями
percent_numbers = [30, 60, 100]

# Последний просмотренный уровень
# Максимально достигнутый уровень
# Количество допустимых ошибок
# Уровень игры
# Количество подсказок
level = None
max_level = None
error = None
difficulty = None
advice = None

see_example = None

dataload = loading()
if level is None:
    reset()
