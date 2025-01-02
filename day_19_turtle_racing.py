from turtle import Turtle,  Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="welcome to the turtle racing game.", prompt= "Place your bets on which turtle will win")
colors = ["red", "orange", "cyan", "green", "blue", "purple"]
turtles = []
y_axis = [-100, -70, -40, -10, 20, 50]
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_axis[i])
    turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:

    for one_turtle in turtles:
        if one_turtle.xcor() > 230:
            race_on = False
            winner = one_turtle.pencolor()
            if winner == user_bet:
                print(f"You win, {winner} wins")
            else:
                print(f"You lose, {winner} wins")

        random_distance = random.randint(0, 10)
        one_turtle.forward(random_distance)
    









screen.exitonclick()