#Assignment: implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how
#old they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from
#Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity,
#that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In
#other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. Use
#datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.


import re
import sys
import inflect
from datetime import date

p = inflect.engine()

def main():
    delta_time = get_time_in_minutes(input("Date of Birth: "))
    print(f"{convert_to_words(round(delta_time))} minutes")


def get_time_in_minutes(dob):
    match = re.match(r"\d{4}-\d{2}-\d{2}", dob)

    if match:
        dob_day     = date.fromisoformat(dob)
        current_day = date.today()
        delta = current_day - dob_day
        return delta.days * 24 * 60
    else:
        sys.exit("Invalid date")


def convert_to_words(number):
    return p.number_to_words(number, andword="").capitalize()


if __name__ == "__main__":
    main()
