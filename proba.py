

while True:
    choice = str(input("Selected: "))


    if choice == "1":
        print("1 Selected")
        break
    if choice == "2":
        print("2 Selected")
        break
    if choice == "3":
        print("3 Selected")
        break
    if choice in ["e", "exit"]:
        print("exit")
        exit()
    else:
        print("\nPlease select a valid choice:\n")

