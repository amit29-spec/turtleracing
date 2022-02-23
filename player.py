from turtle import Turtle


class Game(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(y=-290, x=0)

    def start(self):
        self.goto(y=-290, x=0)

    def up(self):
        self.forward(20)

    def level(self):
        if self.ycor() > 285:
            return True
        else:
            return False

