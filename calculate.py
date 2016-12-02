import arcade
class cal:
    ans_chai = 0
    ans_pa = 0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.A:
            self.ans_chai = 1
        elif key == arcade.key.S:
            self.ans_chai = 2
        elif key == arcade.key.D:
            self.ans_chai = 3
        if key == arcade.key.J:
            self.ans_pa = 1
        elif key == arcade.key.K:
            self.ans_pa = 2
        elif key == arcade.key.L:
            self.ans_pa = 3
        if self.ans_chai != 0 and self.ans_pa != 0:
            if key == arcade.key.SPACE:
                self.ans_chai = 0
                self.ans_pa = 0

