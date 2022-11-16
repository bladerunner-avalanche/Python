def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def simple_calculator():
    print("Simple Calculator Program")
    print("")
    print("Select from the following options:")
    print("--------------------------------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("--------------------------------")
    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        print("You have selected Addition")
        print("Enter the first number: ")
        num1 = float(input())
        print("Enter the second number: ")
        num2 = float(input())
        print("The sum of the two numbers is: ", addition(num1, num2))
    elif choice == 2:
        print("You have selected Subtraction")
        print("Enter the first number: ")
        num1 = float(input())
        print("Enter the second number: ")
        num2 = float(input())
        print("The difference of the two numbers is: ", subtraction(num1, num2))
    elif choice == 3:
        print("You have selected Multiplication")
        print("Enter the first number: ")
        num1 = float(input())
        print("Enter the second number: ")
        num2 = float(input())
        print("The product of the two numbers is: ", multiplication(num1, num2))
    elif choice == 4:
        print("You have selected Division")
        print("Enter the first number: ")
        num1 = float(input())
        print("Enter the second number: ")
        num2 = float(input())
        print("The quotient of the two numbers is: ", division(num1, num2))
    elif choice == 5:
        print("You have selected Exit")
        exit()

    else:
        print("Invalid input, please try again")
        simple_calculator()

    print("Another one?")
    print("1. Yes")
    print("2. No")
    choice = int(input("Enter the number of your choice: "))
    if choice == 1:
        simple_calculator()
    elif choice == 2:
        exit()
    else:
        print("Invalid input, please try again")
        simple_calculator()

