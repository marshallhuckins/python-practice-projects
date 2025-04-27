#Marshall Huckins 12.16.2020


value1 = 0
value2 = 0
answer = 0
math = "?"

math = input ( "Enter 1 for addition, 2 for subtraction, 3 for multiplication, or 4 for division: ")
value1 += float (input( "Enter your first value: "))
value2 += float (input( "Enter your second value: "))

while( math != "Q" ):
  if (math == "1"):
    answer = (value1 + value2)
    print(answer)
    
      
  elif (math == "2"):
    answer = (value1 - value2)
    print(answer)

  elif (math == "3"):
    answer = (value1 * value2)
    print(answer)
    
  elif (math == "4"):
    answer = (value1 / value2)
    print(answer)

  else:
      print("Please enter a value 1-4")

 

  
