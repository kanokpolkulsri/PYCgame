import arcade
import arcade.sound

class sound:
    def __init__(self, screen):
        self.screen = screen
        self.bgsound = arcade.sound.load_sound('sounds/bgSound.mp3')
        self.win = arcade.sound.load_sound('sounds/yeah.mp3')
        self.canplay = True

    def play_bg_sound(self):
        self.bgsound.play()

    def play_game_sound(self):
        if (self.screen.score.score_left == 3 or self.screen.score.score_right == 3) and self.canplay == True:
            self.win.play()
            self.canplay = False
        elif self.screen.score.score_left == 1 or self.screen.score.score_right == 1:
            self.canplay = True
