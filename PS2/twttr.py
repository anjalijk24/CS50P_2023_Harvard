#Assignment:implement a program that prompts the user for a str of text and then outputs that same text but with
#all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.


def main():
    string = input("Input: ")
    string_new = shorten(string)
    print(string_new)


def shorten(word):
    newstring = ""
    for s in range(len(word)):
        ss = word[s].casefold()
        match ss:
              case "a" | "e" | "i" | "o" | "u":
                 newstring = newstring
              case _:
                newstring += word[s]

    return newstring


if __name__ == "__main__":
    main()
