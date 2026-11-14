import time
from turtle import Screen
from player import Player
from car_manager import *
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager_system = CarManager()

screen.listen()
screen.onkey(player.move_turtle, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_number = random.randint(1, 6)
    if random_number == 6:
        car_manager_system.create_cars()
    car_manager_system.move_cars(STARTING_MOVE_DISTANCE)
    player.reset_turtle()

screen.exitonclick()
