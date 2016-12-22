import arcade
import arcade.sound
# from calculate import cal
from calculation import scoreWithButton, score
from drawing import render, typeText

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.button = scoreWithButton()
        self.score = score()
        self.render = render()
        self.type = typeText()
        #self.cal = cal()

    def on_draw(self):
        arcade.start_render()
        self.render.screen_draw()
        self.type.type_score()
        # self.cal.chai()
        # self.cal.pa()
        # self.cal.show_result()
        # arcade.draw_text(str(self.cal.score_chai), 95, 50, arcade.color.GRAY, 20)
        # arcade.draw_text(str(self.cal.score_pa), 900, 50, arcade.color.GRAY, 20)

        # self.render.print()

    def on_key_press(self, key, key_modifiers):
        # self.cal.update_result()
        # self.cal.on_key_press(key, key_modifiers)
        self.button.on_key_press(key, key_modifiers)
        # self.score.print_score()

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()