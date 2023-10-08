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
