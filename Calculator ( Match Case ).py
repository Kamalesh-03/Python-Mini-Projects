a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

match operator:
    case "+":
        print("Answer:", a + b)
    case "-":
        print("Answer:", a - b)
    case "*":
        print("Answer:", a * b)
    case "/":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Answer:", a / b)
    case _:
        print("Invalid operator")
