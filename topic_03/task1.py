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

while True:
    cmd = input("Enter operator (+, -, *, /) or 'exit' to quit: ")
    if cmd.lower() == 'exit':
        break

    if cmd not in ('+', '-', '*', '/'):
        print("Invalid operator")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if cmd == '+':
        print("Result:", add(a, b))
    elif cmd == '-':
        print("Result:", subtract(a, b))
    elif cmd == '*':
        print("Result:", multiply(a, b))
    elif cmd == '/':
        print("Result:", divide(a, b))
