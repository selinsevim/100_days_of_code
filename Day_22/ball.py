from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0, 0)
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        self.penup()
        new_cor_y = self.ycor() + self.y_move
        new_cor_x = self.xcor() + self.x_move
        self.goto(new_cor_x, new_cor_y)

    def move_ball_opposing(self):
        # self.y_move *= -1
        self.x_move *= -1

    def detect_collision(self):
        self.y_move *= -1

    def bouncing_on_paddle(self):
        self.y_move *= -1

    def reset_ball_position(self):
        self.goto(0, 0)
