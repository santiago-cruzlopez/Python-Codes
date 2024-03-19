"""
Perimeter of Circle

This script allows the user to calculate the perimeter of a circle given its radius.

Formula: 2*pi*radius.

The script prompts the user to enter the radius of the circle, and then it calculates and prints the perimeter.

The output is formatted to two decimal places.

"""

from math import pi

def calculate_perimeter(radius):
    return 2 * pi * radius

def main():
    print("Calculate the perimeter of a circle: ")
    radius =  float(input("Radius: "))
    perimeter = calculate_perimeter(radius)
    print('Perimeter: {0:0.2f} meters'.format(perimeter), end='')

if __name__ == "__main__":
    main()