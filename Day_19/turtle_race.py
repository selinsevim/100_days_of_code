from turtle import Turtle, Screen

screen = Screen()
# Set the size
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
coordinates = [0, 30, 60, -30, -60, -90]

# Add a pop up
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=coordinates[turtle_index])

screen.exitonclick()
