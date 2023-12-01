from turtle import Turtle

FONT = ("Courier New", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto((-200, 260))
        self.level = 0
        self.level_up()

    def end_game(self):
        self.color("red")
        self.hideturtle()
        self.penup()
        self.home()
        self.write("GAME OVER", align="center",  font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)
