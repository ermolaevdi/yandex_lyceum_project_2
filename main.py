import pygame

import tuning
from tuning import *
from game import Game
from add_map import AddMap
from buttons import Buttons
from start_screen import StartScreen
from sound import Sound


pygame.init()
pygame.display.set_caption("! Японские кроссворды by Dmitriy Ermolaev !")

size = [WIDTH, HEIGHT]
scene = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Началась ли игра?
game_status = True
time_difference = 0

# Карты для всех уровней игры
map = AddMap()
# Работа со всеми кнопками
button = Buttons()
# Звуки в игре
sound = Sound(pygame)
# Связка всей игры
game = Game(map, sound)
# Стартовое окно
start_screen = StartScreen()

# Кнопки-счетчики
mouse_btn_press1 = 0
mouse_btn_press2 = 0

if tuning.error < 8:
    sound.play(Sound.START_PLAY_GAME)
else:
    start_screen.enabled = False

# Пока "игра" работает...
while game_status:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_status = False
        # Если отсутствует пример для решения (для открытия числа)
        if tuning.see_example is None:
            if event.type == pygame.MOUSEBUTTONDOWN and not start_screen.enabled:
                if mouse_btn_press1 == 0 and event.button == 1:
                    sound.play(Sound.CLICK)
                    game.press_mouse_1(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                    game.set_filling(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                if mouse_btn_press2 == 0 and event.button == 3:
                    sound.play(Sound.CLICK)
                    game.set_blocked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

                mouse_btn_press1 = event.button
                mouse_btn_press2 = event.button

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_btn_press1 = 0
                mouse_btn_press2 = 0
        else:
            mouse_btn_press1 = 0
            mouse_btn_press2 = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    tuning.see_example.press_mouse_button_1(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    scene.fill("#1c3055")
    game.draw(scene, time_difference)

    if tuning.see_example is not None:
        button.draw(scene, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], False)
        tuning.see_example.draw(scene)
    elif not start_screen.enabled:
        pressed_btn = button.draw(scene, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], True)

        # Вывод информации "Об авторе"
        if pressed_btn == Buttons.AUTHOR:
            game.draw_authors(scene, time_difference)
        # Вывод правил игры
        if pressed_btn == Buttons.RULES:
            game.draw_play(scene, time_difference)

        # Обработка событий при нажатии различных клавиш
        if mouse_btn_press1 == 1 and pressed_btn != "NONE":
            mouse_btn_press1 = 0
            if pressed_btn == Buttons.CHECK:
                sound.play(Sound.CLICK)
                game.check_end_round()
            elif pressed_btn == Buttons.RESTART:
                sound.play(Sound.CLICK)
                game.start_level()
            elif pressed_btn == Buttons.ADVICE:
                sound.play(Sound.HELP)
                game.run_help()
            elif pressed_btn == Buttons.D30:
                sound.play(Sound.COMPLEXITY)
                tuning.difficulty = 1
                game.start_level()
            elif pressed_btn == Buttons.D60:
                sound.play(Sound.COMPLEXITY)
                tuning.difficulty = 2
                game.start_level()
            elif pressed_btn == Buttons.D100:
                sound.play(Sound.COMPLEXITY)
                tuning.difficulty = 0
                game.start_level()
            elif pressed_btn == Buttons.NEXT:
                sound.play(Sound.CLICK)
                tuning.level += 1
                if tuning.level == len(game.maps.level) or tuning.level == tuning.max_level + 1:
                    tuning.level -= 1
                game.start_level()
            elif pressed_btn == Buttons.PREV:
                sound.play(Sound.CLICK)
                tuning.level -= 1
                if tuning.level < 0:
                    tuning.level = 0
                else:
                    game.start_level()
            elif pressed_btn == Buttons.EXIT:
                tuning.save()
                game_status = False
            elif pressed_btn == Buttons.RESET:
                sound.play(Sound.CLICK)
                tuning.reset()
                game.gamestate = Game.PLAY_GAME
                game.start_level()

    if start_screen.alpha > 0:
        start_screen.draw(scene, time_difference)

    pygame.display.flip()

    # Задействуем функционал основного поля (и "мышки"), если окно с заданиями не используется
    if tuning.see_example is None:
        if mouse_btn_press1 == 1:
            game.mouse_1_button_down(mouse_btn_press1, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        if mouse_btn_press2 == 3:
            game.mouse_3_button_down(mouse_btn_press2, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    game.act(time_difference, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    time_difference = clock.tick(FPS) / 1000

pygame.quit()
tuning.save()
