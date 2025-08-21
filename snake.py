from turtle import Turtle
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        position = 0
        for i in range(3):
            new_square = Turtle()
            new_square.color("green")
            new_square.shape('square')
            new_square.penup()
            new_square.goto(position, 0)
            position -= 20
            self.segments.append(new_square)

    def extend(self):
        new_square = Turtle()
        new_square.hideturtle()
        new_square.color("green")
        new_square.shape('square')
        new_square.penup()
        new_square.goto(self.segments[-1].position())
        new_square.showturtle()
        self.segments.append(new_square)


    def move(self):
        for num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[num - 1].xcor()
            new_y = self.segments[num - 1].ycor()
            self.segments[num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.setheading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.setheading != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.setheading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.setheading != LEFT:
            self.head.setheading(RIGHT)





