from turtle import Turtle
import random
ALIGNMENT = "center"
FONT = ('Arial', 22, 'normal')
with open("data.txt") as file:
    SCORE = file.read()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.highscore = int(SCORE)
        self.score_update()
        self.color("white")
        self.hideturtle()
        self.pu()

    def score_update(self):
        self.goto(0, 270)
        self.clear()
        self.write(f"Score = {self.score} High score = {self.highscore}", True, align="center", font=('Arial', 22, 'normal'))

    def score_increase(self):

        self.score += 1

        self.goto(0,270)

        self.score_update()

    def reset(self):
        self.goto(0, 270)
        if self.score> self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.clear()
        self.score_update()







    # def score_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER ", True, align="center", font=('Arial', 29, 'normal'))


