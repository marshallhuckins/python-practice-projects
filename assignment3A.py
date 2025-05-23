#Marshall Huckins 01.09.2021

def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit






import temperature as temp

def display_menu():
    print("Menu")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print()

def convert_temp():
    option = int(input("Enter a menu option: "))
    if option == 1:
        f = int(input("Enter degrees Fahrenheit: "))
        c = temp.to_celsius(f)
        c = round(c, 2)
        print("Degrees Celsius:", c)
    elif option == 2:
        c = int(input("Enter degrees Celsius: "))
        f = temp.to_fahrenheit(c)
        f = round(f, 2)
        print("Degrees Fahrenheit:", f)
    else:
        print("You must enter a valid menu number.")

def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Convert another temperature? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()
