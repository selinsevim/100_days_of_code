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
# number_of_corners = 3
# colors = ["red", "purple", "blue", "green", "yellow", "orange"]
# while number_of_corners <= 10:
#     for i in range(number_of_corners):
#         turtle.pencolor(colors[number_of_corners % 6])
#         corner_degree = 360 / number_of_corners
#         turtle.right(corner_degree)
#         turtle.forward(100)
#     number_of_corners += 1

import random

# Create the scree so that it only exits when clicked
screen = Screen()

screen.colormode(255)

# angles = [-90, 90, 0, 180]
# colors = [
#     "#264653",  # Dark teal
#     "#2A9D8F",  # Teal
#     "#8AB17D",  # Sage green
#     "#E9C46A",  # Mustard yellow
#     "#F4A261",  # Soft orange
#     "#E76F51",  # Coral
#     "#D62828",  # Red
#     "#9B5DE5",  # Purple
#     "#577590",  # Steel blue
#     "#F15BB5",  # Pink
# ]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


turtle.speed("fastest")


def draw_spinograph(add_gap):
    for i in range(int(360 / add_gap)):
        turtle.pen(pencolor=random_color())
        turtle.circle(50)
        turtle.setheading(turtle.heading() + add_gap)


draw_spinograph(30)

# for i in range(1000):
#     turtle.pen(pencolor=random_color(), pensize=10)
#     # turtle.right(random.choice(angles))
#     turtle.setheading(random.choice(angles))
#     turtle.forward(20)


screen.exitonclick()
