#This is an etch-a-sketch app built in python using the turtle module; to explain event listeners

from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_left():
    t.left(10)

def move_right():
    t.right(10)

def clear_screen():
    t.clear()
    t.penup()
    t.home()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=clear_screen, key="c")






screen.exitonclick()