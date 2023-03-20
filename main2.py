from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win te race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

start_positions = [
    (-230, -100),
    (-230, -60),
    (-230, -20),
    (-230, 20),
    (-230, 60),
    (-230, 100),
]

turtles = []

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(start_positions[i])
    turtles.append(new_turtle)

if user_bet:  # if user didn't input anything this equals false
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
