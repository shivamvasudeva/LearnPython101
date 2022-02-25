# 3 Clients --- Harry, Rohan Hammad
# Total 6 Files
# Write a function that when executed take name as input as client name
import datetime
def gettime():
    return datetime.datetime.now()
def log(choice_of_client):
    if choice_of_client == 1:
        choice_of_file = int(input(" 1 for Exercice\n2 for Food: "))
        if choice_of_file == 1:
            data= input("Enter the Exercies here: ")
            with open ("Sam-ex.txt",'a') as f:
                f.write("Time: " + str(gettime())+ " " + data+ '\n')
            print("Data Added to Ex file")
        elif choice_of_file == 2:
            data= input("Enter the Exercies here: ")
            with open("Sam-food.txt",'a') as f:
                f.write("Time: " + str(gettime())+ " " + data+ '\n')
            print("Data Added to Ex file")
    if choice_of_client ==2:
        choice_of_file = int(input(" 1 for Exercice\n2 for Food: "))
        if choice_of_file == 1:
            data= input("Enter the Exercies here: ")
            with open("Bing-ex.txt",'a') as f:
                f.write("Time: " + str(gettime())+ " " + data+ '\n')
            print("Data Added to Ex file")
        elif choice_of_file == 2:
            data= input("Enter the Exercies here: ")
            with open("Bing-food.txt",'a') as f:
                f.write("Time: " + str(gettime())+ " " + data+ '\n')
            print("Data Added to Ex file")
    if choice_of_client ==3:
        choice_of_file = int(input(" 1 for Exercice\n2 for Food: "))
        if choice_of_file == 1:
            data= input("Enter the Exercies here: ")
            with open("Ross-ex.txt",'a') as f:
                f.write("Time: " + str(gettime())+ " " + data+ '\n')
            print("Data Added to Ex file")
        elif choice_of_file == 2:
            data= input("Enter the Exercies here: ")
            with open("Ross-food.txt",'a') as f:
                f.write("Time: " + str(gettime())+ " " + data+ '\n')
            print("Data Added to Ex file")

def retrive(choice_of_client):
    if choice_of_client == 1:
        choice_of_file = int(input(" 1 for Exercice\n2 for Food: "))
        if choice_of_file == 1:
            with open("Sam-ex.txt") as f:
               r =  f.read()
               print(r)
        elif choice_of_file == 2:
            with open("Sam-food.txt") as f:
                r = f.read()
                print(r)
    if choice_of_client ==2:
        choice_of_file = int(input(" 1 for Exercice\n2 for Food: "))
        if choice_of_file == 1:
            with open("Bing-ex.txt") as f:
                r = f.read()
                print(r)
        elif choice_of_file == 2:
            with open("Bing-food.txt") as f:
                r = f.read()
                print(r)
    if choice_of_client ==3:
        choice_of_file = int(input(" 1 for Exercice\n2 for Food: "))
        if choice_of_file == 1:
            with open("Ross-ex.txt") as f:
                r = f.read()
                print(r)
        elif choice_of_file == 2:
            with open("Ross-food.txt") as f:
                r = f.read()
                print(r)
print ("Enter 1 to add Data")
print("Enter 2 To Read Data")
choice_of_fn = int(input("Choice is yours"))
print("Enter 1 for Sam")
print("Enter 2 for Bing")
print("Enter 3 for Ross")
choice_of_client = int(input("Enter value: "))
if choice_of_fn == 1:
    log(choice_of_client)
else:
    retrive(choice_of_client)





