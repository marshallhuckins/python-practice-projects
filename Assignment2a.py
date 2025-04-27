#Marshall Huckins 12.19.2020

print("Basic Calculator")
print()
print("================")

operation = 0
value1 = 0
value2 = 0

while (operation != "Q"):

    operation = input("Please enter + - * / to begin [Q to quit]: ")

    if (operation == "+"):
        value1 = float(input("Enter your first number: "))
        value2 = float(input("Enter your second number: "))
        print(value1 + value2)

    elif (operation == "-"):
        value1 = float(input("Enter your first number: "))
        value2 = float(input("Enter your second number: "))
        print(value1 - value2)

    elif (operation == "*"):
        value1 = float(input("Enter your first number: "))
        value2 = float(input("Enter your second number: "))
        print(value1 * value2)

    elif (operation == "/"):
        value1 = float(input("Enter your first number: "))
        value2 = float(input("Enter your second number: "))
        print(value1 / value2)

    elif (operation == "Q"):
        print("Goodbye")

    else:
        print("Please enter a valid option")
        
