import arcade
class cal:
    ans_chai = 0
    ans_pa = 0
    score_chai = 1
    score_pa = 1

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
        print(self.score_chai, self.score_pa)

    def update_result(self):
        if self.ans_chai == 1 and self.ans_pa == 1:
            self.ans_chai = 0
            self.ans_pa = 0
            print('draw')
        elif self.ans_chai == 2 and self.ans_pa == 2:
            self.ans_chai = 0
            self.ans_pa = 0
            print('draw')
        elif self.ans_chai == 3 and self.ans_pa == 3:
            self.ans_chai = 0
            self.ans_pa = 0
            print('draw')
        #scissor = 1, rock = 2, paper = 3
        elif self.ans_chai == 1 and self.ans_pa == 2:
            self.ans_chai = 0
            self.ans_pa = 0
            self.score_pa += 1
        elif self.ans_chai == 1 and self.ans_pa == 3:
            self.ans_chai = 0
            self.ans_pa = 0
            self.score_chai += 1
        elif self.ans_chai == 2 and self.ans_pa == 1:
            self.ans_chai = 0
            self.ans_pa = 0
            self.score_chai += 1
        elif self.ans_chai == 2 and self.ans_pa == 3:
            self.ans_chai = 0
            self.ans_pa = 0
            self.score_pa += 1
        elif self.ans_chai == 3 and self.ans_pa == 1:
            self.ans_chai = 0
            self.ans_pa = 0
            self.score_pa += 1
        elif self.ans_chai == 3 and self.ans_pa == 2:
            self.ans_chai = 0
            self.ans_pa = 0
            self.score_chai += 1