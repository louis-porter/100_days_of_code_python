from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.generate_initial_cars()

    def generate_initial_cars(self):   
        for _ in range(30):
            self.generate_car()
    
    def generate_car(self):
        car = Turtle("square")
        car.pu()
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.goto(random.randint(-300,300), random.randint(-240,240))
        self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.seth(180)
            car.forward(STARTING_MOVE_DISTANCE)

    def reset_car(self):
        for car in self.cars:
            if car.xcor() < -300:
                car.setx(300)

    def increase_speed(self):
        for car in self.cars:
            car_speed = car.speed()
            car.speed(car_speed + MOVE_INCREMENT)
        
