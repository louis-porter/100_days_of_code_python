import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_car()
    car.reset_car()

    #Detect collision with car
    for car_ in car.cars:
        if player.distance(car_) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect collision with far wall
    if player.ycor() > 280:
        car.increase_speed()
        player.reset()
        scoreboard.update_scoreboard()

screen.exitonclick()