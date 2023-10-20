#implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a
#common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted
#alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to
#pluralize the items. Treat the user’s input case-insensitively.

def main():
    list_grocery = get_list("")
    sorted_list = sorted(list_grocery.items())

    for key, value in sorted_list:
        print(value, key)


def get_list(prompt):
     grocery_list = {}
     while True:
         try:
            item = input(prompt).upper()
            if item in grocery_list:
                grocery_list[item] +=  1
            else:
                grocery_list[item] = 1
         except EOFError:
             break

     print('\n')
     return grocery_list



if __name__ == "__main__":
    main()

