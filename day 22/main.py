from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
game_ball = Ball()

screen.listen()
screen.onkey(fun=r_paddle.UP, key= "Up")
screen.onkey(fun=r_paddle.DOWN, key= "Down")

screen.onkey(fun=l_paddle.UP, key= "w")
screen.onkey(fun=l_paddle.DOWN, key= "s")
game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  game_ball.move()
  #detect collision with wall
  if game_ball.ycor() > 280 or game_ball.ycor() < -280:
    game_ball.bounce_y()

  #detect collision with paddle

  if  game_ball.distance(r_paddle) < 50 and game_ball.xcor() > 320 or game_ball.distance(l_paddle) and game_ball.xcor() < -320:
    game_ball.bounce_x()

screen.exitonclick()