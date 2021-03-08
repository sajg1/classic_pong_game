from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_x):
        super().__init__()
        self.starting_x = starting_x
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x=-self.starting_x, y=0)
        self.left(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
