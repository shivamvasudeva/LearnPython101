import time

initial = time.time()
k = 0
while(k<10):
    print(k+1)
    time.sleep(1) #add a lag of time
    k+=1
print("While Loop Ran for: ", time.time()-initial)

"""
initial2 = time.time()
for i in range(10):
    print("Shivam")
print("For Loop Ran for: ", time.time()-initial2)
"""


"""

localtime = time.asctime(time.localtime(time.time()))
print(localtime)"""