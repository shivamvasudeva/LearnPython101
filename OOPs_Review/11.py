#Super and Overridding
class A:
    var1 = "I am a VAR in Class A "
    def __init__(self):
        self.var1 = "I am in class A constructor"
        self.clsvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    var1 = "I am a VAR in Class B "
    def __init__(self):
        super().__init__()
        self.var1 = "I am in class B constructor"
        self.clsvar1 = "Instance var in class B"
a=A()
b=B()

print(b.special)
print(b.clsvar1)
print(b.var1)
print(b.clsvar1)
print(b.var1)
