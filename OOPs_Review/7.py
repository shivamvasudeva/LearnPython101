
class Emp:
    no_of_leaves = 10 # Class variable
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
        return cls(*string.split(",")) #One Liner
    @staticmethod
    def static_meth(string):
        print("this is a static method: " + string)
        return
class Prog_Inheritance(Emp):
    def __init__(self,name,sal,role,lang):
        self.name = name
        self.sal = sal
        self.role = role
        self.lang =lang

    def print_pr(self):
        return f'the programmer name is {self.name} and he knows{self.lang}'


#Data
shivam = Emp.from_str("Shivam,60000,CloudEng")
guggu= Emp.from_str("Guggu,90000,DEV")
new = Prog_Inheritance.from_str("Test,101,Programmer,[java]")

#Run the functions
print(new.print_pr())