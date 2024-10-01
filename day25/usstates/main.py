import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 states correct", prompt="What's another state's name ?")
    df = pd.read_csv('50_states.csv')
    answer_state.capitalize()
    all_states = df.state.to_list()
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        guessed_state.append(answer_state)
    else:
        screen._write(pos=(50,50), txt="Game Over", align='r', font="ariel", pencolor='black')
        break




turtle.mainloop()