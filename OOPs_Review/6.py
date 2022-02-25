"""
I don't need class or instance variable

Static Methods

Why we need to put it in class
Ans: When you need to run a func on the objects in the class
no class or instance variable reqiured

"""

class Emp:
    no_of_leaves = 10 # Class variable
#Constructor: yeh function ko arg dene ke liye hai agr hm init nai use krenge to vo apne ap nai lega arg
    def __init__(self,name,sal,role):
        self.name =name
        self.sal=sal
        self.role =role
    def print_details(self):
        return f"Name is {self.name}. Sal is {self.sal} and role is {self.role}"

    @classmethod
    def change_leaves(cls,updated_leaves):
        cls.no_of_leaves = updated_leaves
    @classmethod
    def from_str(cls,string):
        """ params = string.split(",")""" #It will pars the strign and make a list
        """ return cls(params[0],params[1],params[2])""" #here cls means EMP Class
        return cls(*string.split(",")) #One Liner
    @staticmethod
    def static_meth(string):
        print("this is a static method: " + string)
        return

#Data
shivam = Emp.from_str("Shivam,60000,CloudEng")
guggu= Emp.from_str("Guggu,90000,DEV")
new = Emp.from_str("Test,101,Student")

#Run the functions
new.static_meth("Test")