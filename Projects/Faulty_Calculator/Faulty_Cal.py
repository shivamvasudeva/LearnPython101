a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
print ("Type 1 for Division")
print ("Type 2 for Multiply")
print ("Type 3 for Add")
print ("Type 4 for Sub")
User_input_operators= int(input("Enter Operator: "))
if a ==45 and b == 3 and User_input_operators == 2:
    print ("555")
elif a ==56 and b == 9 and User_input_operators == 3:
    print ("77")
elif a ==56 and b == 6 and User_input_operators == 1:
    print ("4")
else:
    if User_input_operators == 1:
        print("Division of 2 numbers will be",a/b)
    elif User_input_operators == 2:
        print("Multiplication of 2 numbers will be",a*b)
    elif User_input_operators == 3:
        print("Addition of 2 numbers will be",a+b)
    elif User_input_operators == 4:
        print("Subtraction of 2 numbers will be",a-b)
    else:
        print("Invalid Entry")
