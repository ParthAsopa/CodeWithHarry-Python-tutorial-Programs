import random
num=random.randint(1,100)#random number between 1 to 10

guess=0
while True:
    user_guess=int(input('Enter your guess:'))#user's guess
    if user_guess>num:#user's guess larger than actuall number
        print("\nLower number please...\n")
        guess+=1
    elif user_guess<num:#user's guess smaller than actuall number
        print("\nHigher number please...\n")
        guess+=1
    elif user_guess==num:#user's guess equal to actuall number
        print(f"\nYou guessed it!!\nIt took you {guess} guesses.")
        break


with open("high_score.txt") as f:
    n=int(f.read())
if guess<n:#if no. guesses if less than last high score
    n=guess
    print("You just made a new high score.")
    with open("high_score.txt","w") as f:
        f.write(str(n))
elif guess >=n:#if no. guesses if greater than or equal to last high score
    pass       #do nothing
print(f"\nHigh Score = {n}\n")