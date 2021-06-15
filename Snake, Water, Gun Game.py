import random
print("Type 'exit' to exit")
result=""
while True:
    print("Computer's Turn")
    rand =random.randint(1,3)
    if rand==1:
        comp="s"
    elif rand==2:
        comp="w"
    elif rand==3:
        comp="g"
    player=input("Your turn: Choose from Snake(s) or Water(w) or Gun(g):")
    if player.lower()=="exit":
        break
    elif comp =="s":
        if player.lower() == "s":
            result="Tie"
        if player.lower() == "w":
            result="Lose"
        if player.lower() == "g":
            result="Win"
    elif comp =="w":
        if player.lower() == "s":
            result="Win"
        if player.lower() == "w":
            result="Tie"
        if player.lower() == "g":
            result="Lose"
    elif comp =="g":
        if player.lower() == "s":
            result="Lose"
        if player.lower() == "w":
            result="Win"
        if player.lower() == "g":
            result="Tie"
    print(f'''Copmuter Chose : {comp}
    {result}''')
print("Thanks for playing!!")