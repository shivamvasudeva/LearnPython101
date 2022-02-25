class A:
    classvar1 = "I am var in class A"

    def __init__(self):
        self.var1 = "I am inside class A Const"
        self.classvar1 = "Instance of var in class A"
        self.special = "Special in A Class"


class B(A):
    var1 = "I am  var in class B"

    def __init__(self): #We overwrite the const of class A
        super().__init__() # it will take the attirbutes of super claass: it means patrents class
        self.var1 = "I am inside class B Const"
        self.classvar1 = "Instance of var in class B"

a = A()
b =B()
print(b.var1)
print(b.special, b.var1, b.classvar1)