# LIST COMPREHENSION
"""
Make a list of numbers which are divisible by 3 in a range
without using big chunk of code
lets do it in one line using list comprehension
"""
    # Big Chunk Of code:
'''
ls = []
for i in range(10):
    if i%3 ==0:
        ls.append(i)
print("Big code (List)",ls)
'''
    # One line using List Comprihensions
'''
ls = [i for i in range(10) if i%3 ==0]
print ("One Liner (List)",ls)
'''

#Dictioner Comprihensions
"""
What do we need:  { 0:"item0", 1:"item1".....100:"item100"}
Why do we need: Scalability; we can do with any number
"""
    #Without any condition
'''
dict1 = {i:f"Item {i}" for i in range(1,11)}
print(dict1)
'''
    #With Condition
'''
dict1 = {i:f"Item {i}" for i in range(1,11) if i%3==0}
print(dict1)
'''

    #How to reverse Key value pair
'''
dict1 = {i: f"Item {i}" for i in range(1, 6)}
dict2 = {value: key for key,  value in dict1.items()}
print(dict1)
print(dict2)
'''

#Set Comprihensions

"""
One liner for set compihensions
use { } 
"""

'''
set_ex = {ex1 for ex1 in [1,2,3,4,3,3,3,2,2,23,4,4,5,6,7,8]}
print(set_ex)
print(type(set_ex))
'''
#Genrators Comprihensions
"""
Functions which yield a value on fly 

use ()
"""
"""
evens = (i for i in range(100) if i%2 ==0)
for items in evens:
    print(items)
print(evens.__next__())
print(evens.__next__())
print(type(evens))
"""