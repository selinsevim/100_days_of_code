from turtle import Turtle, Screen

# Create Turtle object
turtle = Turtle()
# Change the shape
turtle.shape("turtle")
# Change the color of the turtle
turtle.color("CornflowerBlue")

# Draw a square
# for move in range(4):
#     # Move the turtle
#     turtle.forward(100)
#     # Turn right
#     turtle.right(90)

# Draw a dashed line
for _ in range(20):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()


# Create the scree so that it only exits when clicked
screen = Screen()
screen.exitonclick()
