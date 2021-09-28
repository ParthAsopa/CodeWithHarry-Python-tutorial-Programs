import random
num=random.randint(1,10)

guess=0
while True:
    user_num=int(input('Enter your guess:'))
    if user_num>num:
        print("\nLower number please...\n")
        guess+=1
    elif user_num<num:
        print("\nHigher number please...\n")
        guess+=1
    elif user_num==num:
        print(f"\nYou guessed it!!\nIt took you {guess} guesses.")
        break
with open("high_score.txt") as f:
    n=int(f.read())
if guess<n:
    n=guess
    print("You just made a new high score.")
    with open("high_score.txt","w") as f:
        f.write(str(n))
elif guess >=n:
    pass
print(f"\nHigh Score = {n}\n")