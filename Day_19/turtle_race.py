from turtle import Turtle, Screen
import random

screen = Screen()
# Set the size
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
coordinates = [0, 30, 60, -30, -60, -90]
all_turtles = []
is_race_on = False

# Add a pop up
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.speed = "fastest"
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=coordinates[turtle_index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True


winner = []
while is_race_on:
    for turtle in all_turtles:
        turtle_distance = random.randint(0, 50)
        turtle.forward(turtle_distance)
        if turtle.xcor() >= 230:
            is_race_on = False
            winner.append(turtle.pencolor())

if winner[0] == user_bet:
    print("You win!")
else:
    print("You lose!")

screen.exitonclick()
