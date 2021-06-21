with open("books.txt") as f:
    books=f.read()
    print(f'''***************
Books available:\n{books}
***************''')

class Issuer:
    def details(self, name, age, gender, book):
        self.name = name
        self.age = age
        self.gender = gender
        self.book = book
        if self.book in books:
            temp = books.replace(self.book,"")
            print(f'''
***************
{self.book} has been issued to {self.name}
Age: {self.age}
Gender: {self.gender}
***************
Books Reamining:\n {temp}
***************''')
            with open("books.txt", "w") as x:
                x.write(temp)
        elif self.book not in books:
            print("Sorry we dont have this book.")

user_name=input("Enter your name:\n")
user_age=input("Enter your age:\n")
user_gender=input("Enter your gender:\n")
user_book=input("Enter the name of the book you want:\n")

user=Issuer()
user.details(user_name, user_age, user_gender, user_book)
