def Menu():
    while True:
        choice = str(input("Selected: "))


        if choice == "1":
            print("Asphalt Selected")
            break
        if choice == "2":
            print("Mixed Selected")
            break
        if choice == "3":
            print("OffRoad Selected")
            break
        if choice == "e" or "exit":
            print("exit")
            exit()
        # else:
        #     print("\nPlease select a valid choice:\n")
        #     Selection()