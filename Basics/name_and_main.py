# if we import; it will execute all the things
def printstr(str):
    return f" Yehs string: {str}"

def addit(n1,n2):
    return n1+n2+5
print ("name is", __name__) #test
if __name__ == '__main__':# we use this to avoid runnin the below code in another file wile imporing
    print(printstr("Shivam"))
    o = addit(5, 4)
    print(o)
