"""
> Itreable : __iter__() or __getitem__()

> Iterator: __next__()

> Irrtation:

Genrators are ittrators

Where we need genrator:

"""
#Genrating on the fly
"""for i in range(5):
    print(i)"""

def gen(n):
    for i in range(n+1):
        yield i

"""g = gen(15)
print(g)"""

#to irrtate in genrator
"""for i in range(5):
    print(g.__next__()) """

'''strs = [1,2,3,4,5]

ier = iter(strs)
for st in ier:
    print(st.__next__())
'''



"""for c in strs:
    print(c)"""
"""
> return:  It is return value of a function;  it will return and wont procede forward
> yield:  it will genrate values on the fly;  it is a genrator 
> print: it will just show the value 

"""