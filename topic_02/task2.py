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

if op == '+':
    print(add(a, b))
elif op == '-':
    print(subtract(a, b))
elif op == '*':
    print(multiply(a, b))
elif op == '/':
    print(divide(a, b))
else:
    print("Invalid operator")
