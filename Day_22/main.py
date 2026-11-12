from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pongo Game")

# Turn off the tracer
screen.tracer(0)

# Create right paddle
paddle_right = Paddle((350, 0))

# Create left paddle
paddle_left = Paddle((-350, 0))

# Create the ball
ball = Ball()

# Create scoreboard
scoreboard = Scoreboard()

# Add the event listeners
screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")


screen.onkey(paddle_left.move_up, "W")
screen.onkey(paddle_left.move_down, "S")


# Draw a dashed line in the middle
line = Turtle()
line.color("white")
line.shapesize(1)
line.teleport(0, 300)
line.setheading(270)

for _ in range(100):
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()
    if ball.ycor() <= -280 or ball.ycor() >= 280:
        ball.detect_collision()
    if (
        ball.distance(paddle_right.pos()) <= 50
        and ball.xcor() >= 330
        or ball.distance(paddle_left.pos()) <= 50
        and ball.xcor() <= -330
    ):
        ball.bouncing_on_paddle()
    # Ball is missed on left side
    if ball.xcor() <= -400:
        # is_game_on = False
        scoreboard.increase_score_left()
        scoreboard.write_score()
        ball.reset_ball_position()
        ball.move_ball_opposing()
        screen.update()

    # Ball is missed on right side
    if ball.xcor() >= 400:
        # is_game_on = False
        scoreboard.increase_score_right()
        scoreboard.write_score()
        ball.reset_ball_position()
        ball.move_ball_opposing()
        screen.update()


screen.exitonclick()
