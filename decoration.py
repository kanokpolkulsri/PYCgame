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
        self.cover = arcade.Sprite('images/cover.png')
        self.cover.set_position(500,250)
        self.podium = arcade.Sprite('images/podium.png')
        self.podium.set_position(500, 250)
        self.cha_podium = arcade.Sprite('images/chaForPodium.png')
        self.cha_podium.set_position(270, 40)
        self.pa_podium = arcade.Sprite('images/paForPodium.png')
        self.pa_podium.set_position(730, 40)
        self.score_left_0 = arcade.Sprite('images/score0.png')
        self.score_left_0.set_position(200,300)
        self.score_right_0 = arcade.Sprite('images/score0.png')
        self.score_right_0.set_position(800, 300)

    def screen_draw(self):
        self.bg.draw()
        self.prs.draw()
        self.left.draw()
        self.right.draw()
        self.change_position_podium()

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

    def draw_cover(self):
        if self.screen.score.canplay == False:
            self.cover.draw()
            self.podium.draw()
            self.cha_podium.draw()
            self.pa_podium.draw()
            self.score_left_0.draw()

    def change_position_podium(self):
        if self.screen.score.score_left == 0:
            self.cha_podium.set_position(270, 40)
        elif self.screen.score.score_left == 1:
            self.cha_podium.set_position(340, 90)
        elif self.screen.score.score_left == 2:
            self.cha_podium.set_position(415, 130)
        elif self.screen.score.score_left == 3:
            self.cha_podium.set_position(500, 180)

        if self.screen.score.score_right == 0:
            self.pa_podium.set_position(730, 40)
        elif self.screen.score.score_right == 1:
            self.pa_podium.set_position(650, 90)
        elif self.screen.score.score_right == 2:
            self.pa_podium.set_position(575, 130)
        elif self.screen.score.score_right == 3:
            self.pa_podium.set_position(500, 175)
