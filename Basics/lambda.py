# Lambda Fucntions or Anonymous Functions
'''
minus = lambda x, y: x-y
print(minus(9,6))
'''
# Its just another way to make functions

# Conventional way
def a1(a):
    return a[1]

a = [[43,1],[50,6],[8,8]]
a.sort(key=a1) # It take function as input
print("With Function", a)

# Labda Way

a = [[43,1],[50,250],[520,2]]
a.sort(key=lambda x:x[1])
print('With Lambda:', a)