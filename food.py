from turtle import Turtle
import random
colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta", "brown", "grey"]



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("purple")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        self.color(random.choice(colors))
        random_x = random.randint(-280, 265)
        random_y = random.randint(-280, 265)
        self.goto(random_x, random_y)
