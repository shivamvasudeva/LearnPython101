"""
def fn1():
    print("I have Interview")
fn2 =fn1
fn2()

def fn_returner(num):
    if num == 0:
        return print
    if num == 1:
        return sum # return function with a function
a = fn_returner(1)
print(a)
a = fn_returner(0)
print(a)

def exe(func):
    func("This")

exe(print)

"""


def dec1(func1): # takes function as argument
    def noexec():
        print("Executing Now")
        func1()
        print("Executed")
    return noexec
@dec1
def whoisshivam(): #this is func 1 used as a agr for dec1
    print("i am gooood")

#whoisshivam = dec1(whoisshivam)

whoisshivam()