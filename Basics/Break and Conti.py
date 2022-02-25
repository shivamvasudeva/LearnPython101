i = 0
while (True):
    if i+1<25:
        i = i + 1
        continue #Current irrtation in while loop


    print(i+1, end = " ")
    if (i==49):
        break #Stop the Loop
    i = i + 1

    #Quiz
while(True):
    i = int(input("Enter number:"))
    if i >=100:
        print("its 100000")
        break
    else:
        print("try again")
        continue