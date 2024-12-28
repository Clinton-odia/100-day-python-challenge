from turtle import Screen, Turtle
import time
from snake import Snake, Up, Down, left, right
from food import Food
from scoreboard import Scoreboard
#set the screen and background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#creation of the block or segment of the snake body

snake = Snake()
food = Food()
scoreboard = Scoreboard()
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
  # scoreboard.update_scoreboard()

  snake.move()
  
  #detect collision
  if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.increase_score()
    snake.add_segment()

  #detect collison with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False
    scoreboard.game_over()

  #detect collison with tail
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      game_is_on = False
      scoreboard.game_over()

screen.exitonclick()