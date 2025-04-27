#Marshall Huckins 01.09.2021

def append( name, course ):
    results = name + " " + course
    return results

def positiveNumber( number ):
    if number <= 0:
      return 0
    else:
      return number

def evenOdd ( number ):
    if (number % 2) == 0:
        return ("Number is even. ")
    else:
        return ("Number is odd. ")

def inCenturyRange ( number ):
    if number >= 0 and number <= 100:
        return ("Number is between 0 and 100.")
    else:
        return ("Number is not between 0 and 100.")

def repeater( stringNumber, word ):
    answer = word * stringNumber
    return answer    

def main():
    name = input("Enter name: ")
    course = input("Enter course: ")

    print( append ( name, course ) )

    number = float ( input("Enter a number: "))
    print(positiveNumber (number))
    print(evenOdd (number))
    print(inCenturyRange (number))

    stringNumber = int(input("Enter a number to concatenate your word: "))
    word = input("Enter your string: ")
    print( repeater (stringNumber, word))
    
main()
