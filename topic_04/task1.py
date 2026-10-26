def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, try again")

while True:
    try:
        cmd = input("Enter operator (+, -, *, /) or 'exit' to quit: ")
        if cmd.lower() == "exit":
            break
        operation = operations[cmd]
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")
        print("Result:", operation(a, b))
    except KeyError:
        print("Invalid operator")
    except (KeyboardInterrupt, EOFError):
        print("`nExit")
        break