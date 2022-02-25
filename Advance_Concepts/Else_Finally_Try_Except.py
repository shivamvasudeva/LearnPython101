f1 = open("test.txt")
try:
    f = open("test2.txt")
except Exception as e:
    print(e)
else:
    print("This will run only if EXCEPT is not running")
finally:
    print("Run this Finally block of code")
    try:
        f.close()
    except IOError as e:
        print(e)
    f1.close()
print("Run the rest of the code")