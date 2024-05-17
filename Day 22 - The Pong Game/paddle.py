from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.turtlesize(4,1)
        self.color("white")
        self.pu()
        self.speed("fastest")
        self.goto(x=x_cor, y=y_cor)


    def up(self):
        self.sety(self.ycor() + 20)

    def down(self):
        self.sety(self.ycor() - 20)
        