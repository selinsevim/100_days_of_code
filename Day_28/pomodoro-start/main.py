import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

main_label = tk.Label(text="Timer", font=("Courier", 24), fg=GREEN, bg=YELLOW)
main_label.grid(row=0, column=1)

tick_label = tk.Label(text="✓", font=("Courier", 24), fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)

start_button = tk.Button(text="Start", highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)

# Canvas widget
canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(row=1, column=1)

python_image = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_28/pomodoro-start/tomato.png"
)
canvas.create_image((100, 112), image=python_image)
canvas.create_text((100, 130), text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

window.mainloop()
