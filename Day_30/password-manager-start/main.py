import tkinter as tk
from tkinter import messagebox
import random
import json


# ---------------------------- SEARCH ------------------------------- #
def search():
    # upload the data first
    try:
        with open(
            "/Users/selinsevim/Documents/100_days_of_code/Day_30/password-manager-start/data.json",
            "r",
        ) as data_file:  # r -> load(read) and update
            # Read old data from json file
            data = json.load(data_file)
            # get the entry of website
            website_request = website_entry.get()
            email = data[website_request]["email"]
            password = data[website_request]["password"]
            messagebox.showinfo(
                title=website_request,
                message=f"Email address is {email} and password is {password}",
            )

    except:
        print("There is no file")
        messagebox.showinfo(title="Warning", message="There is no file!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list_1 = [random.choice(letters) for _ in range(nr_letters)]

    password_list_2 = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list_3 = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_list_1 + password_list_2 + password_list_3

    random.shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    return password


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_content = website_entry.get()
    email_content = email_entry.get()
    password_content = password_entry.get()
    new_data = {
        website_content: {
            "email": email_content,
            "password": password_content,
        }
    }

    if website_content == "" or password_content == "":
        messagebox.showinfo(
            title="Warning", message="Please don't leave any fields blank"
        )
    else:
        try:
            # if there is already data.json file
            with open(
                "/Users/selinsevim/Documents/100_days_of_code/Day_30/password-manager-start/data.json",
                "r",
            ) as data_file:  # r -> load(read) and update
                # Read old data from json file
                data = json.load(
                    data_file
                )  # it needs to be in read mode, this converts json -> python dict

        except FileNotFoundError:
            # if there is no data.json file w -> dump (writing into)
            with open(
                "/Users/selinsevim/Documents/100_days_of_code/Day_30/password-manager-start/data.json",
                "w",
            ) as data_file:
                json.dump(
                    new_data, data_file, indent=4
                )  # write new data into the new data
        else:
            data.update(new_data)

            with open(
                "/Users/selinsevim/Documents/100_days_of_code/Day_30/password-manager-start/data.json",
                "w",
            ) as data_file:
                json.dump(data, data_file, indent=4)  # write new data into the new data
        finally:
            # clean the boxes after the saved
            website_entry.delete(0, "end")
            # email_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# Canvas widget
canvas = tk.Canvas(window, width=200, height=200)

photo_image = tk.PhotoImage(
    file="/Users/selinsevim/Documents/100_days_of_code/Day_29/password-manager-start/logo.png"
)
canvas.create_image((100, 100), image=photo_image)
canvas.grid(row=0, column=1)

# Website Text
website_text = tk.Label(text="Website:")
website_text.grid(row=1, column=0)
# Website Entry
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

# Email Text
email_text = tk.Label(text="Email/Username:")
email_text.grid(row=2, column=0)
# Email Entry
email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
# Prepopulate the email
email_entry.insert(0, "selin@gmail.com")

# Password Text
password_text = tk.Label(text="Password:")
password_text.grid(row=3, column=0)
# Password Entry
password_entry = tk.Entry(width=23)
password_entry.grid(row=3, column=1)

# generate button
generate_button = tk.Button(
    text="Generate Password", width=10, command=generate_password
)
generate_button.grid(row=3, column=2)

# search button
search_button = tk.Button(text="Search", width=10, command=search)
search_button.grid(row=1, column=2)

# add button
add_button = tk.Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
