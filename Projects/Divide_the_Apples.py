# Harry got N number of apples. Harry has students;  He wants to distribute among them
#Number of appples given by frnds; he can ask for less or more
# you need to print if the number is in mn to mx is a devisor or not
# Input: n , mn ,mx from user
#Output: print if n is devisor or not


n = int(input("Enter number of apples: "))
mn = int(input ("Enter min number"))
mx = int(input("Enter Max number"))
if mn == mx:
    print("Please Enter a range")
for x in range(mn,mx+1,1):
    if n%x == 0:
        print(f"{x} is a devisor of {n}")
    else:
        print(f"{x} is not a devisor of {n}")
