from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.turtle_moves, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect when turtle goes *squish*
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.end_game()
            game_on = False

    # Detect when turtle reaches the other side
    if player.at_finish_line():
        player.turtle_reset()
        car_manager.speed_up()
        scoreboard.level_up()

screen.exitonclick()
