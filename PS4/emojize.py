#Assignment:  implement a program that prompts the user for a str in English and then outputs the “emojized”
#version of that str, converting any codes (or aliases) therein to their corresponding emoji.

from emoji import emojize

def main():
    str = input("Input: ")
    print("Output:", get_emoji(str))


def get_emoji(s):
    return emojize(s, language = 'alias')


if __name__ == "__main__":
    main()
