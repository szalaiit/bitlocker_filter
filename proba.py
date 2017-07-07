
def Menu():
    choice = str(input("Selected: "))

    while True:

        if choice == "1":
            print("Asphalt Selected")
            break
        if choice == "2":
            print("Mixed Selected")
            break
        if choice == "3":
            print("OffRoad Selected")
            break
        if choice in ["e", "exit"]:
            print("exit")
            exit()
        else:
            print("\nPlease select a valid choice:\n")
            Selection()
    return choice

