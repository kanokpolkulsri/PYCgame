import arcade
from calculation import score
class render:
    def __init__(self):
        self.bg = arcade.Sprite('images/bg.psd')
        self.bg.set_position(500, 250)

    def print(self):
        print(score.score_left)

    def screen_draw(self):
        self.bg.draw()