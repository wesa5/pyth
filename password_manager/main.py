from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_letters = [choice(letters) for char in range(randint(8, 10))]
  password_symblos = [choice(symbols) for char in range(randint(2, 4))]
  password_numbers = [choice(numbers) for char in range(randint(2, 4))]

  password_list = password_letters + password_numbers + password_symblos
  shuffle(password_list)

  password = "".join(password_list)
  pass_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    web = web_input.get()
    user = use_input.get()
    pas = pass_input.get()

    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: \nEmail: {user} \nPassword: {pas} \n is it ok to save")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{web} | {user} | {pas}\n")
                web_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=100)


canvas = Canvas(width=200, height=200)
canva_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canva_img)
canvas.grid(column=1, row=0)

#Labels
web_label = Label(text="Website:")
web_label.config(pady=5)
web_label.grid(column=0, row=1)
use_label = Label(text="Email/Username:")
use_label.config(pady=5)
use_label.grid(column=0, row=2)
pass_label = Label(text="Pasword:")
pass_label.config(pady=5)
pass_label.grid(column=0, row=3)

#Inputs
web_input = Entry(width=41)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()
use_input = Entry(width=41)
use_input.grid(column=1, row=2, columnspan=2)
use_input.insert(0, "wesa@gmail.com")
pass_input = Entry(width=31)
pass_input.grid(column=1, row=3)

#Buttons
generate_button = Button(text="Generate password", command=generate_password)
generate_button.grid(column=2, row=3, columnspan=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()