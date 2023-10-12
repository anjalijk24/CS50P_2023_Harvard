#Assignment: implement a function called convert that accepts a str as input and returns that same input with any :) converted
#to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face).
#All other text should be returned unchanged.

def main():
    string = input("Enter the input: ")
    string = convert(string)
    print(string)

def convert(s):
    #replace emoticons with emojis and return the string
    s = s.replace(":)", "🙂").replace(":(", "🙁")
    return s

main()