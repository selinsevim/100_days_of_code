import colorgram
from turtle import Turtle, Screen
import random

# Extract 6 colors from an image.
# colors = colorgram.extract(
#     r"/Users/selinsevim/Documents/100_days_of_code/Day_18/hirsh-painting/image.jpg", 10
# )

# color_list = []
# for color in colors:
#     rgb = color.rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     rgb_tuple = (r, g, b)
#     color_list.append(rgb_tuple)

screen = Screen()
screen.colormode(255)


# print(color_list)
color_list = [
    (249, 249, 248),
    (241, 249, 245),
    (250, 244, 247),
    (238, 245, 249),
    (227, 145, 89),
    (199, 80, 114),
    (140, 82, 106),
    (215, 129, 159),
    (59, 99, 159),
    (145, 87, 69),
]

# Create a turtle object
turtle = Turtle()


def pick_random_color(color_list):
    color = random.choice(color_list)
    return color


def draw_hirsh(number_of_dots, gap_between):
    total_turnover = number_of_dots * gap_between
    for _ in range(number_of_dots):
        for _ in range(number_of_dots):
            turtle.penup()
            turtle.dot(20, pick_random_color(color_list))
            turtle.fd(gap_between)
            turtle.pendown()
        turtle.penup()
        turtle.setheading(90)
        turtle.fd(gap_between)
        turtle.setheading(-180)
        turtle.fd(total_turnover)
        turtle.setheading(0)
        turtle.pendown()


draw_hirsh(10, 50)

screen.exitonclick()
