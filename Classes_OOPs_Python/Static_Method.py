class Employee:
    no_of_leaves = 10
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

    @classmethod
    def change_leaves_default(cls,changed_default):
        cls.no_of_leaves = changed_default

    @classmethod
    def from_str(cls, string):
        return cls(*string.split(';'))

    @staticmethod   #We put it in class to apply only to the objects within class
    def printit(string):
        print("This is a static methods: "+ string)

shivam = Employee("Shivam",28,"Cloud Engineer",1000,5)
jhankar = Employee("Jhankar",30,"Therepist",5000,6)
gudiya = Employee.from_str("Gudiya;25;admin;4500;9")

print(shivam.print_details())
print(jhankar.print_details())


gudiya.printit("Worked with instance of the classs")
Employee.printit("Worked with Class")
