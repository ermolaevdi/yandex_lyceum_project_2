import pygame


pygame.init()
pygame.display.set_caption("Японские кроссворды")

WIDTH = 1000
HEIGHT = 700
FPS = 120

size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Началась ли игра?
game = True
time_difference = 0


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
    f = open("setup.dat", "w", encoding="UTF-8")

    f.write("level=0\n")
    f.write("max_level=0\n")
    f.write(f"error=0\n")
    f.write(f"difficulty=0\n")
    f.write(f"advice=5\n")

    f.close()
    set_data()

# Установка значений
def set_data():
    global level, max_level, difficulty, error, advice

    dataload = loading()

    ###### -
    print(dataload)

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
#####

# Подсветка текста
#####

# Размеры игры
game_sizes = []
for i in range(20):
    game_sizes.append(int(60 - i * 2.2))

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

##### Исправить! (не работает при первом запуске - ошибка)
##### set_data()

# Процент скрытых чисел для выражений
percent_numbers = [30, 60, 100]


pygame.quit()
###### save()
