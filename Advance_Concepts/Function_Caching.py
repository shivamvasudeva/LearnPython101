import time
from functools import lru_cache      #it is a decorator


"""
@lru_cache(maxsize=3)
def func1(n):
    #Some task taking n sec
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Run the function ")
    func1(3)
    print("Done!! Calling again.....")
    func1(3)
    print("Done with CACHED Call!! ")"""


number = int(input("Enter: "))
@lru_cache(maxsize=number)
def func1(n):
    #Some task taking n sec
    time.sleep(n)
    return n
if __name__ == '__main__':
    print("Run the function 1 ")
    func1(3)
    print("Done!! Calling again..... 3 sec")
    func1(2)
    print("Done with CACHED Call!! 2 sec ")
    func1(3)
    print("Done with CACHED Call!! 3sec ")
    func1(5)
    print("Done with  Call!! 5sec ")
    func1(5)
    print("Done with CACHED Call!!  5sec ")
    func1(2)
    print("Done with CACHED Call!!  2sec ")

