from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1 = 0
        self.player_2 = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_score()



    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.player_1}", align="center", font=('Arial', 50))
        self.goto(100, 200)
        self.write(f"{self.player_2}", align="center", font=('Arial', 50))

    def player_1_point(self):
        self.player_1 += 1
        self.update_score()

    def player_2_point(self):
        self.player_2 += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.update_score()
        self.goto(0, 0)
        if self.player_1 > self.player_2:
            winner = "1"
        else:
            winner = "2"
        self.write(f"Game Over", align="center", font=("Arial", 26))
        self.goto(0, -100)
        self.write(f"Player {winner} won the game.", align="center", font=("Arial", 26))