# from turtle import Screen, shape
import turtle
import pandas
screen = turtle.Screen()

screen.title("U.S. States Game")
image = "Python100daycode/Day25/us_states_game/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)


turtle = turtle.Turtle()
turtle.hideturtle()
turtle.penup()

## get the on screen coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

state_data = pandas.read_csv("Python100daycode/Day25/us_states_game/50_states.csv")

# print(state_data["state"])

score = 0
guessed_state = []

#all_states = state_data["state"].to_list()   # this is useful if used .title()

def check_state(input_state):
    global score
    # if (input_state in all_state) and (input_state not in guessed_state):  # alternative method when used .title()
    for state in state_data["state"]:
        if (state.lower() == input_state) and (state not in guessed_state):
            guessed_state.append(state)
            x = int(state_data[state_data["state"] == state].x.iloc[0])
            y = int(state_data[state_data["state"] == state].y.iloc[0])
            turtle.goto(x,y)
            turtle.write(arg= f"{state}")
            score += 1
           

game_is_on = True
# print(len(state_data))

while game_is_on and score<len(state_data):
    answer_state = screen.textinput(title=f"Guess State {score}/50", prompt="Type state's name.").lower()  #.title()  #as our data is in title
    if answer_state == "exit":
        break
    check_state(answer_state)
    if score == 50:
        turtle.goto(0,0)
    

# print(state_data["state"])
# print(state_data["x"])
# print(state_data["y"])

# print(state_data[state_data.state])

# USING LIST COMPREHENSION 
remaining_state = [state for state in state_data["state"] if state not in guessed_state]

# remaining_state = []

# for state in state_data["state"]:
#     if state not in guessed_state:
#         remaining_state.append(state)



data=pandas.DataFrame(remaining_state)

data.to_csv("Python100daycode/Day25/us_states_game/learn_state.csv")

# screen.exitonclick()