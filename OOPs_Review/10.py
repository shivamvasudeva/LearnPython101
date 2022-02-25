#Public Private and Procted Access Specifires


class Emp:
    no_of_leaves = 10 # Class variable
    _protac = 15 #Protacted Variable
    __pv = 100 #Private varibale
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
class Player:
    gamelimit = 4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    @classmethod
    def from_str(cls, string):
        return cls(*string.split(","))  # One Liner

    def print_details(self):
        return f"Name is {self.name}. Game is {self.Game}"

emp=Emp("Shivam",100,"test")

print(emp._protac)

print(emp.__pv) # this is name angling

print(emp._Emp__pv) # to use private variable we nee to use _Classname