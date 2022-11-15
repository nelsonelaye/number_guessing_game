import math
import random

'''
Number guessing game
'''

random_number = math.ceil((50 * random.random()))
name = input("What is your name? ")
guessed_number = input("Welcome, {}. I'm thinking of a magic number. Can you guess it? ".format(name))


# call function when user input a valid guess value or after an already handled error
def call_prompt(guessed):

    while guessed != random_number:

        if guessed < random_number:
            print("magic number is greater than {}".format(guessed))
            guessed = int(input("Guess again: "))

        elif guessed > random_number:
            print("magic number is lesser than {}".format(guessed))
            guessed = int(input("Guess again: "))

    print("Congratulations, {}. You won!!!".format(name))


# check if user input a valid guess value
def check_val():
    if len(guessed_number) <= 0:
        raise ValueError("Invalid input. Value must be a number")


# Exception handler for the entire game
try:
    check_val()
    guessed_number = int(guessed_number)

except ValueError as err:
    print(err)
    guessed_number = int(input("Guess again: "))
    call_prompt(guessed_number)

else:
    call_prompt(guessed_number)
