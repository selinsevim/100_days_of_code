import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    main_label.config(text="Timer", font=("Courier", 24), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_sec)
        main_label.config(text="Break", font=("Courier", 24), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        countdown(short_sec)
        main_label.config(text="Break", font=("Courier", 24), fg=PINK, bg=YELLOW)
    else:
        countdown(work_sec)
        main_label.config(text="Work", font=("Courier", 24), fg=GREEN, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global timer
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if 0 <= count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

main_label = tk.Label(text="Timer", font=("Courier", 24), fg=GREEN, bg=YELLOW)
main_label.grid(row=0, column=1)


tick_label = tk.Label(text="✓", font=("Courier", 24), fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)

start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# Canvas widget
canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
python_image = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_28/pomodoro-start/tomato.png"
)
canvas.create_image((100, 112), image=python_image)
timer_text = canvas.create_text(
    (100, 130), text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=1, column=1)


window.mainloop()
