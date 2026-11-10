from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(0, 250)
        self.color("white")
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
            f"Score: {self.score}",
            move=False,
            font=("monaco", 10, "bold"),
            align="center",
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"Game Over",
            move=False,
            font=("monaco", 20, "bold"),
            align="center",
        )
