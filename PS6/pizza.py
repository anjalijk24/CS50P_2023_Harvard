#Assignment:  implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in
#Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI at
#pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one
#command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist,
#the program should instead exit via sys.exit.

import sys
import csv
from tabulate import tabulate


def main():
    file = check_arg(sys.argv)
    menu = get_menu(file)
    print(tabulate(menu, headers="keys", tablefmt="grid"))


def check_arg(v):
    if len(v) == 1:
        sys.exit("Too few command-line arguments")
    elif len(v) > 2:
        sys.exit("Too many command-line arguments")
    elif not v[1].endswith(".csv"):
         sys.exit("Not a CSV file")

    return v[1]


def get_menu(f):
    menu = []

    try:
        with open(f) as file:
            reader = csv.DictReader(file)
            for row in reader:
                    menu.append(row)
    except FileNotFoundError:
       sys.exit("File does not exist")

    return menu


if __name__ == "__main__":
    main()


