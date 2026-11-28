BACKGROUND_COLOR = "#B1DDC6"

import tkinter as tk
import pandas as pd
import random
from tkinter.messagebox import _show

timer = None


# Read the data in csv format
french_data = pd.read_csv(
    "/Users/selinsevim/Documents/100_days_of_code/Day_31/flash-card-project-start/data/french_words.csv"
)


def next_card():
    canvas.itemconfigure(canvas_image, image=image_front)
    french, english = random_word_selection()
    canvas.itemconfigure(card_word, text=french)
    canvas.itemconfigure(card_title, text="French")
    window.after(1000, lambda: flip_card(english))


def flip_card(english):
    canvas.itemconfigure(card_word, text=english)
    canvas.itemconfigure(card_title, text="English")
    canvas.itemconfigure(canvas_image, image=image_back)


def random_word_selection():
    # Convert the dataframe into dictionary
    data_dict = {row.French: row.English for (index, row) in french_data.iterrows()}
    # Randomly pick key:value pair - first convert to list
    french, english = random.choice(list(data_dict.items()))
    return french, english


window = tk.Tk()
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)


# Create Canvas
canvas = tk.Canvas(
    window, width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR
)
image_front = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_31/flash-card-project-start/images/card_front.png"
)

image_back = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_31/flash-card-project-start/images/card_back.png"
)

canvas.grid(row=0, column=0, columnspan=2)
canvas_image = canvas.create_image((400, 263), image=image_front)
card_title = canvas.create_text(
    (400, 200),
    text="",
    font=("Ariel", 40, "italic"),
    fill="black",
)
card_word = canvas.create_text(
    (400, 300),
    text="",
    font=("Ariel", 60, "bold"),
    fill="black",
)

# Buttons
right_image = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_31/flash-card-project-start/images/right.png"
)
right_button = tk.Button(
    window, image=right_image, highlightthickness=0, bd=0, command=next_card
)
right_button.grid(row=1, column=0)

wrong_image = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_31/flash-card-project-start/images/wrong.png"
)
wrong_button = tk.Button(
    window, image=wrong_image, highlightthickness=0, bd=0, command=next_card
)
wrong_button.grid(row=1, column=1)

window.mainloop()
