BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
import csv

#===========GENERATE NEW FLASH CARD============#

try:
    data = pd.read_csv(r"Day 31 - Flash Card App Capstone Project\data\words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv(r"Day 31 - Flash Card App Capstone Project\data\french_words.csv")
words = data.to_dict(orient="records")
current_card = {}

def generate_new_word():
    global current_card
    current_card = random.choice(words)
    french_random_word = current_card["French"]
    canvas.itemconfig(front_card, image=front_card_image)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(french_text, text=french_random_word, fill="black")
    window.after(3000, flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(front_card, image=back_card_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(french_text, text=current_card["English"], fill="white")

#=================SAVE RESULTS=================#
def is_known():
    global current_card
    words.remove(current_card)
    generate_new_word()
    data = pd.DataFrame(words)
    data.to_csv(r"Day 31 - Flash Card App Capstone Project\data\words_to_learn.csv")

#===================UI SETUP===================#
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Create Canvas
canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=900, height=650) 
canvas.grid(column=0, row=0, columnspan=2)

front_card_image = PhotoImage(file=r"Day 31 - Flash Card App Capstone Project\images\card_front.png")
back_card_image = PhotoImage(file=r"Day 31 - Flash Card App Capstone Project\images\card_back.png")
right_image = PhotoImage(file=r"Day 31 - Flash Card App Capstone Project\images\right.png")
wrong_image = PhotoImage(file=r"Day 31 - Flash Card App Capstone Project\images\wrong.png")

front_card = canvas.create_image(450, 325, image=front_card_image)
language_text = canvas.create_text(440, 150,text="French", font=("Ariel", 35, "italic"))
french_text = canvas.create_text(440,290, font=("Ariel", 55, "bold"))


# Create Tick button
tick_button = Button(image=right_image, highlightthickness=0, command=is_known)
tick_button.grid(column=1, row=1)


# Create X button
x_button = Button(image=wrong_image, highlightthickness=0, command=generate_new_word)
x_button.grid(column=0,row=1)

generate_new_word()


window.mainloop()