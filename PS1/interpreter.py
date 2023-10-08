expression = input("Expression: ")

x, y, z = expression.split(" ")

x, z = float(x), float(z)

match y:
    case "+":
        print(round(x + z, 1))
    case "-":
        print(round(x - z, 1))
    case "/":
        print(round(x / z, 1))
    case "*":
        print(round(x * z, 1))