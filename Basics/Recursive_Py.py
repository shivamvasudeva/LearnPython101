# Recursion means using fucntion inside a function

def factorial_irrtative(n):
    fac =1
    for i in range(n):
        fac = fac * (i+1)
    return fac
    """
    :param n: Int
    :return: n* n-1*n-2......
    """

"""
def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
num = int(input("Enter: "))
print("Using Irrtative method",factorial_irrtative(num))
print("Using Recursive method", factorial_recursive(num))
"""
# Quiz:
#Fibonacci Seq

def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1)+ fibo(n-2)
num = int(input("Enter: "))
print("Fibo", fibo(num))
"""
def fibo_i(n):
    fib =0
    for i in range(0,n):
        fib = fib + (i-1)+(i-2)
        print(fib)
    return fib
num = int(input("Enter: "))
print("Fib", fibo_i(num))"""