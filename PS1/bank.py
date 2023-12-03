#Assignment: implement a program that prompts the user for a greeting. If the greeting starts with “hello”,
#output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100.
#Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

def main():
    greet = input("Greeting: ").strip()
    output = value(greet)
    print(f"${output}")


def value(greeting):
    words = greeting.casefold().split()
    if words[0].strip(",") == "hello":
        return 0
    elif words[0][0] == "h" and words[0] != "hello":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
