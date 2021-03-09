from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle(position=(-350,0), screen_width=600)
left_paddle = Paddle(position=(350,0), screen_width=600)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")
screen.onkey(left_paddle.up, "Up")

screen.onkey(left_paddle.down, 'Down')

game_is_on = True
while game_is_on:
    scoreboard.show_score()
    point_scored = False
    ball.goto(0, 0)
    while not point_scored:
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

        if ball.xcor() > 400:
            print("player 1 point")
            point_scored = True
            scoreboard.player_1 +=1

        elif ball.xcor() < -400:
            print("player 2 point")
            point_scored = True
            scoreboard.player_2 += 1

screen.exitonclick()

