from turtle import Turtle
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        with open("./snakegame/highscore.txt") as file:
            self.highscore = int(file.read())
        self.goto(x=0, y=270)
        self.update_scoreboard()
    

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}",  align="center", font=FONT)            

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("./snakegame/highscore.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


