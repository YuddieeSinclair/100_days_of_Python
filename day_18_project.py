#This is a reclaim of the HIRST painting project. 
# I will be using the turtle module to create a painting similar to the one created by HIRST.

#step 1: import modules screen and turtle
import turtle
from turtle import Turtle, Screen
import random

#step 2: set up the screen and turtle
turtle.colormode(255) # set the color mode to 255
screen = Screen()
t = Turtle()




rgb_colors = [
	(234, 232, 227), (230, 233, 239), (239, 231, 235), (228, 235, 231), (199, 162, 100), (62, 91, 128), (140, 170, 192),
			   (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49),
				 (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), 
			   (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187),
				 (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44)
]

dot_size = 20
dot_spacing = 50
rows = 10
col = 10
total = rows * col


#set the heading of the turtle to 225 and set its speed to 0.
t.setheading(225)
t.penup()
t.forward(400)
t.setheading(0)
t.speed(0)

#Loop through the total number of dots and set the color of the dot to a random color from the rgb_colors list.
for color_dots in range(1, total + 1):
    t.dot(dot_size, random.choice(rgb_colors))
    t.forward(dot_spacing) # move the turtle forward by the dot_spacing value.
    if color_dots % rows == 0: # if the color_dots is divisible by the rows, then move the turtle to the next row.
        t.left(90)
        t.forward(dot_spacing)
        t.left(90)
        t.forward(dot_spacing * rows) # move the turtle forward by the dot_spacing * rows value.
        t.setheading(0)





screen.exitonclick()