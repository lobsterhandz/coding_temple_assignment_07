def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y
    
    
def get_user_input():
    operation = input("Do you want to add, subtract, multiply, or divide? Enter '+', '-', '*', or '/': ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return operation, num1, num2
