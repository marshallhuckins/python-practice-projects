my_num = input("Enter a number between 1 and 999:")
check_num = int(my_num)
while check_num <= 0 and check_num != 1000:
    my_num = input("Try again. The number must be between 1 and 999")
    check_num = int(my_num)
