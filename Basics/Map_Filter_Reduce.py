#---------------------Map-------------------------------------------------

"""
if i have a list of numbers in str
convert a str into int without using for loop
function which will be applied to all the elements

First arg is the function name; second arg is the data

num1 = ["3","4","5"]
num1 = list(map(int,num1))
print(num1)


def sq(a):
    return a*a
square = list(map(sq,num1)) # Using FUnction
print(square)

square1 = list(map(lambda x:x*x,num1)) # Using Lambda
print(square1)

def sq(a):
    return a*a
def cube(a):
    return a*a*a
num = [3,4,5,6,7,8,9,9,9]
func = [sq,cube]
for i in range(10):
    val= tuple(map(lambda x:x(i),func)) #what is happening here?
     # lambda is taking a function x then asking ofor args in the same function x(i), func is taking a list of names of functions which will replace x and execute
    print(val)
   """
#--------------------Filter-------------------------------------
"""
makes a list of elements 
returns true
"""
"""

num = [3,4,5,6,7,8,9,9,2,10]
def great(num):
    return num >5
l3 = list(filter(great,num)) # Type cast into list or any datatipe for filter
print(l3)
"""

#-----------------------Reduce----------------------------------------------------
"""
 if i need to add elements od list 

"""
from functools import reduce
num = [3,4,5,6,7,8,9,9,2,10,100]
res = reduce(lambda x,y:x+y, num)
print (res)