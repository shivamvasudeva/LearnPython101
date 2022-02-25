import random

# Randint
rand1 = random.randint(0,10000)
print(rand1)
# Random
rand2 = random.random() *1000
print(rand2)
# Choice
list1 = ["audi","bmw", 'benz', 'acura', 'lexus', 'lambo']
rand3 = random.choice(list1)
print(rand3)

import os

print(os.uname())
print(os.getcwd())