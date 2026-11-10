from turtle import Turtle
import random

# note : self.food = Turtle() --> I dont need to create another turtle object
# because by inheriting self becomes == Turtle object


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5)
        self.move_location_randomly()

    def move_location_randomly(self):
        self.penup()
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def food_position(self):
        return self.pos()
