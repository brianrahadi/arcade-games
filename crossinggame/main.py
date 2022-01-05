import time
from turtle import Screen
from .player import Player
from .car_manager import CarManager
from .scoreboard import Scoreboard
from .map import Map

def play_crossing(main_screen):
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.title("Turtle Crossing Game (Press M for Menu)")
    screen.tracer(0)

    pavement = Map()
    pavement.pavement()
    roadtop = Map()
    roadtop.road((0, 145))
    roadbot = Map()
    roadbot.road((0, -145))

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.move, "Up")

    screen.onkey(main_screen, 'm')


    cars = []
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move()

        for car in car_manager.cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()
                print("You Lose!")

        if player.ycor() > 280:
            player.reset_position()
            car_manager.increase_level()
            scoreboard.increase_level()


    screen.exitonclick()