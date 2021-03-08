from turtle import Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

right_paddle = Paddle(position=(-350,0), screen_width=600)
left_paddle = Paddle(position=(350,0), screen_width=600)
screen.listen()

screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()