import arcade
from calculation import score

class render:

    def __init__(self):
        self.bg = arcade.Sprite('images/bg.psd')
        self.bg.set_position(500, 250)
        self.prs = arcade.Sprite('images/prs.png')
        self.prs.set_position(500, 250)

        self.left = arcade.Sprite('images/cha1.png')
        self.left.set_position(100,100)

        

    def print(self):
        print(score.score_left)

    def screen_draw(self):
        self.bg.draw()
        self.prs.draw()
        self.left.draw()