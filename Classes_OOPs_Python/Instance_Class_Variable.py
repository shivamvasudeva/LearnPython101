class Employee:
    no_of_leaves = 8 # Class Var; only class can overright no object instance can change it
    pass
shivam = Employee()
jhankar = Employee()

shivam.name = "Shivam"
shivam.age = 28
shivam.job = "Cloud Engineer"
shivam.pay = 6000
shivam.leaves_taken = 5
print(shivam.__dict__)

jhankar.name = "Jhankar"
jhankar.age = 30
jhankar.job = "Therepist"
jhankar.pay = 5000
jhankar.leaves_taken = 6
print(jhankar.__dict__)
print(Employee.__dict__)
