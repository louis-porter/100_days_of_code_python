from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


def button_pressed():
    conversion = float(input.get()) * 1.60934
    output["text"] = conversion


# Text Input
input = Entry(width=10)
input.insert(END, "0")
input.grid(column=2, row=0) 


# Miles Label
miles = Label(text="Miles")
miles.grid(column=3, row=0) 

# Equal Label
equals = Label(text="is equal to")
equals.grid(column=1, row=1)

# Output Label
output = Label(text=0)
output.grid(column=2, row=1)

# Km Label
km = Label(text="Km")
km.grid(column=3, row=1)

# Button
button = Button(text="Calculate", command=button_pressed)
button.grid(column=2, row=2)




window.mainloop()