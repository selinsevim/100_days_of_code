from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def move(self):
        self.forward(20)

    def move_up(self):
        new_cor_y = self.ycor() + 20
        self.goto(self.xcor(), new_cor_y)

    def move_down(self):
        new_cor_y = self.ycor() - 20
        self.goto(self.xcor(), new_cor_y)
