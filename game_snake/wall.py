
class Wall:
    def __init__(self):
        super().__init__()
        self.x =0
        self.y=0
        
    
        def check_wall(self):
            self.x= .xcor()
            self.y=.ycor()
            right_wall = 600 / 2    
            left_wall = -600 / 2    
            top_wall = 600 / 2      
            bottom_wall = -600 / 2 
            if self.x > right_wall or self.x < left_wall or self.y > top_wall or self.y < bottom_wall:
                print("Game Over")