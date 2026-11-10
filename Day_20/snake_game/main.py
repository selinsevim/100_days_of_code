from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food

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

snake = Snake(coordinates=coordinates, color="white", num_of_segments=3)
food = Food()

screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.move_location_randomly()

screen.exitonclick()
