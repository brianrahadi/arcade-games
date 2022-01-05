from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.level = -1
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"LEVEL: {self.level}", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 80, "normal"))
