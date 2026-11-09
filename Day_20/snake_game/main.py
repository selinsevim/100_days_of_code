from turtle import Turtle, Screen

screen = Screen()
# Setup the screensize
screen.setup(width=600, height=600)
# Change the background color
screen.bgcolor("black")
# Create a title
screen.title("My Snake Game")

coordinates = [0, 20, 40]
all_turtles = []

for turtle_index in range(0, 3):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.setx(coordinates[turtle_index])
    all_turtles.append(turtle)


screen.exitonclick()
