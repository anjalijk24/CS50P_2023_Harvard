#Assignment:implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the 
#greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s 
#greeting, and treat the user’s greeting case-insensitively.

Greeting = input("Greeting: ").strip().casefold()

prefix = Greeting.split(', ')

if Greeting=="hello" or prefix[0]=="hello":
   print("$0")
elif Greeting[0]=="h" and prefix[0]!="hello":
    print("$20")
else:
    print("$100")

