from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, 250)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.score_right = 0
        self.score_left = 0
        self.write(
            f"{self.score_right}",
            move=False,
            font=("monaco", 30, "bold"),
            align="right",
        )
        self.write(
            f"{self.score_left}",
            move=False,
            font=("monaco", 30, "bold"),
            align="left",
        )

    def increase_score_right(self):
        self.score_right = self.score_right + 1
        return self.score_right

    def increase_score_left(self):
        self.score_left = self.score_left + 1
        return self.score_left

    def write_score(self):
        self.clear()
        self.write(
            f"{self.score_right}",
            move=False,
            font=("monaco", 30, "bold"),
            align="right",
        )
        self.write(
            f"{self.score_left}",
            move=False,
            font=("monaco", 30, "bold"),
            align="left",
        )
