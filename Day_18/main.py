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
# for _ in range(20):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# Draw a triangle, square, pentagon, hectagon..
number_of_corners = 3
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
while number_of_corners <= 10:
    for i in range(number_of_corners):
        turtle.pencolor(colors[number_of_corners % 6])
        corner_degree = 360 / number_of_corners
        turtle.right(corner_degree)
        turtle.forward(100)
    number_of_corners += 1


# Create the scree so that it only exits when clicked
screen = Screen()
screen.exitonclick()
