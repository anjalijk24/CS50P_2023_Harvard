#Assignment: implement a program that:

    #Expects zero or two command-line arguments:
        #Zero if the user would like to output text in a random font.
        #Two if the user would like to output text in a specific font, in which case the first of the -
        #two should be -f or --font, and the second of the two should be the name of the font.

    #Prompts the user for a str of text.
    #Outputs that text in the desired font.

#If the user provides two command-line arguments and the first is not -f or --font or the second is not the
#name of a font, the program should exit via sys.exit with an error message.

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

def main():
    fontname = get_font(sys.argv)
    string = input("Input: ")
    print(figlet.renderText(string))


def get_font(arg):
    if len(arg) == 1:
        return random.choice(fonts)
    elif arg[1] == "-f" or arg[1] == "--font":
        if arg[2] in fonts:
            return figlet.setFont(font=arg[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")



if __name__ == "__main__":
    main()

