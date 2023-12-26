import pygame

from tuning import *
from map import *
from btns import Buttons


pygame.init()
pygame.display.set_caption("Японские кроссворды")

size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()


# Началась ли игра?
game = True
time_difference = 0


# Карты для всех уровней игры
map = AddMap()
# Работа со всеми кнопками
button = Buttons()


pygame.quit()
save()
