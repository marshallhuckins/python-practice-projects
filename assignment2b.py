#Marshall Huckins 12.19.2020

totalPay = 0
employeePay = 0
employeeRate = 0
hoursWorked = "?"
replay = 0
total = 0

while (replay != "n" ):
  employeeRate = int(input("Enter employee's pay-rate (more than $9.25): "))

  hoursWorked = int(input("Enter hours worked this week: "))

  if hoursWorked <= 40:
    totalPay = (employeeRate * hoursWorked)
    total = totalPay + total
    print ("Employee's total pay: ", totalPay)
    replay = input("Do you wish to continue [y/n]: ")

  elif hoursWorked > 40:
      totalPay = (employeeRate * 40) + (hoursWorked - 40) * (employeeRate * 1.5)
      total = totalPay + total
      print ("Employee's total pay: ", totalPay)
      replay = input("Do you wish to continue [y/n]: ")
  else:
      print("Please enter a valid answer.")

print("The total pay for all employees is: ", total)
