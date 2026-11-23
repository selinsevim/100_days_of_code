from tkinter import *

# creates a screen/window
window = Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# Label class
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.pack()

# in order to configure the text
my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    # my_label["text"] = "New Text"
    my_label.config(text=input.get())


# Button class
button = Button(window, text="Click me", width=25, command=button_clicked)
button.pack()

# Entry component
input = Entry(window, width=10)
input.pack()

# keeps the window open
window.mainloop()
