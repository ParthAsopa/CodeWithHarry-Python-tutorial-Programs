class Rail_ticket:
    @staticmethod
    def __init__():
        print('Welconme To indian Railways!')
    def getName(self,name):
        self.name=name
    def getStatus(self, no_of_seats):
        self.status= no_of_seats
    def getFare(self, fare):
        self.fare= fare
Parth=Rail_ticket()
Parth.getName("Parth")
Parth.getStatus(15)
Parth.getFare("₹500")
print(f'''A ticket has been confirmed to {Parth.name}
No. of seats remaining {Parth.status}
Fare received {Parth.fare}''')
