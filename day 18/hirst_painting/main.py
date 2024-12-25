import turtle as t
import random
# import colorgram

# colours = colorgram.extract('hirst.jpg', 15)

# rgb_colours =  []

# for color in colours:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   new_color = (r, g, b)
#   rgb_colours.append(new_color)

t.colormode(255)

# print(rgb_colours)
colours = [ (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12)]

timmy = t.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
  timmy.dot(20,random.choice(colours))
  timmy.forward(50)
  
  if dot_count % 10 == 0:
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)
    
screen = t.Screen()
screen.exitonclick()