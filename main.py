from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

s = Screen()
t = Turtle()
ball = Ball()
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)

s.listen()
s.onkey(r_paddle.go_up, "Up")
s.onkey(r_paddle.go_down, "Down")
s.onkey(l_paddle.go_up, "w")
s.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset()
        ball.bounce_x()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset()
        ball.bounce_x()
        scoreboard.r_point()


s.exitonclick()
