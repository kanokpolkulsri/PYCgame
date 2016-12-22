import arcade
class render:

    def __init__(self, screen):
        self.screen = screen

        self.bg = arcade.Sprite('images/bg.psd')
        self.bg.set_position(500, 250)
        self.prs = arcade.Sprite('images/prs.png')
        self.prs.set_position(500, 250)

        self.left = arcade.Sprite('images/cha0.png')
        self.left.set_position(100,100)

        self.right = arcade.Sprite('images/pa0.png')
        self.right.set_position(900, 100)

    def screen_draw(self):
        self.bg.draw()
        self.prs.draw()
        self.left.draw()
        self.right.draw()

    def draw_score(self):
        if self.screen.score.canplay == True:
            arcade.draw_text(str(self.screen.score.button_1), 360, 320, arcade.color.GRAY, 20)
            arcade.draw_text(str(self.screen.score.button_2), 480, 320, arcade.color.GRAY, 20)
            arcade.draw_text(str(self.screen.score.button_3), 600, 320, arcade.color.GRAY, 20)

            arcade.draw_text(str(self.screen.score.player_left_1), 250, 50, arcade.color.GRAY, 20)
            arcade.draw_text(str(self.screen.score.player_left_2), 300, 50, arcade.color.GRAY, 20)
            arcade.draw_text(str(self.screen.score.player_left_3), 350, 50, arcade.color.GRAY, 20)

            arcade.draw_text(str(self.screen.score.player_right_1), 650, 50, arcade.color.GRAY, 20)
            arcade.draw_text(str(self.screen.score.player_right_2), 700, 50, arcade.color.GRAY, 20)
            arcade.draw_text(str(self.screen.score.player_right_3), 750, 50, arcade.color.GRAY, 20)


