import arcade
from calculation import allAboutScore
from decoration import render

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.score = allAboutScore(self)
        self.render = render(self)

    def on_draw(self):
        arcade.start_render()
        self.render.screen_draw()
        self.render.draw_score()
        self.render.draw_cover()

    def on_key_press(self, key, key_modifiers):
        self.score.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()