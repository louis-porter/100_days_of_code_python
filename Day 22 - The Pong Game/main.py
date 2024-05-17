from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

lpaddle = Paddle(-350,0)
rpaddle = Paddle(350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(lpaddle.up,"w")
screen.onkey(lpaddle.down,"s")
screen.onkey(rpaddle.up,"Up")
screen.onkey(rpaddle.down,"Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.speed_value)
    screen.update()
    ball.move()
    
    #Detect collision with top/bottom wall
    if ball.ycor() == -280 or ball.ycor() == 280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect collision with left/right ball
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()




screen.exitonclick()