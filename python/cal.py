import math

# Define calculator functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

while True:
    print("*" * 30)
    print("Welcome to My Calculator".center(30))
    print("Select an Option\n1. Add\n2. Sub\n3. Mul\n4. Div\n5. Sqrt")
    print("*" * 30)
    
    choice = int(input("Enter your choice: "))

    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    elif choice == 5:
        num1 = float(input("Enter number to find square root: "))
    else:
        print("Invalid choice! Please select from 1–5.")
        continue

    if choice == 1:
        print(f"Sum of {num1} and {num2} = {add(num1, num2)}")
    elif choice == 2:
        print(f"Difference of {num1} and {num2} = {sub(num1, num2)}")
    elif choice == 3:
        print(f"Product of {num1} and {num2} = {mul(num1, num2)}")
    elif choice == 4:
        print(f"Division of {num1} by {num2} = {div(num1, num2)}")
    elif choice == 5:
        print(f"Square root of {num1} = {math.sqrt(num1)}")

    x = int(input("Do you want to exit? Press 0 to exit, 1 to continue: "))
    if x == 0:
        print("Thank you for using My Calculator!")
        break
