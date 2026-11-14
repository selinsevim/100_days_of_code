import time
from turtle import Screen
from player import *
from car_manager import *
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager_system = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_turtle, "Up")

game_is_on = True
move_distance = STARTING_MOVE_DISTANCE
while game_is_on:
    time.sleep(0.1)
    screen.update()
    all_cars = car_manager_system.all_cars
    # Reduce the chance of creating cars
    random_number = random.randint(1, 6)
    if random_number == 6:
        car_manager_system.create_cars()
    car_manager_system.move_cars(move_distance)
    # the logic where turtle passes the level comes here
    if player.ycor() >= 280:
        player.goto(STARTING_POSITION)
        move_distance += 10
        car_manager_system.move_cars(move_distance)
        scoreboard.increase_score()
        scoreboard.write_score()
    # Check collision detection
    for car in all_cars:
        if player.distance(car) <= 40:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
