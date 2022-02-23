colour = ["red", "blue", "green", "orange", "yellow", "black", "brown", "violet"]
import random
from turtle import Turtle
start_speed = 10


class Car:

    def __init__(self):
        self.all_cars = []
        self.car_speed = start_speed

    def create_car(self):
        rvalue = random.randint(1, 6)
        if rvalue == 1 or rvalue == 2:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colour))
            new_car.goto(x=300, y=(random.randint(-250, 250)))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += 5


