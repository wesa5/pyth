from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

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
    new_data = {
        web : {
            "email": user,
            "password": pas
        }
        }
    

    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="Oops", message="Don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old Data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old Data with new_data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)


def find_password():
    web = web_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file not found")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(title=web, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(title="Not Found", message=f"There's no saved details for {web}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=100, bg="#C2DED1")


canvas = Canvas(width=200, height=200, bg="#371B58", highlightthickness=0)
canva_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=canva_img)
canvas.grid(column=1, row=0)

#Labels
web_label = Label(text="Website:",bg="#CDC2AE",)
web_label.grid(column=0, row=1)
use_label = Label(text="Email/Username:", bg="#CDC2AE",)
use_label.config(pady=5)
use_label.grid(column=0, row=2)
pass_label = Label(text="Pasword:",bg="#CDC2AE", fg="#371B58")
pass_label.config(pady=5)
pass_label.grid(column=0, row=3)

#Inputs
web_input = Entry(width=35)
web_input.grid(column=1, row=1)
web_input.focus()
use_input = Entry(width=65)
use_input.grid(column=1, row=2, columnspan=3)
use_input.insert(0, "wesa@gmail.com")
pass_input = Entry(width=35)
pass_input.grid(column=1, row=3)

#Buttons
generate_button = Button(text="Generate password", width=22, command=generate_password)
generate_button.grid(column=2, row=3, columnspan=2)
add_button = Button(text="Add", width=56, command=save)
add_button.grid(column=1, row=4, columnspan=3)
search_button = Button(text="Search", width=22, command=find_password)
search_button.grid(column=3, row=1)

window.mainloop()