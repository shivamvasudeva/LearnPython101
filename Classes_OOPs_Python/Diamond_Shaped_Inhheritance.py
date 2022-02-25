class A:
    def met(self):
        print("Class A Method")
class B(A):
    def met(self):
        print("Class B Method")
class C(A):
    def met(self):
        print("Class C Method")
class D(B,C): #B,C: B will be checked first if we reserve the order C,B then C will be checked frist
    pass

a =A()
b=B()
c=C()
d=D()

d.met()
