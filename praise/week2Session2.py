def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def is_even(number):
    return number % 2 == 0

def calculator():
    num1 = int(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = int(input("Enter second number: "))

    if op == "+":
        return add(num1, num2)
    elif op == "-":
        return subtract(num1, num2)
    elif op == "*":
        return multiply(num1, num2)
    elif op == "/":
        return divide(num1, num2)
    else:
        return "Invalid operation"

print(calculator())