import arcade
class cal:
    ans_chai = 0
    ans_pa = 0
    score_chai = 0
    score_pa = 0
    people_chai = arcade.Sprite('images/cha2.png')
    people_pa = arcade.Sprite('images/pa2.png')
    game_finish = False

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
        if self.game_finish == False:
            #scissor = 1, rock = 2, paper = 3
            if self.ans_chai == 1 and self.ans_pa == 2:
                self.score_pa += 1
            elif self.ans_chai == 1 and self.ans_pa == 3:
                self.score_chai += 1
            elif self.ans_chai == 2 and self.ans_pa == 1:
                self.score_chai += 1
            elif self.ans_chai == 2 and self.ans_pa == 3:
                self.score_pa += 1
            elif self.ans_chai == 3 and self.ans_pa == 1:
                self.score_pa += 1
            elif self.ans_chai == 3 and self.ans_pa == 2:
                self.score_chai += 1
            if self.ans_chai != 0 and self.ans_pa != 0:
                self.ans_chai = 0
                self.ans_pa = 0
        if self.score_chai == 5 or self.score_pa == 5:
            self.game_finish = True

    def chai(self):
        if self.score_chai - self.score_pa == -3:
            self.people_chai = arcade.Sprite('images/cha-3.png')
        elif self.score_chai - self.score_pa == -2:
            self.people_chai = arcade.Sprite('images/cha-2.png')
        elif self.score_chai - self.score_pa == -1:
            self.people_chai = arcade.Sprite('images/cha-1.png')
        elif self.score_chai - self.score_pa == 0:
            self.people_chai = arcade.Sprite('images/cha0.png')
        elif self.score_chai - self.score_pa == 1:
            self.people_chai = arcade.Sprite('images/cha1.png')
        elif self.score_chai - self.score_pa == 2:
            self.people_chai = arcade.Sprite('images/cha2.png')
        elif self.score_chai - self.score_pa == 3:
            self.people_chai = arcade.Sprite('images/cha3.png')
        elif self.score_chai - self.score_pa == 4:
            self.people_chai = arcade.Sprite('images/cha4.png')
        self.people_chai.set_position(300, 150)
        self.people_chai.draw()

    def pa(self):
        if self.score_pa - self.score_chai == -3:
            self.people_pa = arcade.Sprite('images/pa-3.png')
        elif self.score_pa - self.score_chai == -2:
            self.people_pa = arcade.Sprite('images/pa-2.png')
        elif self.score_pa - self.score_chai == -1:
            self.people_pa = arcade.Sprite('images/pa-1.png')
        elif self.score_pa - self.score_chai == 0:
            self.people_pa = arcade.Sprite('images/pa0.png')
        elif self.score_pa - self.score_chai == 1:
            self.people_pa = arcade.Sprite('images/pa1.png')
        elif self.score_pa - self.score_chai == 2:
            self.people_pa = arcade.Sprite('images/pa2.png')
        elif self.score_pa - self.score_chai == 3:
            self.people_pa = arcade.Sprite('images/pa3.png')
        elif self.score_pa - self.score_chai == 4:
            self.people_pa = arcade.Sprite('images/pa4.png')
        self.people_pa.set_position(700, 150)
        self.people_pa.draw()

    def show_result(self):
        if self.game_finish == True and self.score_chai == 5:
            self.result_chai = arcade.Sprite('images/win.png')
            self.result_chai.set_position(300, 400)
            self.result_chai.draw()
            self.result_pa = arcade.Sprite('images/lose.png')
            self.result_pa.set_position(700, 400)
            self.result_pa.draw()
        elif self.game_finish == True:
            self.result_chai = arcade.Sprite('images/lose.png')
            self.result_chai.set_position(300, 400)
            self.result_chai.draw()
            self.result_pa = arcade.Sprite('images/win.png')
            self.result_pa.set_position(700, 400)
            self.result_pa.draw()