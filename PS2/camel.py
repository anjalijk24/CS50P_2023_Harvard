#Assignment: implement a program that prompts the user for the name
#of a variable in camel case and outputs the corresponding name in
#snake case. Assume that the user’s input will indeed be in camel case.
def main():
  #enter a string in camel case
  string = input("camelCase: ")

  #check each letter and find out the position
  #of capslock letters, put "_" right before it,
  #and convert it into lower case
  new_string = ""
  for l in range(len(string)):
    if string[l].isupper():
      new_string = new_string + "_" + string[l].lower()
    else:
       new_string = new_string + string[l]

  print("snake_case: ", new_string)


main()

