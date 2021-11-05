class Library:
    def __init__(self,booksAva, booksIss):
        self.booksAva = booksAva
        self.booksIss = booksIss

    def issued(self,bookname):
        if bookname in self.booksAva:
            with open("books.txt","w") as f:
                f.write(self.booksAva.replace(bookname,""))
            with open("issued books.txt","w") as f:
                f.write(self.booksIss+"\n"+bookname+"\n")
            return True
        elif bookname not in self.booksAva:
            if bookname in self.booksIss:
                print("The book is curently issued by someone else. Sorry for the inconvinience.")
                return False
            elif bookname not in self.booksIss:
                print("Sorry we don't have this book.")
                return False
    
    def returned(self,bookname):
        if bookname in self.booksAva:
            print("The book is already returned.")
            return False
        elif bookname not in self.booksAva:
            if bookname in self.booksIss:
                with open("issued books.txt","w") as f:
                    f.write(self.booksIss.replace(bookname,""))
                with open("books.txt","w") as f:
                    f.write(self.booksAva+"\n"+bookname+"\n")
                return True
            elif bookname not in self.booksIss:
                print("This book doesn't belong to our library.")
                return False



class Student:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def issued(self,bookname):
        print(f'''{bookname} has been issued to
Name - {self.name}
Age - {self.age}
Gender - {self.gender}
Please keep the book in good condition and return it within 30 days.''')

    def returned(self,bookname):
        print(f'''{bookname} has been returnd by
Name - {self.name}
Age - {self.age}
Gender - {self.gender}
Thanks for visiting our library Do visit again!!.''')


if __name__ == '__main__':
    try:
        user_name=input("Enter your name:\n")
        user_age=input("Enter your age:\n")
        user_gender=input("Enter your gender:\n")

        stu=Student(user_name,user_age,user_gender)

        while True:
            with open("books.txt") as f:
                books_ava=f.read()
            
            with open("issued books.txt") as f:
                books_iss=f.read()

            lib = Library(books_ava,books_iss)

            command=input("> ").lower()
            if command == "borrow":
                user_book=input("Enter the name of the book you want:\n")
                lib.issued(user_book)
                if lib.issued(user_book) == True:
                    stu.issued(user_book)
                else:
                    pass
            elif command == "return":
                user_book=input("Enter the name of the book you want to return:\n")
                lib.returned(user_book)
                if lib.returned(user_book) == True:
                    stu.returned(user_book)
                else:
                    pass
            elif command=="quit":
                break
            else:
                print("I don't understand that.")
    except Exception as e:
        print(f"Your input threw an error:\n{e} ")