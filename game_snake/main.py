from turtle import Screen
from snake import Snake
import time
def main():
    screen = Screen()
    screen.setup(width=600,height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")    
    screen.tracer(0)
       
    snake = Snake()
        
    game_on = True
    while game_on:
        
        time.sleep(0.2)
        snake.move()
        screen.update()
        
    screen.exitonclick()
if __name__ == "__main__":
    main()