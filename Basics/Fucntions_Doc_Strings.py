#Built in Function
a =9
b =10
c = sum((a,b))
print(c)

#User Defined Functions
def fn1():
    print("First func of pycharm")
print(fn1())
# Why none value with print
fn1()

def fn2(a,b):
    """ This is a function which will cal avg of 2 numbers"""
    avg  = (a+b)/2
    print(f"fn2 without return val: {avg}")
    return avg
v = fn2(4,7)
print(f"fn2 with return valve stored in a variable {v}")
print(fn2.__doc__)


