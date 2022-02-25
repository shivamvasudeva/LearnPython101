#Mapping Operator to Functions
#Dunder Methodds
#Operator overloading

class Employee:
    no_of_leaves = 8
    def __init__(self,aname,aage,ajob,apay,aleaves_taken):
        self.name = aname
        self.age = aage
        self.job=ajob
        self.pay = apay
        self.leaves_taken = aleaves_taken



    def print_details(self):
        return f"Name is {self.name}. Age is {self.age} and job is {self.job} and pay is {self.pay}. You have only {self.number_of_leaves_left()} Leaves Left"

    def number_of_leaves_left(self):
        left = Employee.no_of_leaves - self.leaves_taken
        return left

    @classmethod #Decorator
    def change_leaves_default(cls,changed_default):
    #what is CLS ? it is a class which is the instance
        cls.no_of_leaves = changed_default
 #Dunder Methods
    def __add__(self, other):
        return self.pay + other.pay
    def __truediv__(self, other):
        return self.age / other.age
    def __repr__(self): #REPR method
        return f"Name '{self.name}' and Pay is '{self.pay}'"
    def __str__(self): # by default it use this
        return f"Name is {self.name}. Age is {self.age} and job is {self.job} and pay is {self.pay}. You have only {self.number_of_leaves_left()} Leaves Left"


# if i want my instance should also be able to access class variable
# takes class as input and the variable what we need to change

shivam = Employee("Shivam",28,"Cloud Engineer",1000,5)
#jhankar = Employee("Jhankar",30,"Therepist",5000,6)

print(shivam)


