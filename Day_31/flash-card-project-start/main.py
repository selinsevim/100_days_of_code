BACKGROUND_COLOR = "#B1DDC6"

import tkinter as tk

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
canvas.create_text(
    (400, 300),
    text="English",
    font=("Ariel", 60, "bold"),
    fill="black",
)

# Buttons
right_image = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_31/flash-card-project-start/images/right.png"
)
right_button = tk.Button(window, image=right_image, highlightthickness=0, bd=0)
right_button.grid(row=1, column=0)

wrong_image = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_31/flash-card-project-start/images/wrong.png"
)
wrong_button = tk.Button(window, image=wrong_image, highlightthickness=0, bd=0)
wrong_button.grid(row=1, column=1)

window.mainloop()
