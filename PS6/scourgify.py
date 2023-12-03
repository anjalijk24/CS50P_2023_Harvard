#Assignment: implement a program that:

    #Expects the user to provide two command-line arguments:
        #the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
        #name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
    #Converts that input to that output, splitting each name into a first name and last name. Assume that each student will
    #have both a first name and last name.

#If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via
#sys.exit with an error message.


import sys
import csv


def main():
    file1, file2 = check_arg(sys.argv)
    new_file = make_newfile(file1, file2)


def check_arg(v):
    if len(v) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(v) > 3:
        sys.exit("Too many command-line arguments")
    return v[1], v[2]


def make_newfile(f1, f2):
    student_info = []

    try:
        with open(f1) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                student_info.append({"first": first, "last": last, "house": row["house"]})

        with open(f2, "w") as file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_info)

    except PermissionError:
       sys.exit(f"Could not read {f1}")

    return f2


if __name__ == "__main__":
    main()
