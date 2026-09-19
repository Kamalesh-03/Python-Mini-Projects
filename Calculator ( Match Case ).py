a = int(input("Enter first number: "))
b = int(input("Enter first number: "))

operator = input("Enter opeator (+,-,*,/): ")

match operator:
    case "+":
        print("Answer:", a+b)

    case "-":
        print("Answer:", a-b)

    case "*":
        print("Answer", a*b)

    case "/":
        print("Answer", a/b)

    case _:
        print("Invalid Answer")