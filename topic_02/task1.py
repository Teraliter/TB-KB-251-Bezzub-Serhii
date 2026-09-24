import math

def calc_discriminant(a, b, c):
    return b**2 - 4*a*c

def solve_quadratic(a, b, c):
    if a == 0:
        if b != 0:
            return -c / b
        return None

    d = calc_discriminant(a, b, c)

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        return -b / (2 * a)
    else:
        return None

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

res = solve_quadratic(a, b, c)
print("Result:", res)
