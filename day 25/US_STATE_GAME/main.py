import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"day 25\US_STATE_GAME\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(r"day 25\US_STATE_GAME\50_states.csv")
all_state = data.state.to_list()
gussed_states = []
# print(us_state)
# Guess = answer_state.title()
while len(gussed_states) < 50:

  answer_state = screen.textinput(title=f"{len(gussed_states)}/50Guess the state", prompt= "What's another state's name?").title()

  if answer_state == 'Exit':
    missing_states = []
    for state in all_state:
      if state not in gussed_states:
        missing_states.append(state)
        newdata = pandas.DataFrame(missing_states)
        newdata.to_csv("state_to_learn.csv")
    break
  if answer_state in all_state:
    gussed_states.append(answer_state)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(answer_state)



#state_to_learn.csv
turtle.mainloop()
