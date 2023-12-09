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
    sum_of_squares = side_a**2 + side_b**2
    hypotenuse = math.sqrt(sum_of_squares)
    # Returning the hypotenuse to the function.
    return hypotenuse


# Declaring function to calculate the perimeter.
def calculate_perimeter(side_a, side_b):
    # Calling the calculated hypotenuse from its function to use it for calculating the perimeter.
    hypotenuse = calculate_hypotenuse(side_a, side_b)
    # Calculating the perimeter.
    perimeter = side_a + side_b + hypotenuse
    # Returning the perimeter to the function.
    return perimeter


# Declaring main() function to get user input/output, catch invalid inputs and loop.
def main():
    # Explaining my program to the user.
    print(
        "Welcome to my right triangle program in python. My program will calculate the hypotenuse of any right triangle using Pythagorean Theorem and can additionally calculate its perimeter. It uses a loop to allow for my program to be run again."
    )
    while True:
        # Getting user input for the 2 sides (A & B) only once.
        side_a = input("Enter the length of side A (cm): ")
        side_b = input("Enter the length of side B (cm): ")

        # Loop main() function.
        # Using a try catch to catch any errors.
        try:
            # Converting user input to a float.
            side_a_as_float = float(side_a)
            side_b_as_float = float(side_b)

            # Calculating hypotenuse and perimeter.
            hypotenuse = calculate_hypotenuse(side_a_as_float, side_b_as_float)
            perimeter = calculate_perimeter(side_a_as_float, side_b_as_float)

            # Displaying the hypotenuse and perimeter to the user.
            print("The hypotenuse is {:.2F}".format(hypotenuse))
            print("The perimeter is {:.2F}".format(perimeter))

            # Using a second try catch to catch any errors for inputs regarding if they would like to run my program again.
            try:
                # Asking the user if they want to run the program again.
                user_input = input(
                    "Do you want to run the program again? (1 - Yes or 2 - No): "
                )

                # Converting user input as a string to an integer.
                user_input_as_integer = int(user_input)

                # If the user input is not equal to 1, break out of the loop.
                if user_input_as_integer != 1:
                    break

            # Catching invalid inputs regarding running my program again.
            except:
                print(
                    "Invalid input. Please enter 1 to run my program again or 2 to stop my program."
                )
                break
        # Catching invalid inputs for side lengths.
        except:
            print("Invalid input for sides. Please try again.")


if __name__ == "__main__":
    main()
