# Pattern Printing
# Input =  int n
# Boolean  = input 1 or zero bollean true or false
# if true
"""
*
**
***
****
"""
# if false
"""
****
***
**
*
"""
print("Print a Pattern with Stars '*'")
print("Press 1 if you want a sequential pattern")
print("Press 0 if you want a reverse sequential pattern")
B_input = int(input("Enter your choice:  "))
boool = bool(B_input)
user_input = int(input("How many star rows you want to see: "))
if boool == True:
# Approch 1
    for i in range(1, user_input + 1):
        for j in range(1, i + 1):
            print('*', end="")
        print()
elif boool == False:

    for i in range(user_input, 0, -1):
        for j in range(1, i + 1):
            print('*', end="")
        print()
# Approch 2
"""
for i in range(1,user_input+1):
     print('*' *i) 
"""

