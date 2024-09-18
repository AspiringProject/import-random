def add():
    answer = num1 + num2
    print(num1, "+", num2, "=", answer)

def sub():
    answer = num1 - num2
    print(num1, "-", num2, "=", answer)

def multiply():
    answer = num1 * num2
    print(num1, "*", num2, "=", answer)

def divide():
    if num2 != 0:
        answer = num1 / num2
        print(num1, "/", num2, "=", answer)
    else:
        print("Cannot divide by zero")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

calcType = input("Enter operation (add, sub, multiply, divide): ")

if calcType.lower() == 'add':
    add()
elif calcType.lower() == 'sub':
    sub()
elif calcType.lower() == 'multiply':
    multiply()
elif calcType.lower() == 'divide':
    divide()
else:
    print("Invalid operation")