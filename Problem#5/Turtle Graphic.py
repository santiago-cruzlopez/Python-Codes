"""
Turtle Graphic

This script uses the turtle module to draw a spiral star pattern on the screen. The turtle moves forward a certain number of pixels, 
then turns right 144 degrees, repeating this process to form the spiral star pattern. The screen closes when the user clicks on it.

This script requires that `turtle` be installed within the Python environment you are running this script in.

This file can also be imported as a module and contains the following functions:

    * draw_spiral_star - draws a spiral star pattern on the screen
"""

from turtle import Screen, Turtle

def draw_spiral_star():
    """
    Draws a spiral star pattern on the screen using the turtle module.

    Parameters:
        None

    Returns:
        None
    """
    # Create a new Screen object
    scrn = Screen()
    # Set the window size of the screen to 700 pixels wide and 500 pixels high
    scrn.setup(700,500)
    # Set the size of the canvas (the drawable area) to 400 pixels wide and 200 pixels high
    scrn.screensize(400,200)

    # Create a new Turtle object
    tort = Turtle()
    tort.speed(10)  # Increase the speed of the turtle

    # Draw a spiral star pattern
    for i in range(50):
        tort.forward(i * 10)  # Move the turtle forward by 'i * 10' pixels
        tort.right(144)  # Rotate the turtle 144 degrees to the right

    # Close the screen when the user clicks on it
    scrn.exitonclick()

if __name__ == "__main__":
    draw_spiral_star()