import turtle as t
from colors import rgb_colors
import random

print(rgb_colors)

screen = t.Screen()
screen.colormode(255)
tim = t.Turtle()
tim.pensize(15)
tim.speed("fastest")

for i in range(0,10):
    tim.home()
    tim.left(90)
    tim.forward(i*50)
    tim.right(90)
    for j in range(10):
        tim.pencolor(random.choice(rgb_colors))
        tim.pd()
        tim.dot()
        tim.pu()
        tim.forward(50)
        tim.pd()
    tim.pu()
    



    









screen.exitonclick()

