# Classes - Template
# Ojects - Instance of Classes
#Dry -  Donot repeat yourself
#Class
class Emp:
    chutiyan = 8

    pass

#Objects
shivam = Emp()
guggu = Emp()

#Instance Valirable
shivam.name = "Shivam"
shivam.title = "QA"
shivam.sal = 60000
print(shivam.__dict__)
guggu.name = "guggu"
guggu.title = "DEV"
guggu.sal = 90000
print (guggu.chutiyan)

