from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from gameboard import Gameboard
import time


screen = Screen()


def play_pong():

    right_paddle = Paddle(position=(350, 0), screen_width=600)
    left_paddle = Paddle(position=(-350, 0), screen_width=600)
    ball = Ball()
    scoreboard = Scoreboard()
    gameboard = Gameboard()

    screen.listen()

    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, 's')

    gameboard.centerline()
    game_is_on = True
    while game_is_on:

        gameboard.players()
        point_scored = False
        ball.reset_position()
        screen.update()
        # delays the movement of new ball
        time.sleep(0.5)
        while not point_scored:
            screen.update()
            ball.move()
            time.sleep(ball.move_speed)
            # when the ball reaches either of these y-coordinates,
            # wall_bounce() changes the sign in front of self.move_y
            if ball.ycor() > 280 or ball.ycor() < -280:
                ball.wall_bounce()

            # Because of the stretched nature of the paddle, using ball.distance(paddle) alone will not work.
            # This is because the distance is measured from the center of each object.
            # the ends of the paddles will be further away
            # Therefore I had to check for a max xcor() being reached first. Followed by a larger distance of 50px
            if 310 < ball.xcor() < 330 or -310 > ball.xcor() > -330:
                print(ball.xcor())
                if ball.distance(right_paddle) < 80 or ball.distance(left_paddle) < 80:
                    print("in contact")
                    ball.paddle_bounce()

            if ball.xcor() > 400:
                point_scored = True
                scoreboard.player_1_point()
                if scoreboard.player_1 == 5:
                    scoreboard.update_score()
                    game_is_on = False
                    gameboard.clear()
                    scoreboard.game_over()
            elif ball.xcor() < -400:
                point_scored = True
                scoreboard.player_2_point()
                if scoreboard.player_2 == 5:
                    scoreboard.update_score()
                    game_is_on = False
                    gameboard.clear()
                    scoreboard.game_over()


while screen.textinput(title="Play Pong", prompt="Play a game of PONG? 'y' or 'n': ") == 'y':
    screen.clear()
    screen.bgcolor("black")
    screen.title("Pong")
    screen.setup(width=800, height=600)
    screen.tracer(0)
    play_pong()

screen.exitonclick()

