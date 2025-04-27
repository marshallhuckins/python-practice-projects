workdayList = [ "M", "TH" ]
vacation = [ "TU", "S" ]
validDays = [ "M", "TU", "W", "TH", "F", "S" ]
day = "?"
while( day != "Q"):

    day = input ( "Enter a day (M, TU, W, TH, F, or S) Q-Quits" )

    if ( day in validDays ):
        print("Hi")

    if ( day == "W" ):
        print("Metro")
        print("INFO 1003")
    elif ( day == "F" ):
        print("IWCC")
        print("CSC 101")
    elif ( day in workdayList ):
        print("It is Workday")
        if( day == "M"):
            print("Time for Shopping")
        else:
            print("Time for Lunch at Sonic")
    elif ( day in vacation ):
        print ("Yay! No Class")
