class ED:
    Power = "120-220v"
    Size = "5inch-100inch"
    UsedFor= "Entertainment"

    def printdata(self):
        return f"Electronics Device is usualy powered in with {self.Power}, Size ranging {self.Size} and is used for {self.UsedFor}"

class PG(ED):
    Portable= "Portable"
    Power= "5V"
    Size = "5inch-15inch"

    def printdata(self):
        return f"Portable device usualy is {self.Portable},Size ranging {self.Size} and works on {self.Power} "

class Ph(PG):
    UsedFor = "Entertainment & Calling"
    def printdata(self):
        return f"Phones are used for {self.UsedFor},Size ranging {self.Size} and is {self.Portable} "

iphone = Ph()
tv = ED()
ipod = PG()

print(iphone.printdata())
print(tv.printdata())
print(ipod.printdata())