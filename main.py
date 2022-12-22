from turtle import Turtle, Screen
from player import Player
from random_cars import Cars
from new_level import New_level
import time 
screen = Screen()
screen.tracer(0)
player = Player()
cars = Cars()
screen.listen()
screen.onkey(player.player_up, "w")
screen.setup(width=800,height=600)

score = New_level()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.movement()
    

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
        
    
    if player.level_passed():
        player.go_to_start()
        cars.level_up()
        score.update()
   





screen.exitonclick()