from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def random_color(self):
        color = random.choice(COLORS)
        return color

    def reset_car_position(self, single_car):
        random_y_cor = random.randint(-250, 250)
        single_car.goto(300, random_y_cor)

    def create_cars(self):
        car = Turtle()
        car.shape("square")
        car.color(self.random_color())
        car.shapesize(stretch_len=2)
        car.penup()
        self.reset_car_position(car)
        self.all_cars.append(car)

    def move_cars(self, move_distance):
        for single_car in self.all_cars:
            single_car.penup()
            single_car.setheading(180)
            single_car.forward(move_distance)
