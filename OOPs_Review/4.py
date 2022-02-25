#Class Methods

class Emp:
    no_of_leaves = 10 # Class variable
#Constructor: yeh function ko arg dene ke liye hai agr hm init nai use krenge to vo apne ap nai lega arg
    def __init__(self,name,sal,role):
        self.name =name
        self.sal=sal
        self.role =role
    def print_details(self):
        return f"Name is {self.name}. Sal is {self.sal} and role is {self.role}"
#we can use it as alternative constructor
# Self vo object hai jis pe ye function lagega; self apne aap arg le leta hai jis object ka nam hmne likha hai
# We can use class methods as alternative constructors
    @classmethod
    def change_leaves(cls,updated_leaves):
        cls.no_of_leaves = updated_leaves
#Data
shivam = Emp("Shivam",60000,"CloudEng")
guggu= Emp("Guggu",90000,"DEV")
new =  Emp("Test",101,"Test101")

#Run the functions
shivam.change_leaves(2)
print(guggu.no_of_leaves)