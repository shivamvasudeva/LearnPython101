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


"""I dont want to use it as a fucntion
What we can do ?
We will use a decorator"""

#Objects
shivam_vasudea = Emp("shivam","vasudeva")
jhankar_vasudeva = Emp("jhankar","vasudeva")

'''
print(shivam_vasudea.email)
print(Jhankar_vasudeva.email)
Jhankar_vasudeva.lname = "grover_vasudeva"
print(Jhankar_vasudeva.email())  #it will not be updated; why  ?? becuase we had self.email attirbute
'''

shivam_vasudea.email= ("this_that@shivamvasudeva.ca")
print(shivam_vasudea.email)
print(shivam_vasudea.fname)

"""
i want to write a funcrion which changes with the change in fname and lname
if i dont need the fucntion what i will do ?
"""

#Deleter

del shivam_vasudea.email
print(shivam_vasudea.email)