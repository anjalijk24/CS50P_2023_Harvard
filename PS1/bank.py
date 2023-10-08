Greeting = input("Greeting: ").strip().casefold()

prefix = Greeting.split(', ')

if Greeting=="hello" or prefix[0]=="hello":
   print("$0")
elif Greeting[0]=="h" and prefix[0]!="hello":
    print("$20")
else:
    print("$100")

