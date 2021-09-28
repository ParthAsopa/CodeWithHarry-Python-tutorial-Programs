hint='''Type 'quit' to exit.
Type 'play' to play the game.

Find and type the secret number:

Hints:
1.It is a single-digit number.
2.It is not a prime number.
3.It is an odd number.'''
print(hint)
guesses=0
max_guess=3
while True:
    command =input('>').lower()
    if command=='play':
        while guesses<max_guess:
            guess=input("Guess:")
            guesses+=1
            if guess!='9':
                print('Try again!')
            elif guess=='9':
                print('You won!!')
                break
        if guesses==max_guess:
            print('Sorry, no more chances left,you lost!!')
    elif command=='quit':
        print('Byee...have a great time!!')
        break
    else:
        print("I don't understand that.")