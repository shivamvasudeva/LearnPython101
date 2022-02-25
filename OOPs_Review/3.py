class Emp:
    no_of_leaves = 10 # Class variable
#Constructor: yeh function ko arg dene ke liye hai agr hm init nai use krenge to vo apne ap nai lega arg
    def __init__(self,name,sal,role,key):
        self.name =name
        self.sal=sal
        self.role =role
        self.key=key
    def test(self):
        test1 = f"{self.role}{self.key + 1}"
        return test1
    def print_details(self):
        return f"Name is {self.name}. Sal is {self.sal} and role is {self.role} {self.key}"
#we can use it as alternative constructor
# Self vo object hai jis pe ye function lagega; self apne aap arg le leta hai jis object ka nam hmne likha hai

#Data
shivam = Emp("Shivam",60000,"CloudEng",0)
guggu= Emp("Guggu",90000,"DEV",1)
new =  Emp("Test",101,"Test101",2)

#Run the functions
print(shivam.test() + shivam.print_details())

"""
#Objects
shivam = Emp()
guggu = Emp()

#Instance Valirable
shivam.name = "Shivam"
shivam.title = "QA"
shivam.sal = 60000

guggu.name = "guggu"
guggu.title = "DEV"
guggu.sal = 90000
print (guggu.print_details())

"""