from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    #  general movement of ball
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.move_y *= -1

    def paddle_bounce(self):
        self.move_x *= -1
        # increases the speed of the ball movement incrementally when in contact with paddle
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1


