#Assignment: implement a program in Python that prompts the user for input and then outputs that same input, replacing each
#space with ... (i.e., three periods).

#enter input
string = input("Enter the input: ")

#replace space with 3 dots
string = string.replace(" ", "...")

#output the new string
print(string)