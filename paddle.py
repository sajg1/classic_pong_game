from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, screen_width):
        super().__init__()
        self.current_positon = position
        self.width = screen_width
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)
        self.left(90)

    def up(self):
        if self.ycor() < (self.width/2)-50:
            self.forward(20)

    def down(self):
        if self.ycor() > -(self.width/2) + 70:
            self.backward(20)
