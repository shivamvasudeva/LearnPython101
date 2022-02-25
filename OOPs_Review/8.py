
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

class CoolProg(Emp,Player):
    lang = "Python"
    def print_lang(self):
        print(self.lang)

#Data
shivam = Emp.from_str("Shivam,60000,CloudEng")
guggu= Emp.from_str("Guggu,90000,DEV")
gudiya=Player.from_str("gudiya,ludo")
manu=CoolProg("Shivam",8500,"test1")

print(manu.print_details())


