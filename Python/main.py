# Wentworth Events Board Casino Assistant Tool (WEB-CAT)
# Program By Joe Machado

from functions import *  # imports all functions from the functions.py file

# ********** MAIN CODE **********

# Declaring variables that will be used to hold onto the total points and tickets that the CURRENT player has
current_points = 0   
current_tickets = 0

exit = 1

print("Welcome to the Wentworth Events Board Casino Assistant Tool (WEB-CAT)!\n")

while (exit != 0):
    print("Please choose one of the following options:\n")
    print("1. Convert Chips to Points and Tickets")
    print("2. View Help/Instructions")
    print("3. View Legal Information")
    print("4. View Program Information")
    print("5. [COMING SOON!] Chip Exchanger")
    print("6. Launch RandomPicker (Raffle Ticket Software)")
    print("0. Exit the program")
    choice = int(input("Enter your Choice: "))

    if choice == 1: # chips to tickets calculator chosen

        # calls the chips_to_tix function and stores the returned values into the current_points and current_tickets variables
        current_points, current_tickets = chips_to_tix()  
        
        # displays player's points and tickets to user
        print("Calculated Values:")
        print(f"Total Points for Current Player: {current_points} pts\n")
        print(f"Total Tickets for Current Player: {current_tickets} tix\n")
        print("_____________________________________________\n\n")

    elif choice == 2: # help/instructions
        display_help()
    
    elif choice == 3: # legal information
        display_legal_info()

    elif choice == 4: # program information
        display_program_info()

    elif choice == 5: # chip exchanger
       chip_exchanger()

    elif choice == 6: # launches RandomPicker
        launch_randompicker()
    
    elif choice == 0: # exit program
        print("Exiting Program...")
        exit = 0    #ends the loop
    else:
        print("Invalid Choice Entered. Please Try Again")
        print("_____________________________________________\n\n")
