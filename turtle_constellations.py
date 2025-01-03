#Create a program that uses turtles to draw random star-like patterns on the screen.
#The program should prompt the user for the number of stars to draw and the size of the stars.
#The stars should be drawn in random locations on the screen, with random colors and sizes.
#The program should continue drawing stars until the user closes the window.

from turtle import Turtle, Screen
import random

# Set up the screen
screen = Screen()
screen.colormode(255)  # Use RGB color mode
screen.screensize(800, 800)  # Set screen size
screen.bgcolor("black")  # Set background color

# Create a turtle
t = Turtle()
t.color("white")  # Initial color

# Function to draw a star
def draw_star(length):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    t.color(R, G, B)  # Set random color
    
    for star_number in range(5):  # Draw a star with 5 points
        t.forward(length)
        t.right(144)
        t.speed("fastest")

# Function to move the turtle to a random location
def random_location():
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)

    t.penup()
    t.goto(x=x, y=y)  # Move to random position
    t.pendown()
    draw_star(star_length)  # Draw star at the new position

# Prompt user for number of stars and length of each star
star_size = screen.numinput(title="Star Size", prompt="How many stars will you like to have")
star_length = screen.numinput(title="Length of Line", prompt="what will be the length of star", minval=10, maxval=100)

# Loop to draw the specified number of stars
for _ in range(int(star_size)):
    random_location()

# Wait for user to close the window
screen.exitonclick()