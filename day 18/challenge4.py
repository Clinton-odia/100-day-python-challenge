import random
import turtle
from turtle import Turtle, Screen, colormode

timmy_the_turtle = Turtle()

turtle.colormode(255)
def random_color():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  return (r,g,b)

direction = [0, 90, 180, 270]
timmy_the_turtle.pensize(12)
timmy_the_turtle.speed("fastest")

for _ in range(200):
  timmy_the_turtle.color(random_color())
  timmy_the_turtle.forward(30)
  timmy_the_turtle.setheading(random.choice(direction))

screen = timmy_the_turtle.screen
screen.exitonclick()