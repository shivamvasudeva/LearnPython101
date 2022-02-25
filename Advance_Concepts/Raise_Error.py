"""a = input("What is your name: ")
b = int(input("Enter a number other than zero"))
if b ==0:
    raise ZeroDivisionError("Told Ya Dont add ZERO FUCKER")
if a.isnumeric():
    raise Exception ("Number not allowed")
print (f'Hellow {a}')
"""


c = input("Enter a name")
try:
    print(a)
except Exception as e:
    if c=='shivam':
        raise ValueError("Shivam is blocked")
    print("Exception Handled")