import arcade
import arcade.key

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500


class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)
        self.man = arcade.Sprite('images/cha2.png')
        self.man.set_position(100,100)

    def on_draw(self):
        arcade.start_render()
        self.man.draw()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.A:
            self.man = arcade.Sprite('images/cha1.png')
            self.man.set_position(100, 100)
        elif key == arcade.key.S:
            self.man = arcade.Sprite('images/cha3.png')
            self.man.set_position(100, 100)
        elif key == arcade.key.D:
            a = 'images/cha4.png'
            self.man = arcade.Sprite(a)
            self.man.set_position(100, 100)

if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()