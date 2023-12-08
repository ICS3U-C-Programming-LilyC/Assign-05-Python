#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Dec/8/2023
# This program gets 2 sides of a right angle triangle and calculates the hypotenuse.
# It uses a While True loop to run my program again.

# Importing math module to allow for calculations to be done.
import math


# Declaring function to calculate the hypotenuse.
def calculate_hypotenuse(side_a, side_b):
    # Calculating the hypotenuse.
    hypotenuse = math.sqrt(side_a**2 + side_b**2)
    # Returning the hypotenuse to the function.
    return hypotenuse

# Declaring function to calculate the perimeter.
def calculate_perimeter(side_a, side_b):
    # Calling the calculated hypotenuse from it's function to use it for calculating the perimeter.
    hypotenuse = calculate_hypotenuse(side_a, side_b)
    # Calculating the perimeter.
    perimeter = side_a + side_b + hypotenuse
    # Returning the perimeter to the function.
    return perimeter

# Declaring main() function to get user input/output and catching invalid inputs.
def main():
    # Getting user input for the 2 sides (A & B).
    side_a = float(input("Enter the length of side A (cm): "))
    side_b = float(input("Enter the length of side B (cm): "))

    # Using a try catch to catch any erroneous inputs.
    try:
        side_a_as_float = float(side_a)
        side_b_as_float = float(side_b)
        # Checking if the input is greater than 0.
        if side_a_as_float > 0 and side_b_as_float > 0:
            # Calling functions to display hypotenuse and perimeter.
            hypotenuse = calculate_hypotenuse(side_a_as_float, side_b_as_float)
            perimeter = calculate_perimeter(side_a_as_float, side_b_as_float)
            # Displaying the hypotenuse and perimeter to the user.
            print("The hypotenuse is {:.2F}".format(hypotenuse))
            print("The perimeter is {:.2F}".format(perimeter))

        # Else the input is not greater than 0.
        else:
            print("Please enter a number greater than 0.")

    # Catching any errors.
    except:
        print("Invalid input.")

# Using a while true loop to ask the user if they want to run my program again.
while True:
    main()
    if input("Do you want to run my program again? (1 - Yes or 2 - No): ") != "1":
        break

if __name__ == "__main__":
    main()