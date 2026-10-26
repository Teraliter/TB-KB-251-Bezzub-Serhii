import operations

while True:
    cmd = operations.get_operator()
    if cmd.lower() == "exit":
        break

    if cmd not in operations.operations:
        print("Invalid operator")
        continue

    a = operations.get_number("Enter first number: ")
    b = operations.get_number("Enter second number: ")
    print("Result:", operations.calculate(cmd, a, b))
