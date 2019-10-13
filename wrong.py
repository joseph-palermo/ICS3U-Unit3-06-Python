#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: October 2019
# This program checks if the guessed number, imported by an RGN, is correct
# or incorrect


import random


def main():
    # This function asks the user to guess the number

    # variables
    correct_number = random.randint(0, 9)
    # input
    guess = int(input("Guess the number between 0 & 9 (integer): "))
    print("")

    # process
    try:
        guess = int(guess)
        if guess == correct_number:
            print("You correctly guessed the number!")
        else:
            print("Wrong number!")
            print("The correct number is: ", (correct_number))
    except Exception:
        print("Please insert an integer.")


if __name__ == "__main__":
    main()
