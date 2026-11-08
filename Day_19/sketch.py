from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


# Move forward
def move_forward():
    turtle.fd(20)


# Move bbackwards
def move_backwards():
    turtle.bk(20)


# Move counter-clockwise
def move_counter_clockwise():
    turtle.left(20)


# Move counter-clockwise
def move_clockwise():
    turtle.right(20)


def clear_drawing():
    screen.clearscreen()


screen.listen()
screen.onkeypress(move_forward, "W")
screen.onkeypress(move_backwards, "S")
screen.onkeypress(move_counter_clockwise, "A")
screen.onkeypress(move_clockwise, "D")
screen.onkeypress(clear_drawing, "C")
screen.exitonclick()
