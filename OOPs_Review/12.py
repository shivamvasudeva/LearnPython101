#Diamond Shape Problem
#Multiple Inheritance

class A:
    def meth1(self):
        print("Class A")
class B(A):
    def meth1(self):
        print("Class B")
class C(A):
    def meth1(self):
        print("Class C")
class D(B,C):
    pass
a =A()
b= B()
c= C()
d=D()

print(d.meth1())