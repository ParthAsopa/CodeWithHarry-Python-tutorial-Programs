count=1
while count!=4:
    count=str(count)
    try:
        print(f"Trying to find '{count}.txt'...\n")
        with open(f"{count}.txt", "r") as f:
            print("file found\n")
            print(f"It says : {f.read()}\n")
    except FileNotFoundError as e:
        print("Error: File not found\n")
    count=int(count)
    count+=1