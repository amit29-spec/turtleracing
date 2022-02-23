import time
from turtle import Screen
from player import Game
from cars import Car
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Game()
cars = Car()
point = Score()

screen.onkey(tim.up, "Up")

screen.listen()
switch = True
while switch:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()
    for car in cars.all_cars:
        if car.distance(tim) < 25:
            switch = False
            point.over()
    if tim.level():
        tim.start()
        cars.level_up()
        point.increase()

screen.exitonclick()
