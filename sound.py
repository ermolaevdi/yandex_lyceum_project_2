class Sound:
    # Номера звуковых сигналов
    START = 0
    CLICK = 1
    CLICK_BAD = 2
    HELP = 3
    UP_OR_DOWN = 4
    COMPLEXITY = 5
    START_PLAY_GAME = 6
    GAME_OVER = 7

    def __init__(self, pygame):
        pygame.mixer.music.set_volume(0.6)

        self.sounds = []
        self.sounds.append(pygame.mixer.Sound("sound/start.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/good.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/bad.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/help.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/up_down.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/complexity.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/play_game.mp3"))
        self.sounds.append(pygame.mixer.Sound("sound/game_over.mp3"))

    def play(self, num):
        self.sounds[num].play()
