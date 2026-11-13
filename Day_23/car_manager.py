from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.create_cars()

    def random_color(self):
        color = random.choice(COLORS)
        return color

    def spread_random_location(self, car):
        random_x_cor = random.randint(-300, 300)
        random_y_cor = random.randint(-300, 300)
        car.goto(random_x_cor, random_y_cor)

    def create_cars(self):
        for _ in range(10):
            car = Turtle()
            car.shape("square")
            car.color(self.random_color())
            car.shapesize(stretch_len=2)
            car.penup()
            self.spread_random_location(car)
            self.all_cars.append(car)

    def move_cars(self):
        self.setheading(180)
        self.forward(10)


# screen = Screen()
# screen.setup(width=600, height=600)

# car = CarManager()

# screen.exitonclick()
