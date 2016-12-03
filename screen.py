import arcade
import arcade.key
from calculate import cal

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        # arcade.set_background_color('images/background.png')
        self.bg = arcade.Sprite('images/background.png')
        self.bg.set_position(500,250)
        self.cal = cal()

    def on_draw(self):
        arcade.start_render()
        self.bg.draw()
        self.cal.chai()
        self.cal.pa()
        arcade.draw_text(str(self.cal.score_chai), 95, 50, arcade.color.GRAY, 20)
        arcade.draw_text(str(self.cal.score_pa), 900, 50, arcade.color.GRAY, 20)

    def on_key_press(self, key, key_modifiers):
        self.cal.update_result()
        self.cal.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()