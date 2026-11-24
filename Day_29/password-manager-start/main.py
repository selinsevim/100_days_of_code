import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)


# Canvas widget
canvas = tk.Canvas(window, width=200, height=200)

photo_image = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_29/password-manager-start/logo.png"
)
canvas.create_image((100, 100), image=photo_image)
canvas.pack()

window.mainloop()
