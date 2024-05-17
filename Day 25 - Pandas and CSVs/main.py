import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = r"Day 25 - Pandas and CSVs\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_answers = 0
guessed_states = []
t = turtle.Turtle()
t.pu()
t.hideturtle()

data = pd.read_csv(r"Day 25 - Pandas and CSVs\50_states.csv")
states = data["state"].to_list()


while len(guessed_states) <50:
    answer_state = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="Guess the name of a state").title()

    if answer_state == "Exit":
        break
    if answer_state in states:
        correct_answers += 1
        guessed_states.append(answer_state)
        answer_row = data[data["state"] == answer_state]
        t.goto(int(answer_row.x), int(answer_row.y))
        t.write(answer_state)

missed_states = [state for state in states if state not in guessed_states]


df = pd.DataFrame(missed_states)
df.to_csv(r"Day 25 - Pandas and CSVs\states_to_learn.csv")