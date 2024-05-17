from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win a race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles=[]

for i, turtle in enumerate(colours):
    turtle = Turtle(shape="turtle")
    turtle.color(colours[i])
    turtle.pu()
    turtle.goto(x=-235, y=((i+1)*30)+-100)
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
            is_race_on = False
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)






screen.exitonclick()