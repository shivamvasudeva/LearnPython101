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

    @classmethod
    def from_str(cls, string):
        return cls(*string.split(';'))
        # params = string.split(";")
        # return cls(params[0],params[1],params[2],params[3],params[4])



# if i want my instance should also be able to access class variable
# takes class as input and the variable what we need to change

shivam = Employee("Shivam",28,"Cloud Engineer",1000,5)
jhankar = Employee("Jhankar",30,"Therepist",5000,6)
gudiya = Employee.from_str("Gudiya;25;admin;4500;9")

shivam.change_leaves_default(10)
print(shivam.print_details())
print(jhankar.print_details())
print(gudiya.job)
