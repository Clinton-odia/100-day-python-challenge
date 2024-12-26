import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y_pos = -100


for color in colors:
  
  new_turtle = Turtle(shape="turtle")
  new_turtle.color(color)
  new_turtle.penup()
  new_turtle.goto(x=-230, y=y_pos)
  all_turtles.append(new_turtle)

  y_pos += 40

if user_bet:
  is_race_on = True

while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
      is_race_on = False
      winning_color = turtle.pencolor()
      if winning_color == user_bet:
        print(f"You've won.{winning_color} is the winning turtle")
      else:
        print(f"You've lost.{winning_color} is the winning turtle")
    random_distance = random.randint(1, 10)
    turtle.forward(random_distance)






screen.exitonclick()