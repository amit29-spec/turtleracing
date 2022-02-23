from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("red")
        self.penup()
        self.goto(x=-230, y=260)
        self.hideturtle()
        self.write(f"LEVEL:{self.level}", False, align="center", font=("Arial", 24, "normal"))

    def increase(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL:{self.level}", False, align="center", font=("Arial", 24, "normal"))

    def over(self):
        self.color("red")
        self.penup()
        self.goto(x=0, y=0)
        self.hideturtle()
        self.write(f"GAME OVER", False, align="center", font=("Arial", 24, "normal"))


