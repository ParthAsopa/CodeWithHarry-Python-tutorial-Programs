# Creating functions to update train's seats status
def log_read(name):
    with open(f"{name}.txt") as f:
        return int(f.read())

def log_update(name,seatsAva):
    with open(f"{name}.txt","w") as f:
        f.write(str(seatsAva))    

print('''********************************************************************************
Hi! Welcome to Indian Railways!
********************************************************************************''')

class Train:#class for train's functions
    def details(self,name):
        self.name = name
        self.seatsAva = log_read(self.name)

    def bookTicket(self):
        self.seatsAva=self.seatsAva-1
        log_update(self.name,self.seatsAva)
    
    def ticketCancel(self):
        self.seatsAva=self.seatsAva+1
        log_update(self.name,self.seatsAva)

class Passeneger:#class for passenger's functions
    def __details__(self, name, age, gender):
        self.name = name
        self.age=age
        self.gender = gender
    
    def bookTicket(self):
        name=input("Enter Train Name: \n").lower()
        trin=Train() #Creating an object for train to carry out passenger's function
        trin.details(name)
        if trin.seatsAva!=0:#If steats are available
            print(f'''
********************************************************************************
A seat has been booked to 
{self.name}
Age:{self.age}
Gender:{self.gender}
Train Name: {trin.name}
Seat number: {trin.seatsAva}
''')
            trin.bookTicket()            
            print(f'''Seats Left: {trin.seatsAva}
********************************************************************************''')
        
        elif trin.seatsAva ==0:#If seats not available
            print('''********************************************************************************

Sorry, no seats available
Try in some other train.

********************************************************************************''')
    
    def ticketCancel(self):
        name=input("Enter Train Name: \n").lower()
        trin=Train()
        trin.details(name)
        trin.ticketCancel()
        print(f'''
********************************************************************************
The following seat has been canceled:
Name: {self.name}
Age: {self.age}
Gender: {self.gender}
Seat number: {trin.seatsAva}
Seats Available: {trin.seatsAva}
********************************************************************************''')

while True:
    print('''
How may I help you?
''')
    
    command=input(">")
    command=command.lower()

    if command=="book a ticket":
        name=input("Enter your name: \n")
        age=input("Enter your age: \n")
        gender=input("Enter your gender: \n")
        pas=Passeneger()
        pas.__details__(name,age,gender)
        pas.bookTicket()
    elif command=="cancel ticket":
        name=input("Enter your name: \n")
        age=input("Enter your age: \n")
        gender=input("Enter your gender: \n")
        pas=Passeneger()
        pas.__details__(name,age,gender)
        pas.ticketCancel()
    elif command == "exit":
        break    
    else:
        print("I don't understand that.")
