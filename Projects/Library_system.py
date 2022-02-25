# Create a library class
# Display Book
# Lend Book
# Add book
# Return book
class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name= name
        self.lend= {}
    def displayBooks(self):
        print(f" Books in Library: {self.name} ")
        for book in self.booksList:
            print(book)
    def lendBook(self,user,book):
        if book not in self.lend.keys():
            self.lend.update({book:user})
            self.booksList.remove(book)
            print("Lender book database is updated: Take the book now")
        else:
            print(f"Book is taken by {self.lend[book]}")
    def addBook (self,book):
        self.booksList.append(book)
        print ("Book has been addded")
    def returnBook(self, book):
        self.lend.pop(book)
        self.booksList.append(book)
if __name__ == '__main__':
    Calgary_Library = Library(['Python',"AWS","Azure","C++","Java"], "Calgary_Library")
    while(True):
        print(f"Welcome to {Calgary_Library.name}")
        print("Enter your choice")
        print("1: Display Books ")
        print("2: Lend")
        print("3: Add")
        print("4: Return")

        user_choice = input()
        if user_choice not in ['1','2','3','4' ]:
            print("Please Enter Valid Option")
            continue
        else:
            user_choice=int(user_choice)


        if user_choice==1:
            Calgary_Library.displayBooks()
        elif user_choice==2:
            book = input("Enter the name of the book you wantr to lend: ")
            user = input("Enter your name")
            Calgary_Library.lendBook(user,book)
        elif user_choice==3:
            book = input("Enter the name of the book you want to Add: ")
            Calgary_Library.addBook(book)
        elif user_choice==4:
            book = input("Enter the name of the book you want to return: ")
            Calgary_Library.returnBook(book)
        else:
            print("Not a valid option")

        print("Q: Quit")
        print("C: Conti")
        user_choice2=""
        while(user_choice2 !="c" and user_choice2 !="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue


