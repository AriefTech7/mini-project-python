from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,500)
        self.write(arg=f"Score = {self.score}",align="center",font=("DejaVu Sans",50,"bold"))    
        self.hideturtle()
        
    
       