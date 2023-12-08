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
    # Getting user using a while True loop for the sides (A & B).
    while True:
        # Using a try catch to catch erroneous data.
        try:
            # Converting user input from strings to floats.
            side_a = float(input("Enter the length of side A (cm): "))
            side_b = float(input("Enter the length of side B (cm): "))

            # If statement to check if the inputs are greater than or equal to 0.
            if side_a >= 0 and side_b >= 0:
                # If they're less than 0 or equal to 0, then break out of the loop.
                break
            # Else their input is less than or equal to 0.
            else:
                print("Please enter a number greater than 0.")

        # Catching any errors.
        except:
            print("Invalid input. Please enter a valid number.")

    # Calling functions to display hypotenuse and perimeter.
    hypotenuse = calculate_hypotenuse(side_a, side_b)
    perimeter = calculate_perimeter(side_a, side_b)

    # Displaying the hypotenuse and perimeter to the user.
    print("The hypotenuse is {:.2F}".format(hypotenuse))
    print("The perimeter is {:.2F}".format(perimeter))


# Declaring a function for the loop.
def run_program():
    # Using a while loop to ask the user if they want to run the program again.
    while True:
        # Loop main() function.
        main()
        # Asking user if they want to run my program again.
        user_input = input("Do you want to run the program again? (1 -Yes or 2 - No): ")
        # If the user input does not equal 1 then break out of the loop.
        if user_input != "1":
            break

# Calling the run_program() function to execute the loop.
run_program()


if __name__ == "__main__":
    main()
