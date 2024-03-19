"""
This Python script uses the turtle graphics library to draw geometric figures based on user input.

Instructions:
1. Run the script.
2. When prompted, enter the number of sides for the figure.
3. Enter the length of the sides.
4. Enter the number of rotations you want for the figure.
5. If you want to draw a new figure, enter "Y" when asked. Otherwise, enter "N".
"""

# Import the Turtle and Screen modules
from turtle import Turtle, Screen

# Initialize a variable to control the main loop
i = "Y"

# Create a new Screen object
scrn = Screen()
# Set the window size of the screen to 700 pixels wide and 500 pixels high
scrn.setup(500,500)
# Set the size of the canvas (the drawable area) to 400 pixels wide and 200 pixels high
scrn.screensize(400,200)

# Main loop to draw figures
while i == "Y":
    # Create a new turtle
    turtle = Turtle()

    # Ask the user for the number of sides of the figure
    num_sides = int(input("Enter the number of sides for the figure: "))

    # Ask the user for the length of the sides
    side_length = int(input("Enter the length of the sides: "))
    side_length *= 2

    # Calculate the angle to turn at each corner
    angle = 180 - (((num_sides - 2) / num_sides) * 180)

    # If the number of sides is greater than 3, draw the figure
    if num_sides > 3:       
        for _ in range(num_sides):
            turtle.left(angle)
            turtle.forward(side_length)    
    else:
        print("Cannot draw a figure with less than 4 sides.")

    # Ask the user for the number of rotations
    print("Enter the number of rotations you want for the figure: ")
    num_rotations = int(input())

    # Define a function to draw a rotation
    def draw_rotation():           
        for _ in range(1, num_sides + 1):
            turtle.left(360 / num_sides)
            turtle.forward(side_length) 

    # Draw the rotations
    for _ in range(1, num_rotations + 1):
        draw_rotation()
        turtle.left(180 - (360 / num_sides))

    # End the fill of the turtle
    turtle.end_fill()

    # Ask the user if they want to draw a new figure
    print("Do you want to draw a new figure? (Y/N)")
    i = str(input("")).upper()

    # If the user wants to draw a new figure, clear the current figure
    if i == "Y":
        turtle.clear()
