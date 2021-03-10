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

    def players(self):
        self.goto(-200, -275)
        self.write("Player 1", align='center', font=('Arial', 26))
        self.goto(200, -275)
        self.write("Player 2", align='center', font=('Arial', 26))