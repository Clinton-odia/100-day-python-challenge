from turtle import Screen, Turtle
import time
from snake import Snake, Up, Down, left, right
#set the screen and background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#creation of the block or segment of the snake body

snake = Snake()
screen.onkey(fun= Up, key="Up")
screen.onkey(fun= Down, key="Down")
screen.onkey(fun= right, key="Right")
screen.onkey(fun= left, key="Left")
screen.listen()
game_is_on = True
#to animate the body of the snake
while game_is_on:
  screen.update()
  time.sleep(0.1)

  snake.move()
  


screen.exitonclick()