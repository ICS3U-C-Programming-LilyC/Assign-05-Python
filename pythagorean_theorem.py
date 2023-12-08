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
    # Calling the calculated hypotenuse from it's function to use it for calculating the perimeter.
    hypotenuse = calculate_hypotenuse(side_a, side_b)
    # Calculating the perimeter.
    perimeter = side_a + side_b + hypotenuse
    # Returning the perimeter to the function.
    return perimeter


# Declaring main() function to get user input/output and catching invalid inputs.
def main():
    while True:
        # Getting user input for the 2 sides (A & B) only once.
        side_a = float(input("Enter the length of side A (cm): "))
        side_b = float(input("Enter the length of side B (cm): "))

        # Loop main() function.
        try:
            # Calculating hypotenuse and perimeter.
            hypotenuse = calculate_hypotenuse(side_a, side_b)
            perimeter = calculate_perimeter(side_a, side_b)

            # Displaying the hypotenuse and perimeter to the user.
            print("The hypotenuse is {:.2F}".format(hypotenuse))
            print("The perimeter is {:.2F}".format(perimeter))
            
            try:
                # Asking user if they want to run the program again.
                user_input = input("Do you want to run the program again? (1 - Yes or 2 - No): ")

                # Converting user input as a string to an integer.
                user_input_as_integer = int(user_input)

                # If the user input is not equal to 1, break out of the loop.
                if (user_input_as_integer != 1):
                    break

            # Catching invalid inputs.
            except:
                print("Invalid input. Please enter 1 to run my program again or 2 to stop my program.")
                break

        except:
            print("Invalid input for sides. Please try again.")

# Calling the main() function to execute the loop.
if __name__ == "__main__":
    main()
