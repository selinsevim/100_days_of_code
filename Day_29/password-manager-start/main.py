import tkinter as tk
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open(
        "/Users/selinsevim/Documents/100_days_of_code/Day_29/password-manager-start/data.txt",
        "a",
    ) as f:
        website_content = website_entry.get()
        email_content = email_entry.get()
        password_content = password_entry.get()

        if website_content == "" or password_content == "":
            messagebox.showinfo(
                title="Warning", message="Please don't leave any fields blank"
            )
        else:
            is_ok = messagebox.askokcancel(
                title=website_content,
                message=f"Are you approving? {email_content}, {password_content}? Is it ok to save?",
            )
            if is_ok:
                f.write(f"{website_content} | {email_content} | {password_content}\n")
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
password_entry = tk.Entry(width=20)
password_entry.grid(row=3, column=1)

# generate button
generate_button = tk.Button(text="Generate Password", width=12)
generate_button.grid(row=3, column=2)

# add button
add_button = tk.Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
