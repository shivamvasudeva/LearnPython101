class Emp:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{self.fname}_{self.lname}@tech.com" not a good way
    def exp(self):
        return f'The First name is {self.fname} and last name is {self.lname}'
#Makes use of function as attirbute
    @property
    def email(self ):
        if self.fname ==None or self.lname ==None:
            return "Email is not set Please Use Setter...."
        return f"{self.fname}_{self.lname}@tech.com"
#Setter
    @email.setter
    def email(self,string):
        print("Setter Working Now....")
        names = string.split("@")[0]
        self.fname = names.split("_")[0]
        self.lname =names.split("_")[1]
#Deleter
    @email.deleter
    def email(self):
        self.fname = None
        self.lname =None


skillf =Emp("skills", "f")
# print(skillf.email)
#Object Introspection

#Checking the properties of object where it is coming from; what function it belongs to
#print(type(skillf))
#Checking the ID of the object
#print(id(skillf))
#Examples:
'''print(id("This"))
print(id("That"))'''

#Check all the methods being used
# Example:

'''o = "this is a string"
print(dir(o))
print(dir(skillf))'''

#Inspect Module

import inspect
print(inspect.getmembers(skillf))