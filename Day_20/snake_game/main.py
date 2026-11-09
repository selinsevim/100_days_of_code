from turtle import Turtle, Screen
import time

screen = Screen()
# Setup the screensize
screen.setup(width=600, height=600)
# Change the background color
screen.bgcolor("black")
# Create a title
screen.title("My Snake Game")
# Turn off the tracer
screen.tracer(0)

coordinates = [(0, 0), (20, 0), (40, 0)]
all_segments = []

for turtle_index in range(0, 3):
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(coordinates[turtle_index])
    all_segments.append(segment)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(all_segments) - 1, 0, -1):
        # last segment will go to the position of the former segment
        former_x_pos = all_segments[seg_num - 1].xcor()
        former_y_pos = all_segments[seg_num - 1].ycor()
        all_segments[seg_num].goto(former_x_pos, former_y_pos)

    all_segments[0].forward(20)
    all_segments[0].right(90)


screen.exitonclick()
