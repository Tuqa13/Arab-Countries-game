import turtle
import pandas

FONT = ('Courier', 10, "bold")

screen = turtle.Screen()
screen.title("Arab Countries Name Game!")
image = "ArabCountries.gif"
screen.bgpic(image)


# # To find the coordinates of the image
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)

data = pandas.read_csv("20_country.csv")
all_states = data.state.to_list()
guessed_states = []
game_is_on = True
score = 0
number_of_states = len(all_states)
x = turtle.Turtle()
x.penup()
x.hideturtle()


def check(idx_):
    global score
    if data.state[idx_] not in guessed_states:
        x.goto((data.x[idx_], data.y[idx_]))
        x.write(f"{data.state[idx_]}", True, 'center', FONT)
        score += 1
        guessed_states.append(data.state[idx_])


while game_is_on:
    user_guess = screen.textinput(title=f"{len(guessed_states)}/{number_of_states} Countries Correct",
                                  prompt="What's another Country's name?").title()
    if user_guess.title() == "Exit":
        game_is_on = False
        x.goto(0, 20)
        x.color('red')
        x.write(f"Your final score is {score}/{number_of_states}\n", True, 'center', ('Courier', 25, "bold"))
        x.goto(0, -20)
        x.write(f"Game Over!", True, 'center', ('Courier', 30, "bold"))

    if user_guess.lower() == "uae":
        idx = 10
        check(idx)
    if user_guess.title() in all_states:
        idx = all_states.index(user_guess.title())
        check(idx)
    if score == number_of_states:
        x.goto(0, 20)
        x.color('blue')
        x.write(f"Your final score is {score}/{number_of_states}\n", True, 'center', ('Courier', 25, "bold"))
        x.goto(0, -20)
        x.write(f"You Won!", True, 'center', ('Courier', 35, "bold"))
        game_is_on = False

screen.exitonclick()
