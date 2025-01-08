import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"day 25\US_STATE_GAME\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="Guess the state", prompt= "What's another state's name?")
turtle.mainloop()
