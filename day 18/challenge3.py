from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

# for _ in range(4):
#   timmy_the_turtle.forward(100)
#   timmy_the_turtle.right(90)


def game(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(angle)
for num in range(3, 11):
  game(num)


screen = timmy_the_turtle.screen
screen.exitonclick()