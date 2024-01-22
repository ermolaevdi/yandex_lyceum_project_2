import pygame
from tuning import *

class Button:

    def __init__(self, id_button, x, y, images_file_name, hint, font):
        self.id_button = id_button
        self.x = x
        self.y = y
        self.images = []
        self.hint = hint
        self.font = font
        self.visible = True

        for file in images_file_name:
            self.images.append(pygame.image.load(f"png/{file}"))

        self.width = self.images[0].get_width()
        self.height = self.images[0].get_height()

    def get_mouse_in_button(self, x, y):
        if self.x < x < self.x + self.width and \
                self.y < y < self.y + self.height:
            return True
        return False

    def draw(self, scene, mouse_x, mouse_y, pressable):
        pressed_id_button = "NONE"

        if not self.visible:
            return pressed_id_button

        if self.get_mouse_in_button(mouse_x, mouse_y) and pressable:
            scene.blit(self.images[1], (self.x - 25, self.y))
            self.draw_hint(scene)
            pressed_id_button = self.id_button
        else:
            scene.blit(self.images[0], (self.x, self.y))

        if pressable:
            return pressed_id_button

        return "NONE"

    # Вывод подсказки при активной кнопке
    def draw_hint(self, scene):
        sc = self.font.getSystemText(f"N{self.y}",
                                        f"{self.hint}",
                                        COLOR_YELLOW_DARK)
        x = (WIDTH - sc.get_width()) // 2
        scene.blit(sc, (x, HEIGHT - 40))
