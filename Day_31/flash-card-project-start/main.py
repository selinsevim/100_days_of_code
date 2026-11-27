BACKGROUND_COLOR = "#B1DDC6"

import tkinter as tk
import pandas as pd
import random

# Read the data in csv format
french_data = pd.read_csv(
    "/Users/selinsevim/Documents/100_days_of_code/Day_31/flash-card-project-start/data/french_words.csv"
)


def random_word_selection():
    # Convert the dataframe into dictionary
    data_dict = {row.French: row.English for (index, row) in french_data.iterrows()}
    # Randomly pick key:value pair - first convert to list
    french, english = random.choice(list(data_dict.items()))
    canvas.itemconfigure(french_object, text=french)
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
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_image((400, 263), image=image_front)
canvas.create_text(
    (400, 200),
    text="French",
    font=("Ariel", 40, "italic"),
    fill="black",
)
french_object = canvas.create_text(
    (400, 300),
    text="item",
    font=("Ariel", 60, "bold"),
    fill="black",
)

# Buttons
right_image = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_31/flash-card-project-start/images/right.png"
)
right_button = tk.Button(
    window, image=right_image, highlightthickness=0, bd=0, command=random_word_selection
)
right_button.grid(row=1, column=0)

wrong_image = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_31/flash-card-project-start/images/wrong.png"
)
wrong_button = tk.Button(
    window, image=wrong_image, highlightthickness=0, bd=0, command=random_word_selection
)
wrong_button.grid(row=1, column=1)

window.mainloop()
