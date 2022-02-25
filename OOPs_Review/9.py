class Father:
    python = 1
class Son(Father):
    react = 2
    def print_whatdo_I_do(self):
        return f"yes i know {self.react}"
class GrandSon(Son):
    CPP= 1
    def print_whatdo_I_do(self):
        return f"I dont know 2 but i know {self.CPP}"



f=Father()
s=Son()
g=GrandSon()

print(g.print_whatdo_I_do())


