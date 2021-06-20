class Train:
    @staticmethod
    def __init__():
        print('''
*****Welconme To indian Railways!*****
''')
    def getStatus(self,trainname, seats, fare):
        self.trainname=trainname
        self.fare= fare
        self.seats= seats
rajdhani=Train()
rajdhani.getStatus("Rajdhani Express", 10 , "₹100")

class Passanger:
    def getPassanger(self,pas_name, pas_age, pas_gender):
            self.pas_name = pas_name
            self.pas_age = pas_age
            self.pas_gender=pas_gender
    def getTicket(self):
        if rajdhani.seats>0:
            print(f'''
*****************************
A ticket has been confirmed to 

Name: {self.pas_name}
Age : {self.pas_age}
Gender: {self.pas_gender}

*****************************
Train Name: {rajdhani.trainname}
Your seat number is: {rajdhani.seats}
Fee issued: {rajdhani.fare}
Number of seats remaining: {rajdhani.seats-1}

*****************************
''')
            rajdhani.seats -= 1
while rajdhani.seats>0:
    pas_name=input("Enter your name:")
    pas_age = input("Enter your Age:")
    pas_gender=input("Enter your gender:")

    pas= Passanger()
    pas.getPassanger(pas_name, pas_age, pas_gender)
    pas.getTicket()
print("The train is now full, kindly try in tatkal.")