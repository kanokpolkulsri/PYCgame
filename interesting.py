import arcade
import arcade.sound

class sound:
    def __init__(self, screen):
        self.bg_sound = arcade.sound.load_sound('sounds/bgSound.mp3')

    def playing_sound(self):
        self.bg_sound.play()