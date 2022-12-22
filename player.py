from turtle import Turtle 
STARTING_POSTION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.color("green")
        self.goto(STARTING_POSTION)

    def player_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSTION)



    def level_passed(self):
        if  self.ycor() > 280:
           return True
        else:
            return False