#Assignment: implement a program that:

    #Prompts the user for a level, n.If the user does not input a positive integer, the program should prompt again.
    #Randomly generates an integer between 1 and n, inclusive, using the random module.
    #Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the
    #user again.
       #If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
       #If the guess is larger than that integer, the program should output Too large! and prompt the user again.
       #If the guess is the same as that integer, the program should output Just right! and exit.


import random

def main():
    # Get the game level from the user
    level = get_level('Level: ')
    guess = get_guess(level)


def get_level(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            else:
                pass # Reprompt the user
        except ValueError:
            pass     # Reprompt the user


def get_guess(n):
    number = random.randint(1, n)
    while True:
        try:
            guess = int(input('Guess: '))

            if guess <= 0:
                pass    # Reprompt the user
            elif guess < number:
                print('Too small!')
                pass    # Reprompt the user
            elif guess > number:
                print('Too large!')
                pass    # Reprompt the user
            elif guess == number:
                print('Just right!')
                break   # Exit from code
        except ValueError:
            pass


if __name__ == '__main__':
    main()
