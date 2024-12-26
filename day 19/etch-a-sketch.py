import turtle
from turtle import Turtle, Screen

tim = Turtle()

def forward():
  tim.forward(10)
def backward():
  tim.backward(10)
def clearscreen():
  tim.reset()
def clockwise():
  tim.right(25)
def counter_clockwise():
  tim.left(25)


screen = Screen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=backward)
screen.onkey(key="c", fun=clearscreen)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='a', fun=counter_clockwise)

screen.listen()
screen.exitonclick()