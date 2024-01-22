import pygame


class FinalText:

    def __init__(self, msg1, msg2, name_image, font, left_x, right_x):

        self.message_1 = font.getBigText("MSG1", msg1, "#dd9587")
        self.message_2 = font.getSmallText("MSG2", msg2, "#AAAA99")

        self.message_1x = (right_x - left_x - self.message_1.get_width()) // 2
        self.message_2x = (right_x - left_x - self.message_2.get_width()) // 2

        self.img = pygame.image.load(name_image)
        self.img_x = (right_x - left_x - self.img.get_width()) // 2
        self.font = font
        self.alpha = 0

    def draw(self, scene: pygame.Surface, delta_time):
        if self.alpha < 255:
            self.alpha += 125 * delta_time
            if self.alpha > 255:
                self.alpha = 255

        self.message_1.set_alpha(int(self.alpha))
        self.message_2.set_alpha(int(self.alpha))
        self.img.set_alpha(int(self.alpha))

        scene.blit(self.message_1, (self.message_1x, 100))
        scene.blit(self.message_2, (self.message_2x, 620))

        scene.blit(self.img, (self.img_x, 250))
