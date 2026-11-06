from turtle import Turtle, Screen

# Create Turtle object
timmy_the_turtle = Turtle()
# Change the shape
timmy_the_turtle.shape("turtle")
# Change the color of the turtle
timmy_the_turtle.color("CornflowerBlue")
# Move the turtle
timmy_the_turtle.forward(100)
# Find the position of the turtle
print(timmy_the_turtle.position())
# Turn right
timmy_the_turtle.right(90)
# Move the turtle
timmy_the_turtle.forward(100)

# Create the scree so that it only exits when clicked
screen = Screen()
screen.exitonclick()
