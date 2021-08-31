def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Options:")
        print("9 - Quit")
        choice = int(input("Enter your choice: "))
        print(type(choice))
        if choice == 9:
            keep_running = False
    
    print(choice)
    return choice


interface()