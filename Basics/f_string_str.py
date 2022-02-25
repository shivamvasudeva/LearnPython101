# F strings
#String Formating
import time
before_ex = time.gmtime()
age = 28
bday = "Aug,14"
year = 1993
name = "Shivam"
lname = "Vasudeva"
a = f'my name is {name} {lname}\nmy bday is on {bday}\nyear of my birth is {year}\nmy age is {age}'
print(a)
after_ex = time.gmtime()
ex_time = (after_ex) - (before_ex)
print(ex_time)