
"""
Class Methods as alternative constructor

We Use args kwargs to make the code more clean we dont have to write split everywhere
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
""" we can use it as alternative constructor
# Self vo object hai jis pe ye function lagega; self apne aap arg le leta hai jis object ka nam hmne likha hai
# We can use class methods as alternative constructors """
    @classmethod
    def change_leaves(cls,updated_leaves):
        cls.no_of_leaves = updated_leaves
    @classmethod
    def from_str(cls,string):
        """ params = string.split(",")""" #It will pars the strign and make a list
        """ return cls(params[0],params[1],params[2])""" #here cls means EMP Class
        return cls(*string.split(",")) #One Liner
#Data
shivam = Emp.from_str("Shivam,60000,CloudEng")
guggu= Emp.from_str("Guggu,90000,DEV")
new = Emp.from_str("Test,101,Student")

#Run the functions
print(new.sal)
print(shivam.print_details())