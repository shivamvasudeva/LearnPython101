"""a = 6
b = 56
c = int(input("Enter Value: "))
if c > b:
    print(f'c = {c} is greater than b = {b}')
elif c == b:
    print ("C === B ")
else:
    print(f'b = {b} is greater than c = {c}')

list1 = [5,4,5,6,7,8]
if 5 in list1:
    print("yesss")
list1 = [5,4,5,6,7,8]
if 15 not in list1:
    print("NOoooooooooooooooooo")"""

age_of_person = int(input("Enter your age: "))
if age_of_person > 18:
    print("Yes you can drive")
elif age_of_person == 18:
    print("Not sure, Come to Center")
else:
    print("Dont You Dare to Drive")