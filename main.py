import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S stats game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491, width=725)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states_names = data.state.to_list()
guesses = []
while len(guesses) < 50:
    answer_text = screen.textinput(title=f"{len(guesses)}/50 correct", prompt="whats another state's name").title()
    print(answer_text)
    if answer_text == "Exit":
        missing_state = []
        for state in states_names:
            if state not in guesses:
                missing_state.append(state)
        missing = pandas.DataFrame(missing_state)
        missing.to_csv("missing_states.csv")
        break
    if answer_text in states_names:
        guesses.append(answer_text)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states = data[data.state == answer_text]
        t.goto(int(states.x), int(states.y))
        t.write(answer_text)


screen.exitonclick()
