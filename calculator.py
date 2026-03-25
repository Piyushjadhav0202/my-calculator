def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("Calculator is running!")
print("3 x 4 =", multiply(3, 4))
print("10 / 2 =", divide(10, 2))
