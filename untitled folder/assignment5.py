#Marshall Huckins 01.18.2021

with open("grocery_list.txt", "w") as outfile:
    outfile.write("")

def write_groceries(groceries):
    with open("grocery_list.txt", "w") as file:
        for grocery in groceries:
            file.write(grocery +"\n")

def read_groceries():
    groceries = []
    with open("grocery_list.txt") as file:
        for line in file:
            line = line.replace("\n", " ")
            groceries.append(line)
    return groceries

def list_groceries(groceries):
    for i in range(len(groceries)):
        grocery = groceries[i]
        print(str(i+1) + ". " + grocery)
    print()

def add_grocery(groceries):
    grocery = input("Grocery item: ")
    groceries.append(grocery)
    write_groceries(groceries)
    print(grocery + " was added.\n")

def delete_grocery(groceries):
    index = int(input("Number: "))
    grocery = groceries.pop(index - 1)
    write_groceries(groceries)
    print(grocery + " was deleted.\n")

def display_menu():
    print("Create a Grocery List")
    print()
    print("Command Menu")
    print("list - List all groceries")
    print("add - Add a grocery item")
    print("del - Delete a grocery item")
    print("exit - Exit program")

def main():
    display_menu()
    groceries = read_groceries()
    while True:
        command = input("Command: ")
        if command == "list":
            list_groceries(groceries)
        elif command == "add":
            add_grocery(groceries)
        elif command == "del":
            delete_grocery(groceries)
        elif command == "exit":
            print("Goodbye!")
            break
        else:
            print("Not a valid option. Please try again.")

if __name__ == "__main__":
    main()
