#Assignment: implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the
#amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the
#user will only input integers, and ignore any integer that isn’t an accepted denomination.

print("Amount Due: 50")
tmp = 0
while True:
    money = int(input("Insert Coin: "))
    if money == 50 or money == 25 or money == 10 or money == 5:
        money = money + tmp
        if money - 50 >= 0:
            print("Change Owed:", money - 50)
            break
        elif 0 < 50 - money < 50:
            print("Amount Due:", 50 - money)
            tmp = money
    else:
        print("Amount Due:",50)


