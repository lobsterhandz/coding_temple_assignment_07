def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Check for division by zero and handle it
    if y == 0:
        return "Error: Can't divide by zero!"
    return x / y

# Gather user input
num1 = float(input("Enter first number: "))
operation = input("Enter operation (e.g., '+', '-', '*', '/'): ")
num2 = float(input("Enter second number: "))

# Perform the chosen operation
if operation == '+':
    print("Result:", add(num1, num2))
elif operation == '-':
    print("Result:", subtract(num1, num2))
elif operation == '*':
    print("Result:", multiply(num1, num2))
elif operation == '/':
    result = divide(num1, num2)
    print("Result:", result)
else:
    print("Invalid operation selected.")
