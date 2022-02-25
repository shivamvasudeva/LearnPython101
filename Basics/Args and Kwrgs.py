print("Function 1 with args")
def fn1(normal,*args):
    # agrs here is just a word you can use anything
    # we have to keep *args at the end always;
    # if kwargs is being used then use kwargs at the end
    print(normal)
    for items in args:
        print(items) #it comes as a tuple
list1= ["Shivam", "Vasudeva", "Gudiya","Vasudeva",19051995,14081993]
normal = "This is normal arg"
fn1(normal,*list1)


def fn2(normal,**kwargs):
    print(normal)
    for items in kwargs:
        print(items)
    for key, value in kwargs.items():
        print(f'{key} is a {value}')
print("Function 2 with kwargs")
dict_kw = {"Rohan":"Monitor", "Shivam":"Programmer","Gudiya":"Prefect","Sam":"Cook"}
normal = "This is normal arg"
fn2(normal, **dict_kw)