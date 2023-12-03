#Assignment: implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
#and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify
#exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does
#not exist, the program should instead exit via sys.exit.

#Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be
#considered a comment.) Assume that any line that only contains whitespace is blank.


import sys

def main():
    number_lines = check_file(sys.argv)
    print(number_lines)


def check_file(f):
    if len(f) == 1:
        sys.exit("Too few command-line arguments")
    elif len(f) > 2:
        sys.exit("Too many command-line arguments")
    elif not f[1].endswith(".py"):
         sys.exit("Not a Python file")


    filename = f[1]
    count = 0

    try:
        with open(filename) as file:
            for line in file:
                line  = line.lstrip(" ")
                if not line.startswith("#") and not line.isspace():
                    count += 1
        return count
    except FileNotFoundError:
       sys.exit("Not a Python file")


if __name__ == "__main__":
    main()

