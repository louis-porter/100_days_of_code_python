from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letter_list = [random.choice(letters) for _ in range(nr_letters)]
    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]
    number_list = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_login_to_file():
    email = email_input.get()
    website = website_input.get()
    password = password_input.get() 
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    
    fields_empty = False
    if website == "" or password == "":
        fields_empty = True

    if fields_empty:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}"
                           f"\n Password: {password}\nIs it OK to save?")
        if is_ok:
            try:
                with open(r"Day 29 - Password Manager\data.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open(r"Day 29 - Password Manager\data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)
                with open(r"Day 29 - Password Manager\data.json", "w") as f:
                    json.dump(data, f, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

# ------------------------- FIND  PASSWORD ---------------------------- #
def find_password():
    website_search = website_input.get()
    try:
        with open(r"Day 29 - Password Manager\data.json", "r") as f:
            data = json.load(f)
        if website_search in data.keys():
            messagebox.showinfo(title=f"{website_search} Login", message=f"Email: {data[website_search]["email"]}"
                                    f"\nPassword: {data[website_search]["password"]}")
        else:
            messagebox.showinfo(title="Error", message="No details for that website exist.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
        
    
    

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file=r"Day 29 - Password Manager\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, columnspan=2)

website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
website_input = Entry(width=21) 
website_input.grid(column=1, row=1)
website_input.focus()
website_search = Button(text="Search", width=15, command=find_password)
website_search.grid(column=2, row=1)

email_label = Label(text="Email/Username: ")
email_label.grid(column=0, row=2)
email_input = Entry(width=40)  
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "louis.porter12@hotmail.co.uk")

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)
password_input = Entry(width=22) 
password_input.grid(column=1, row=3)
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=save_login_to_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
