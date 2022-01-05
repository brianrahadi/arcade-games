from turtle import Turtle, colormode
import random


def random_color():
    colormode(255)

    R = random.randint(70, 255)
    G = random.randint(70, 255)
    B = random.randint(70, 255)
    randomcolor = (R, G, B)
    return randomcolor

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()
        
        
    def refresh(self):
        self.color(random_color())
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)