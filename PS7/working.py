#Assignment: implement a function called convert that expects a str in either of the 12-hour formats below and returns the
#corresponding str in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be capitalized (with no periods therein)
#and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM
#and 5:00 PM specifically.

    #9:00 AM to 5:00 PM
    #9 AM to 5 PM

#Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid
#(e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem;
#someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).


import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(\d+):?(\d+)? (AM|PM) to (\d+):?(\d+)? (AM|PM)$", s)

    if match:
        start_hour, end_hour = map(int, [match.group(1), match.group(4)])


        if match.group(3) == "PM" and start_hour != 12:
            start_hour += 12
        elif match.group(3) == "PM" and start_hour == 12:
            start_hour = start_hour


        if match.group(6) == "PM" and end_hour != 12:
            end_hour += 12
        elif match.group(6) == "PM" and end_hour == 12:
            end_hour = end_hour


        if match.group(2) is not None and int(match.group(2)) < 60:
            start_min = int(match.group(2))
        elif match.group(2) is not None and int(match.group(2)) >= 60:
            raise ValueError
        else:
            start_min = 0

        if match.group(5) is not None and int(match.group(5)) < 60:
            end_min = int(match.group(5))
        elif match.group(5) is not None and int(match.group(5)) >= 60:
            raise ValueError
        else:
            end_min = 0


        if match.group(3) == "AM" and start_hour == 12:
            start_hour = 0

        if match.group(6) == "AM" and end_hour == 12:
            end_hour = 0


        if 0 <= start_hour <= 23 and 0 <= end_hour <= 23:
            return f"{start_hour:02}:{start_min:02} to {end_hour:02}:{end_min:02}"
        else:
            raise ValueError
    else:
        raise ValueError



if __name__ == "__main__":
    main()
