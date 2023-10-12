#Assignment:implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the
#equivalent number of Joules as an integer. Assume that the user will input an integer.

#mass in kg, c in m/s
m, c = int(input("m: ")), 300000000

#energy in Joules
print("E: ", m*pow(c,2))