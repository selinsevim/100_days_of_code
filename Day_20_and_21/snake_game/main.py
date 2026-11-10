from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
# Setup the screensize
screen.setup(width=600, height=600)
# Change the background color
screen.bgcolor("black")
# Create a title
screen.title("My Snake Game")
# Turn off the tracer
screen.tracer(0)


snake = Snake(color="white", num_of_segments=3)
food = Food()

# Create event listeners
screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")


is_game_on = True
score = Scoreboard()

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.move_location_randomly()
        snake.extend_snake()
        score.increase_score()
        score.write_score()

    if snake.head.xcor() > 280:
        is_game_on = False
        score.game_over()

    elif snake.head.xcor() < -280:
        is_game_on = False
        score.game_over()

    elif snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()

    elif snake.head.ycor() > 280:
        is_game_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()
