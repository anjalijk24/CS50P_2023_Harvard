# Assignment: implement a program that:

# Prompts the user for a level, n. If the user does not input 1, 2, or 3, the program should prompt again.
# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative
# integer with n digits. No need to support operations other than addition (+).
# Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the
# program should output EEE and prompt the user again, allowing the user up to three tries in total for that
# problem. If the user has still not answered correctly after three tries, the program should output the
# correct answer.
# The program should ultimately output the user’s score: the number of correct answers out of 10.


import random

LEVELS = {
    1: (0, 9),
    2: (10, 99),
    3: (100, 999)
}

def main():
    # main function for the calculator
    level = get_level("Level: ")
    score = generate_integer(level)
    print(f"Score: {score}")


def get_level(prompt):
    #prompt the user to select a level between 1 & 3
    while True:
        try:
            n = int(input(prompt))
            if n in LEVELS:
                return n
        except ValueError:
            pass         # Reprompt the user


def generate_integer(l):
    lower_limit, upper_limit = LEVELS[l]
    score = 0

    for _ in range(10):
        x = random.randint(lower_limit, upper_limit)
        y = random.randint(lower_limit, upper_limit)
        count = 0

        while count < 3:
            result = input(f"{x} + {y} = ")

            try:
                result = int(result)
                if result == x + y:
                    score += 1
                    break
                else:
                    count += 1
                    print("EEE")
                    if count == 3:
                        print(f'{x} + {y} = {x + y}')
                        break
            except ValueError:
                count += 1
                print("EEE")

    return score


if __name__ == "__main__":
    main()
