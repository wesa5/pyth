from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from car_manager import CarManager
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car.create_car()
    car.move_car()

    #Detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            
    #Detect Successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()
    
     


screen.exitonclick()