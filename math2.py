value1 = 0
value2 = 0
validAnswer = [ "1", "2", "3", "4",]
math = "?"



while( math != "Q"):

    math = input ("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division or Q to quit: ")
    value1 += float (input("Enter your first value: "))
    value2 += float (input("Enter your second value: "))


    if ( math in validAnswer):
        print()

    if ( math == "1" ):
        print(value1 + value2)

    elif ( math == "2" ):
        print(value1 - value2)

    elif ( math == "3" ):
        print(value1 * value2)

    elif ( math == "4" ):
        print(value1 / value2)

    else:
        print("Please enter a valid value.")
