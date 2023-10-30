for num in range(1,5):
    
    try:
        num = int(input("Select an option (1-4): "))
        
        if num == 1:
            print("1 selected")
        elif num == 2:
            print("2 selected")
        elif num == 3:
            print("3 selected")
        elif num == 4:
            print("Quit selected")
            break  
        else:
            print("Option not recognized")
    except ValueError:
        print("Invalid input. Please enter an integer (1-4).")