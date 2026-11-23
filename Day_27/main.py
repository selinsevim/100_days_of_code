from tkinter import *

# creates a screen/window
window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)
# add padding to the screen
window.config(padx=100, pady=100)


def button_clicked():
    # my_label["text"] = "New Text"
    my_label.config(text=input.get())


# Label class
my_label = Label(text="I am a label", font=("Arial", 24))
# in order to configure the text
my_label["text"] = "New Text"
my_label.config(text="New Text")
# Positioning option 1: pack
# my_label.pack()

# Postioning option 2: place , directly place it
# my_label.place(x=0, y=100)

# Postioning option 3: grid
my_label.grid(column=0, row=0)

# Button class
button = Button(window, text="Click me", width=10, command=button_clicked)
# button.pack(side="left")
button.grid(column=1, row=1)

# New Button class
new_button = Button(window, text="Click me - new", width=10, command=button_clicked)
# button.pack(side="left")
new_button.grid(column=2, row=0)

# Entry component
input = Entry(window, width=10)
# input.pack()
input.grid(column=3, row=2)

# keeps the window open
window.mainloop()
