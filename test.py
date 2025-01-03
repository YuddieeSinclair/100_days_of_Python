from turtle import Turtle, Screen

# Create a Screen object to control the turtle graphics window
screen = Screen()

# Define a function to draw a shape with a given number of sides and length
def draw_shape(sides, length):
    # Create the first turtle, set its shape, color, and speed
    t1 = Turtle()
    t1.shape("turtle")
    t1.color("red")
    t1.speed("fastest")

    # Create the second turtle, set its shape, color, and speed
    t2 = Turtle()
    t2.shape("turtle")
    t2.color("blue")
    t2.speed("fastest")

    # Calculate the angle each turtle needs to turn to create the shape
    angle = int(360 / sides)

    # Loop to draw the shape
    for _ in range(int(sides)):
        t1.forward(length)  # Move the first turtle forward by the length
        t1.right(angle)     # Turn the first turtle right by the calculated angle
        t2.forward(length)  # Move the second turtle forward by the length
        t2.right(angle)     # Turn the second turtle right by the calculated angle

    # Keep the window open until a click is detected
    screen.exitonclick()

# Example usage:
# Prompt the user to input the number of sides for the shape
sides = screen.numinput("Enter the number of sides: ", "Enter the number of sides: ", 4, minval=3, maxval=10)
# Prompt the user to input the length of the sides for the shape
length = screen.numinput("Enter the length of sides: ", "Enter the length of sides: ", 100)
# Call the draw_shape function with the user inputs
draw_shape(sides, length)