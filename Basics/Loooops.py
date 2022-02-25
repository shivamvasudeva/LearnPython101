'''
l1 = [[1, 2], [3, 4], [5, 6], [7, 8]]
dict1 = dict(l1)
for item in dict1:
    print(item)

for items, num1 in dict1.items():
    print(items, num1)'''
#Quiz
list_q =[1,2,3,'six',30,20, 'seven']
for i in list_q:
    if str(i).isnumeric() and i > 6:
        print(i)
