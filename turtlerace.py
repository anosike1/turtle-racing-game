# import Turtle and Screen from the Turtle module
from turtle import Turtle, Screen
# import random - we'll use this later
from random import *

# assign the boolean FALSE to a variable- this serves as a switch
is_race_on = False
# create and define the screen
screen = Screen()
screen.setup(width=500, height=400)
# create a list of the colors
colors = ["red","orange","yellow","green","blue","purple","violet","black"]
# create the y positions of the 8 turtles
ypos = [-155,-110,-65,-20,25,70,115,160]
# create an empty list for the turtles
all_turtles = []

# create a for loop that will run the number of times as the number of turtles
for turtle_pos in range (0,8):
    # each turtle will be created
    new = Turtle(shape="turtle")
    # select the colors of each turtle
    new.color(colors[turtle_pos])
    # use the penup() to prevent a line drawn by the turtle 
    new.penup()
    # let each turtle go to different y positions
    new.goto(x=-230,y=ypos[turtle_pos])
    # add the turtles to a list
    all_turtles.append(new)

# create a textinput to as the user for a color
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a colour: ")

# if the user places a bet, the SWITCH IS TURNED ON
if user_bet:
    is_race_on = True

# while the loop is on
while is_race_on:
    #...let EACH turtle 
    for turtle in all_turtles:
        #... move forward random distances
        rand_dist = randint (0,10)
        turtle.forward (rand_dist)

        # if ANY turtle moves close to the end of the screen
        if turtle.xcor()>230:
            # the SWITCH goes Off
            is_race_on=False
            # and the winning turtle iss assigned to the variable WINNER
            winner = turtle.pencolor()
            # if the WINNER is the same as the user's bet, print this...
            if winner==user_bet:                
                print (f"You Won! The {winner} turtle won!")
            # else print this
            else:
                print (f"You Lost! The {winner} turtle won!")
# this is used to get the screen to stay on until it is clicked
screen.exitonclick()