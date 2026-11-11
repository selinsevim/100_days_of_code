from turtle import Turtle, Screen
from paddle import Paddle
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


screen.exitonclick()
