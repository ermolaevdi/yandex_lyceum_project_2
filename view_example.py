import pygame

import tuning
from font import Font
from square import Square
from random import randint


class ViewExample:
    class Button:

        def __init__(self, x, y, width, height, font, value):

            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.font = font
            self.value = value

        def draw(self, scene):
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]

            if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
                pygame.draw.rect(scene, tuning.TEXT_LIGHT_GOOD, (self.x, self.y, self.width, self.height))
                pygame.draw.rect(scene, Square.color_fill, (self.x, self.y, self.width, self.height), 2)
                scene.blit(self.font.getMediumText(f"BTN{self.value}", f"{self.value}", tuning.COLOR_WHITE),
                           (self.x + 9, self.y + 2))

            else:
                pygame.draw.rect(scene, Square.color, (self.x, self.y, self.width, self.height))
                pygame.draw.rect(scene, Square.color_fill, (self.x, self.y, self.width, self.height), 2)
                scene.blit(self.font.getMediumText(f"BTN{self.value}", f"{self.value}", tuning.COLOR_WHITE),
                           (self.x + 9, self.y + 2))


        def press_mouse(self, x, y):
            if (self.x < x < self.x + self.width) and (self.y < y < self.y + self.height):
                return f"{self.value}"
            return False

    def __init__(self, x, y, size_field, value, cell):
        self.x = x + size_field
        self.y = y
        self.size_field = size_field
        self.value = value
        self.cell = cell

        self.font = Font()
        self.msg = ""
        self.in_data = ""
        self.frame = 0

        if value > 4 and randint(0, 100) < 50:
            n = randint(1, value)
            self.msg = f"{n} + {value - n} = "
        else:
            n = randint(value + 1, 10 + value ** 2)
            self.msg = f"{n} - {n - value} = "

        self.width = 375
        self.height = 180
        self.x -= self.width // 4 + size_field
        self.y -= self.height // 4 + size_field

        if self.y + self.height + 20 > tuning.HEIGHT:
            self.y = self.height + self.height + 20
        if self.y - self.height - 20 <= 0:
            self.y = 20
        if self.x + self.width + 20 >= tuning.WIDTH:
            self.x = tuning.WIDTH - self.width - 20

        if self.x < 20:
            self.x = 20

        self.buttons = []

        for i in range(10):
            self.buttons.append(self.Button(self.x + 15 + i * 35, self.y + 100, 30, 30, self.font, i))
        self.buttons.append(self.Button(self.x + 15, self.y + 135, 53, 30, self.font, "<<<"))
        self.buttons.append(self.Button(self.x + 73, self.y + 135, 73, 30, self.font, "Ввод"))

    def draw(self, scene):
        self.frame += 1

        if self.frame < tuning.FPS // 2:
            cursor = "|"
        else:
            cursor = ""

        if self.frame > tuning.FPS:
            self.frame = 0

        pygame.draw.rect(scene, Square.color_line, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(scene, Square.color_fill, (self.x, self.y, self.width, self.height), 5)
        scene.blit(self.font.getMediumText("CAPTION", "Решите пример:", tuning.COLOR_WHITE), (self.x + 15, self.y + 10))
        scene.blit(self.font.getBigText("EXAMPLE", self.msg + self.in_data + cursor, tuning.COLOR_YELLOW),
                   (self.x + 15, self.y + 50))

        for i in range(len(self.buttons)):
            self.buttons[i].draw(scene)

    def press_mouse_button_1(self, x, y):
        for btn in self.buttons:
            res = btn.press_mouse(x, y)
            if res != False:
                if self.in_data == "" and res == "0":
                    return False
                elif res == "<<<":
                    if len(self.in_data) > 0:
                        self.in_data = self.in_data[:-1]
                elif res == "Ввод":
                    self.enter(self.in_data, False)
                else:
                    if len(self.in_data) == 2:
                        self.in_data = self.in_data[:-1]
                    self.in_data += res

        if len(self.in_data) > 0:
            if self.in_data == f"{self.cell.value}":
                self.enter(self.in_data, True)

        return True

    def enter(self, res, b):
        if res == "":
            self.cell.delete_view_example()
        else:
            self.cell.screen = res
            if b:
                self.cell.error_digit = False
                
        self.cell.delete_view_example()
