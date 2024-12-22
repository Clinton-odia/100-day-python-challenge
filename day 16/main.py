from turtle import Turtle, Screen
from prettytable import PrettyTable
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("brown")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# table = PrettyTable()
# table.add_column("Pokemon Name", ["pikachu", "squirte","charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = 'l'

# print(table)
class person:
  def __init__(self, sex, age):
    self.sex = sex
    self.age = age

newperson = person("male",25)
print(newperson.sex)