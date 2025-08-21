from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"SCORE = {self.score}",False, "center", ('Arial', 24, 'normal'))

    def score_up(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE = {self.score}", False, "center", ('Arial', 24, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", False, "center", ('Arial', 40, 'normal'))


