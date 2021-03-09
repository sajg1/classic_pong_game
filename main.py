from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle(position=(-350,0), screen_width=600)
left_paddle = Paddle(position=(350,0), screen_width=600)
ball = Ball()
screen.listen()

screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")
screen.onkey(left_paddle.up, "Up")

screen.onkey(left_paddle.down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()
    # time.sleep(0.1)
    ball.move()
    # when the ball reaches either of these y-coordinates, wall_bounce() changes the sign in front of self.move_y
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    # Because of the stretched nature of the paddle, using ball.distance(paddle) alone will not work.
    # This is because the distance is measured from the center of each object.
    # the ends of the paddles will be further away
    # Therefore I had to check for a max xcor() being reached first. Followed by a larger distance of 50px
    if ball.xcor() > 330 or ball.xcor() < -330:
        if ball.distance(left_paddle) < 50 or ball.distance(right_paddle) < 50:
            ball.paddle_bounce()

screen.exitonclick()

