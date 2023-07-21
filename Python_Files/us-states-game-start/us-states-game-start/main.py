import turtle
import pandas
screen = turtle.Screen()
screen.title("US_State_Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
score = 0
list_state = []
while len(list_state) < 50:
    Guess = (screen.textinput(title=f"Your score is {score}/50 : ", prompt="What's another state : ")).title()
    if Guess =="Exit":
        missing_state = [miss for miss in all_state if miss not in list_state]
        Remaining =pandas.DataFrame(missing_state)
        print(f"Missing states is {Remaining} ")
        Remaining.to_csv("remain")
        break
    if Guess in all_state:
        G_state = data[data.state == Guess]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(G_state.x), int(G_state.y))
        t.write(Guess)
        list_state.append(Guess)
        score += 1
