print('type help to see instructions.')
started= False
command=''
while True:
    command=input('> ').lower()
    if command =='help':
        print('''Type:
start: to start the car
stop: to stop the car
quit: to quit/exit the game''')
    elif command == 'start':
        if started:
            print('Dude...the car is already started...what are you doing?')
        elif not started:
            print('The car has started.')
            started = True
    elif command=='stop':
        if not started:
            print('Dude...the car is already stopped...what are you doing?')
        elif started:
            print('The car has stopped.')
            started = False
    elif command =='quit':
        print('Good byee!!')
        break
    else:
        print("I don't understand that.")