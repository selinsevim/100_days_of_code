import tkinter

# creates a screen/window
window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# Label class
my_label = tkinter.Label(text="I am a label", font=("Arial", 24))
my_label.pack()

# keeps the window open
window.mainloop()
