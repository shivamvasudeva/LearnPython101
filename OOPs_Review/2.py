class Emp:
    no_of_leaves = 10 # Class variable
#Constructor: yeh function ko arg dene ke liye hai agr hm init nai use krenge to vo apne ap nai lega arg
    def __init__(self,name,sal,role):
        self.name =name
        self.sal=sal
        self.role =role
    def print_details(self):
        return f"Name is {self.name}. Sal is {self.sal} and role is {self.title}"

    # Self vo object hai jis pe ye function lagega; self apne aap arg le leta hai jis object ka nam hmne likha hai

shivam = Emp("Shivam",60000,"CloudEng")
guggu= Emp("Guggu",90000,"DEV")

print(shivam.name)

"""#Objects
shivam = Emp()
guggu = Emp()

#Instance Valirable
shivam.name = "Shivam"
shivam.title = "QA"
shivam.sal = 60000

guggu.name = "guggu"
guggu.title = "DEV"
guggu.sal = 90000
print (guggu.print_details())"""