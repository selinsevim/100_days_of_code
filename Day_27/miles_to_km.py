from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
# add padding to the screen
window.config(padx=20, pady=20)


def calculate():
    miles = int(miles_entry.get())
    km = miles * 1.60934
    km_label.config(text=km)


# Miles Entry
miles_entry = Entry(window, width=10)
miles_entry.grid(column=1, row=0)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

km_text = Label(text="is equal to")
km_text.grid(column=0, row=1)

# KM Entry
km_label = Label(text=0, width=10)
km_label.grid(column=1, row=1)

km_text_2 = Label(text="Km")
km_text_2.grid(column=2, row=1)

# Calculate Button
calculate_button = Button(window, text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()
