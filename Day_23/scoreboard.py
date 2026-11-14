FONT = ("Courier", 24, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(-250, 250)
        self.color("black")
        self.speed("fastest")
        self.hideturtle()
        self.score = 0
        self.write_score()

    def increase_score(self):
        self.score = self.score + 1
        return self.score

    def write_score(self):
        self.clear()
        self.write(
            f"Level: {self.score}",
            move=False,
            font=FONT,
            align="left",
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"Game Over",
            move=False,
            font=FONT,
            align="center",
        )
