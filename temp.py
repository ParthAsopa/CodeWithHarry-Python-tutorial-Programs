x=open("seats available.txt")
seatno=int(x.read())

class Passeneger:
    def details(self, name, age, gender):
        self.name = name
        self.age=age
        self.gender = gender
    def bookTicket(self):
        if seatno==0:
            print("Sorry no seats available")
        elif seatno!=0:
            seatLeft=seatno-1
            print(f'''
A seat has been booked to 
{self.name}
Age:{self.age}
Gender:{self.gender}
Seat number: {seatno}
Seats Left: {seatLeft}''')
            with open("seats available.txt","w") as f:
                f.write(str(seatLeft))
x.close()

print('''HI! Welcome to Indian Railways!
How may I help you?''')

command=input(">")
command=command.lower()


while True:
    if command=="book a ticket":
        name=input("Enter your name:")
        age=input("Enter your age:")
        gender=input("Enter your gender:")
        pas=Passeneger()
        pas.details(name,age, gender)
        pas.bookTicket()
        command=input(">")
    elif command == "exit":
        break
    else:
        print("I don't understand that.")
        command=input(">")

