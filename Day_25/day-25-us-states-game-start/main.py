from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.bgpic()
screen.bgpic(
    "/Users/selinsevim/Documents/100_days_of_code/Day_25/day-25-us-states-game-start/blank_states_img.gif"
)
screen.bgpic()

drawing = Turtle()


def get_cor_with_click(x, y):
    print(x, y)


screen.onscreenclick(get_cor_with_click)


# Read csv file
states = pd.read_csv(
    "/Users/selinsevim/Documents/100_days_of_code/Day_25/day-25-us-states-game-start/50_states.csv"
)

correct_guesses = []
all_states = states["state"].to_list()

score = 0
while len(correct_guesses) < len(all_states):
    user_answer = screen.textinput(
        f"Guessing Game: {score}/50", "Guess the state:"
    ).title()

    if user_answer == "Done":
        not_guessed_states = [
            state for state in all_states if state not in correct_guesses
        ]
        # list to dataframe
        df = pd.DataFrame(data={"not guessed states": not_guessed_states})
        df.to_csv(
            "/Users/selinsevim/Documents/100_days_of_code/Day_25/day-25-us-states-game-start/not_guessed_states.csv",
            sep=",",
            index=False,
        )
        break
    if len(states[states["state"] == user_answer]) > 0:
        x = states[states["state"] == user_answer].x.values[0]
        y = states[states["state"] == user_answer].y.values[0]
        drawing.hideturtle()
        drawing.penup()
        drawing.setposition(x, y)
        drawing.write(user_answer)
        correct_guesses.append(user_answer)
        score += 1
