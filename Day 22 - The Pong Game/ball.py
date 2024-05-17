from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed_value = 0.1
        self.x_dir = 10
        self.y_dir = 10
    

    def move(self):
        new_x = self.xcor() + self.x_dir
        new_y = self.ycor() + self.y_dir
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_dir *= -1

    def bounce_x(self):
        self.x_dir *= -1
        self.speed_value *= 0.9

    def reset(self):
        self.goto(0,0)
        self.x_dir *= -1
        self.speed_value = 0.1

    