# Classes -- Templates
# What is Object -- Instance of the class
# Why Class?
# Use DRY Concept > Do not repeat yourself

class Student:
    pass
shivam = Student() # these are objects of class
vasudeva = Student()

shivam.name = "Shivam"
shivam.lastname =" Vasudeva "
shivam.age = 28
shivam.job = "Cloud Engineer"
shivam.location = "Calgary"
shivam.province = "Alberta"
shivam.country = "Canada"
print("Address: ", shivam.location,",",shivam.province,",", shivam.country)