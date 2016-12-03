import arcade
class cal:
    ans_chai = 0
    ans_pa = 0
    score_chai = 0
    score_pa = 0
    people_chai = arcade.Sprite('images/cha2.png')
    people_pa = arcade.Sprite('images/pa2.png')

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
        if key == arcade.key.SPACE:
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

    def chai(self):
        if self.score_chai - self.score_pa == 1:
            self.people_chai = arcade.Sprite('images/cha2.png')
        if self.score_chai - self.score_pa == 2:
            self.people_chai = arcade.Sprite('images/cha4.png')
        if self.score_chai - self.score_pa == 3:
            self.people_chai = arcade.Sprite('images/cha4.png')
        if self.score_chai - self.score_pa == 4:
            self.people_chai = arcade.Sprite('images/cha5.png')
        if self.score_chai - self.score_pa == 5:
            self.people_chai = arcade.Sprite('images/cha5.png')
        self.people_chai.set_position(100, 100)
        self.people_chai.draw()

    def pa(self):
        if self.score_pa - self.score_chai == 1:
            self.people_pa = arcade.Sprite('images/pa2.png')
        if self.score_pa - self.score_chai == 2:
            self.people_pa = arcade.Sprite('images/pa4.png')
        if self.score_pa - self.score_chai == 3:
            self.people_pa = arcade.Sprite('images/pa4.png')
        if self.score_pa - self.score_chai == 4:
            self.people_pa = arcade.Sprite('images/pa5.png')
        if self.score_pa - self.score_chai == 5:
            self.people_pa = arcade.Sprite('images/pa5.png')
        self.people_pa.set_position(900, 100)
        self.people_pa.draw()

