#Assignment:  implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X
#and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in
#the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
#And if 99% or more remains, output F instead to indicate that the tank is essentially full.

def main():
    fuel = get_fuel_value("Fraction: ")
    if fuel <= 1:
        print("E")
    elif fuel >= 90:
        print("F")
    else:
         print(f"{int(fuel)}%")


def get_fuel_value(prompt):
    while True:
        try:
            x, y = input(prompt).split('/')
            x, y = int(x), int(y)
            if x <= y:
                return round(x / y * 100)
            else:
                pass
        except(ValueError, ZeroDivisionError):
            pass


main()