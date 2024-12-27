from turtle import Turtle
MOVEMENT_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
current_direction = RIGHT
position = 0 
def Up():
  global position
  if current_direction != DOWN:
    position =  UP
def Down():
  global position
  if current_direction != UP:
    position = DOWN
def left():
  global position
  if current_direction != RIGHT:
    position = LEFT
def right():
  global position
  if current_direction != LEFT:
    position = RIGHT
class Snake:
  def __init__(self):
    self.segments = []
    self.x_pos = 0
    for _ in range(3):
      segment = Turtle(shape="square")
      segment.color("white")
      segment.penup()
      segment.goto(x=self.x_pos, y= 0)
      self.x_pos -= 20
      self.segments.append(segment)
  
  def move(self):
    global current_direction
    for seg_num in range(len(self.segments)-1, 0, -1):
      new_x = self.segments[seg_num - 1].xcor()
      new_y = self.segments[seg_num - 1].ycor()
      self.segments[seg_num].goto(new_x,new_y)
     
    self.segments[0].forward(MOVEMENT_DISTANCE)

    current_direction = position
    self.segments[0].setheading(position)

