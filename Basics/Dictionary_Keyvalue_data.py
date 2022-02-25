#Dictory: key vaule pairs

d1 = {"Audi":"A4","BMW":"X7", "Acura":{"SED":"ILX", "SUV": "MDX"}}
d2 = {"Audi":"A4","BMW":"X7", "Acura":["ILX","MDX"]}
print(d1["Acura"]['SUV'])
print(d2["Acura"])
d2["Hyundai"] = "Sonata"
d2["Honda"] = "Accord"
print(d2)
del d2["Acura"]
print(d2)

d3 =d2.copy()
print(d3)
d3["Nissan"] = "Altima"
print(d3)
d2.update({"Lexus": "LX"})
print(d2.items())

#Question

#Create a Dict and Take Input from User and return the meaning of the word from dict
dict1 = {"Audi":"A4","BMW":"X7", "Acura":"ILX","Nissan": "Altima" }
user_input= input("Enter car brand: ")
print(dict1[user_input])