import arcade
class button:

    button_1 = 3
    button_2 = 2
    button_3 = 1

    player_left_1 = 0
    player_left_2 = 0
    player_left_3 = 0

    player_right_1 = 0
    player_right_2 = 0
    player_right_3 = 0

    def on_key_press(self, key, key_modifiers):

        if self.player_left_1 != self.button_1 or self.player_left_2 != self.button_2 or self.player_left_3 != self.button_3:
            if key == arcade.key.A:
                self.player_left_1 += 1
                if self.player_left_1 > self.button_1:
                    self.player_left_1 = 0
                print(self.player_left_1, self.player_left_2, self.player_left_3)
            elif key == arcade.key.S:
                if self.player_left_2 > self.button_2:
                    self.player_left_2 = 0
                self.player_left_2 += 1
                print(self.player_left_1, self.player_left_2, self.player_left_3)
            elif key == arcade.key.D:
                if self.player_left_3 > self.button_3:
                    self.player_left_3 = 0
                self.player_left_3 += 1
                print(self.player_left_1, self.player_left_2, self.player_left_3)
            if self.player_left_1 == self.button_1 and self.player_left_2 == self.button_2 and self.player_left_3 == self.button_3:
                print('spacebar')
                self.player_left_1 = 0
                self.player_left_2 = 0
                self.player_left_3 = 0
                self.player_right_1 = 0
                self.player_right_2 = 0
                self.player_right_3 = 0
                # self.button_1 = 1
                # self.button_2 = 2
                # self.button_3 = 3

        if self.player_right_1 != self.button_1 or self.player_right_2 != self.button_2 or self.player_right_3 != self.button_3:
            if key == arcade.key.J:
                self.player_right_1 += 1
                if self.player_right_1 > self.button_1:
                    self.player_right_1 = 0
                print(self.player_right_1, self.player_right_2, self.player_right_3)
            elif key == arcade.key.K:
                self.player_right_2 += 1
                if self.player_right_2 > self.button_2:
                    self.player_right_2 = 0
                print(self.player_right_1, self.player_right_2, self.player_right_3)
            elif key == arcade.key.L:
                self.player_right_3 += 1
                if self.player_right_3 > self.button_3:
                    self.player_right_3 = 0
                print(self.player_right_1, self.player_right_2, self.player_right_3)
            if self.player_right_1 == self.button_1 and self.player_right_2 == self.button_2 and self.player_right_3 == self.button_3:
                print('spacebar')
                self.player_left_1 = 0
                self.player_left_2 = 0
                self.player_left_3 = 0
                self.player_right_1 = 0
                self.player_right_2 = 0
                self.player_right_3 = 0
                # self.button_1 = 1
                # self.button_2 = 2
                # self.button_3 = 3

class score(button):
    def print(self):
        print(self.button_1)
