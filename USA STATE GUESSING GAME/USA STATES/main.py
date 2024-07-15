import turtle
import pandas


screen = turtle.Screen()
screen.title("USA State Guessing Game")
pic = "state.gif"
screen.addshape(pic)
turtle.shape(pic)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guesses_state = [ ]

while len(guesses_state) < 50:

    answer_state = screen.textinput(title=f"{len(guesses_state)}/50 States Correct",prompt="What's another state?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guesses_state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guesses_state.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        tim.color("red")
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x),int(state_data.y))
        tim.write(answer_state, align="center", font=("Arial", 10, "normal"))


