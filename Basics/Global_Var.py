"""
l = 20  # Global Var: Read only within Function;
b = 40
def func1(n):
    # l =5 # Local Var
    m = 8 # Local Var
    global l  # Gives permisions to modify global Var
    l+=45
    print(b, l,m,n, "I Printed")
func1("Shivam ")

"""
# Global come here not in the function
x =100
def func2():
    x = 50
    def func2_1():
        global x
        x = 200000
    print("Before Calling func 2.1", x)
    func2_1()
    print("After Calling func 2.1", x)
func2()
print(x)
#Quiz

