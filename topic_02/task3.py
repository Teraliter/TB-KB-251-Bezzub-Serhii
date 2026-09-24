def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case '+':
        print(add(a, b))
    case '-':
        print(subtract(a, b))
    case '*':
        print(multiply(a, b))
    case '/':
        print(divide(a, b))
    case _:
        print("Invalid operator")
