import json
import os
print(os.getcwd())
#Loads JSON >> Python : >> it cannot take file as arg, s in load means str; it take str as arg
"""data = '{"var1":"shivam", "var2":56}'
parsed = json.loads(data)
print(parsed["var1"])"""

#Load

#Dumps Python >> JSON
#Dict to JSON
data2 = {
    "3name": "Shivam Vasudeva",
    "4cars": ["bmw", "audi", "sonata"],
    "2phone": "iPhone 12",
    "1watch": ('apple watch', 'fossil'),
    "5bdayinaug": True
}

jsoncomp = json.dumps(data2)
print(jsoncomp)
"""
f = open("json_code.json", "w")
f.write(jsoncomp)
f.close"""

#Load >> it takes file as an arg
"""f = open("json_code.json", "r")
load_test = json.load(f)
print(load_test)"""

#sort_keys paramenter in dumps
jsoncomp = json.dumps(data2,sort_keys=True)
print("SortKey", jsoncomp)