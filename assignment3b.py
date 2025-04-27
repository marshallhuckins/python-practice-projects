#Marshall Huckins 01.09.2021

def display_menu():
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print()

def choice():
    choice = float(input("Please enter a menu option: "))

def add( number1, number2):
    results = number1 + number2
    return results

def sub( number1, number2):
    results = number1 - number2
    return results

def mult( number1, number2):
    results = number1 * number2
    return results

def div( number1, number2):
    results = number1 / number2
    return results

def main():
    display_menu()
    repeat = "y"
    while repeat.lower() == "y":
        number1 = int(input("Please enter your first number: "))
        number2 = int(input("please enter your second number: "))
        if choice == 1:
            print(add(number1, number2))
            repeat = input("Again? (y/n): ")
        elif choice == 2:
            print(sub(number1, number2))
            repeat = input("Again? (y/n): ")
        elif choice == 3:
            print(mult(number1, number2))
            repeat = input("Again? (y/n): ")
        elif choice == 4:
            print(div(number1, number2))
            repeat = input("Again? (y/n): ")
        else:
            print("Please enter a valid menu option.")
            repeat = input("Again? (y/n): ")
    print("Bye!")

if __name__ == "__main__":
    main()
            
        
    
