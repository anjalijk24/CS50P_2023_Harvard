#Assignment: implement a function called validate that expects an IPv4 address as input as a str and then returns True or False,
#respectively, if that input is a valid IPv4 address or not. Structure numb3rs.py as follows, wherein you’re welcome to modify
#main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not
#required, to use re and/or sys.

#Either before or after you implement validate in numb3rs.py, additionally implement, in a file called test_numb3rs.py, two or
#more functions that collectively test your implementation of validate thoroughly, each of whose names should begin with test_.


import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Use a regex pattern to check for a valid IPv4 address format
    match = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)

    if match:
        first, second = int(match.groups()[0]), int(match.groups()[1])
        third, fourth = int(match.groups()[2]), int(match.groups()[3])
        if 0 <= first <= 255 and 0 <= second <= 255 and 0 <= third <= 255 and 0 <= fourth <= 255:
            return True
        else:
            return False
    else:
        return False



if __name__ == "__main__":
    main()
