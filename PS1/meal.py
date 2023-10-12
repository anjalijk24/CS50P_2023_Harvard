#Assignment: implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner
#time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time 
#as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or
#anytime in between, it’s time for breakfast.

def main():
  time = input("What time is it? ")

  time = convert(time)

  if 7.0 <= time <= 8.0:
    print("breakfast time")
  elif 12.0 <= time <= 13.0:
    print("lunch time")
  elif 18.0 <= time <= 19.0:
    print("dinner time")

def convert(t):
    if t.endswith("a.m."):
        t = t.removesuffix("a.m.")
    elif t.endswith("p.m."):
        t = (t.removesuffix("p.m.").split(":"))[0]
        t = str(float(t) + 12.0)

    hours, minutes = t.split(":")
    hours, minutes = float(hours), float(minutes)/60.
    return hours + minutes


if __name__ == "__main__":
    main()
