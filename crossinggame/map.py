from turtle import Turtle

class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")

    def pavement(self):
        self.color("Aqua")
        self.shapesize(stretch_len=30, stretch_wid=2)

    def road(self, position):
        self.goto(position)
        self.color("gray80")
        self.shapesize(stretch_len=30, stretch_wid=12)