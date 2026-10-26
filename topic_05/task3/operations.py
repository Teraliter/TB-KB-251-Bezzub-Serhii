import functions

operations = {
    "+": functions.add,
    "-": functions.subtract,
    "*": functions.multiply,
    "/": functions.divide,
}

def get_operator():
    return input("Enter operator (+, -, *, /) or 'exit' to quit: ")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, try again")

def calculate(op, a, b):
    return operations[op](a, b)
