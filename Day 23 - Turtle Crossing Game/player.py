from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.goto(0,-275)
        self.seth(90)
        

    def move(self):
        self.forward(10)

    def reset(self):
        self.goto(0, -275)