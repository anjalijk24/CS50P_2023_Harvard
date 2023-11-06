#Assignment: implement a program that prompts the user for names, one per line, until the user inputs control-d.
#Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one
#and, three names with two commas and one and, and n names with n-1 commas and one and, as in the below:

    #Adieu, adieu, to Liesl
    #Adieu, adieu, to Liesl and Friedrich
    #Adieu, adieu, to Liesl, Friedrich, and Louisa
    #Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
    #Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
    #Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
    #Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl


import inflect

p = inflect.engine()

def main():
    name = get_names("Name: ")
    print(f"Adieu, adieu, to {p.join(name)}")


def get_names(prompt):
    names = []
    while True:
        try:
            tmp = input(prompt)
            names.append(tmp)
        except EOFError:
            break

    print("\n")
    return names


if __name__ == "__main__":
     main()


