from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("honeydew")
        self.penup()
        self.setheading(90)
        self.turtle_reset()

    def turtle_moves(self):
        """Moves the player towards the top of the screen"""
        self.forward(MOVE_DISTANCE)

    def turtle_reset(self):
        """Resets turtle to start new level"""
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        """Confirms whether player has completed the level"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
