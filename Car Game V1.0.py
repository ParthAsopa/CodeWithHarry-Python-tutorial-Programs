instructions='''Type exit to exit.
type start or stop to control the car.'''
print(instructions)
car_start=False
Input=input("> ")
while True:
    if Input.lower()=="start":
        if not car_start:
            print("The car has started.")
            car_start=True
            Input=input("> ")
        elif car_start:
            print("Broo...the car is already started...what are you doing??")
            Input=input("> ")
    elif Input.lower()=="stop":
        if car_start:
            print("The car has stopped.")
            car_start=False
            Input=input("> ")
        elif not car_start:
            print("Broo...the car is already stopped...what are you doing??")
            Input=input("> ")
    elif Input.lower()=="exit":
        break
    else:
        print("I dont't understand that.")
        Input=input("> ")