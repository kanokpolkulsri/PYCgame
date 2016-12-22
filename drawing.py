import arcade
from calculation import score, scoreWithButton

class render:

    def __init__(self):
        self.bg = arcade.Sprite('images/bg.psd')
        self.bg.set_position(500, 250)
        self.prs = arcade.Sprite('images/prs.png')
        self.prs.set_position(500, 250)

        self.left = arcade.Sprite('images/cha0.png')
        self.left.set_position(100,100)

        self.right = arcade.Sprite('images/pa0.png')
        self.right.set_position(900, 100)

    def print(self):
        print(score.score_left)

    def screen_draw(self):
        self.bg.draw()
        self.prs.draw()
        self.left.draw()
        self.right.draw()

class typeText(scoreWithButton):

    def type_score(self):
        arcade.draw_text(str(self.score_left), 95, 50, arcade.color.GRAY, 20)