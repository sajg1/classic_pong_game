from turtle import Turtle

class Gameboard(Turtle):
    def __init__(self):
        super().__init__()


    def centerline(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.right(90)
        for i in range(10):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)