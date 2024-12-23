import random
from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

colours = ["red", "blue", "brown", "SeaGreen", "SlateGray"]
direction = [0, 90, 180, 270]
timmy_the_turtle.pensize(12)
timmy_the_turtle.speed("fastest")

for _ in range(200):
  timmy_the_turtle.color(random.choice(colours))
  timmy_the_turtle.forward(30)
  timmy_the_turtle.setheading(random.choice(direction))

screen = timmy_the_turtle.screen
screen.exitonclick()