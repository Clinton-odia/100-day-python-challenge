import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_pos = -100

for color in colors:
  
  tim = Turtle(shape="turtle")
  tim.color(color)
  tim.penup()
  tim.goto(x=-230, y=y_pos)
  y_pos += 40



screen.exitonclick()