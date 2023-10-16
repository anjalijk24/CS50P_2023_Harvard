#Assignment:implement a program that prompts the user for a str of text and then outputs that same text but with
#all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

string = input("Input: ")
newstring = ""
for s in range(len(string)):
    ss = string[s].casefold()
    match ss:
        case "a" | "e" | "i" | "o" | "u":
            newstring = newstring
        case _:
            newstring = newstring + string[s]


print("Output:", newstring)