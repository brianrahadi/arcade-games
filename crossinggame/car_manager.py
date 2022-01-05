from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#CAR STARTING POSITION





class CarManager():
    def __init__(self):
        self.cars = []
        self.create_car()
        self.speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.choice([random.randint(-250,-40), random.randint(40, 250)]))
            new_car.seth(180)
            self.cars.append(new_car)

    
    def move(self):
        for car in self.cars:
            car.fd(self.speed)
    
    def increase_level(self):
        self.speed += MOVE_INCREMENT


        
        
