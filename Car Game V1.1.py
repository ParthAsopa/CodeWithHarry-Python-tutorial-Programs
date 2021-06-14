instructions='''Type:
Start : To start the car.
Stop : To stop the car.
Right : To turn the car right.
Left : To turn the car left.
Directions : To know the direction in which the car is moving.
Exit/Quit : To exit the game.'''
print("Type 'instructions' to get the instructions.")
car_start=False
car_direction="North"
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
    elif Input.lower()=="instructions":
        print(instructions)
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
    elif Input.lower()=="left":
        if car_direction=="North":
            car_direction="West"
        elif car_direction=="West":
            car_direction="South"
        elif car_direction=="South":
            car_direction="East"
        elif car_direction=="East":
            car_direction="North"
        print("The car has turned left.")
        Input=input("> ")
    elif Input.lower()=="right":
        if car_direction=="North":
            car_direction="East"
        elif car_direction=="West":
            car_direction="North"
        elif car_direction=="South":
            car_direction="West"
        elif car_direction=="East":
            car_direction="South"
        print("The car has turned right.")
        Input=input("> ")
    elif Input.lower()=="directions":
        print(f"The car is facing in {car_direction} direction. ")
        Input=input("> ")
    elif Input.lower()=="quit":
        break
    else:
        print("I dont't understand that.")
        Input=input("> ")