import arcade
class button:

    button_1 = 3
    button_2 = 2
    button_3 = 1

    player_left_1 = 0
    player_left_2 = 0
    player_left_3 = 0

    def on_key_press(self, key, key_modifiers):

        if self.player_left_1 != self.button_1 or self.player_left_2 != self.button_2 or self.player_left_3 != self.button_3:
            if key == arcade.key.A:
                self.player_left_1 += 1
                print(self.player_left_1, self.player_left_2, self.player_left_3)
            elif key == arcade.key.S:
                self.player_left_2 += 1
                print(self.player_left_1, self.player_left_2, self.player_left_3)
            elif key == arcade.key.D:
                self.player_left_3 += 1
                print(self.player_left_1, self.player_left_2, self.player_left_3)
            if self.player_left_1 == self.button_1 and self.player_left_2 == self.button_2 and self.player_left_3 == self.button_3:
                print('spacebar')

        if key == arcade.key.J:
            print('1')
        elif key == arcade.key.K:
            print('2')
        elif key == arcade.key.L:
            print('3')

