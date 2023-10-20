#Assignment: implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636
#or September 8, 1636. Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format,
#prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30,
#or 31 days.

def main():
    y, m, d = get_date("Date: ")
    print(f"{y}-{m:02}-{d:02}")


def get_date(prompt):
    month = [
         "January", "February", "March", "April", "May", "June",
         "July", "August", "September", "October", "November", "December"
         ]

    while True:
        try:
            value = input(prompt).title()
            if '/' in value:
                m, d, y = value.split('/')
                y, m, d = int(y), int(m), int(d)
                if d <= 31 and m <=12:
                    return y, m, d
            elif ',' in value:
                m, d, y = [i.strip(',') for i in value.split(' ')]
                if month.index(m) and int(d) <= 31:
                    y, m, d = int(y), int(month.index(m) + 1), int(d)
                    return y, m, d
        except (EOFError, ValueError):
            pass



if __name__ == "__main__":
    main()

