from turtle import Screen
from paddle import Paddle
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

paddle1 = Paddle(starting_x=-350)
paddle2 = Paddle(starting_x=350)
screen.listen()

screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
screen.exitonclick()