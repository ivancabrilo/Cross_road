from turtle import Turtle

class New_level(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-380,260)
        self.write(f"Level: {self.score}", align="left", font=("Courier", 20, "normal"))
        self.hideturtle()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="left", font=("Courier", 20, "normal"))
       
        

        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Courier", 30, "normal"))