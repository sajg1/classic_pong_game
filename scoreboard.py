from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1 = 0
        self.player_2 = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)

    def show_score(self):
        self.clear()
        self.write(f"{self.player_1} : {self.player_2}", align="center", font=("Arial", 40))