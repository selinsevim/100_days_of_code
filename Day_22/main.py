from turtle import Turtle, Screen

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pongo Game")

# Turn off the tracer
screen.tracer(0)

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

screen.exitonclick()
