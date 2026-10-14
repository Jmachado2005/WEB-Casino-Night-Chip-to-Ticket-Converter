# Wentworth Events Board Casino Assistant Tool (WEB-CAT)
# Program By Joe Machado

from decimal import Decimal, ROUND_HALF_UP  # used later for rounding up for total tickets

# Declaring Chip Values for use later
WHITE_CHIP = 10
RED_CHIP = 25
BLUE_CHIP = 50
GREEN_CHIP = 100
BLACK_CHIP = 250
ORANGE_CHIP = 500
YELLOW_CHIP = 1000

# Declaring variables to hold onto the entered chip values from the user
white_chip_count = 0
red_chip_count = 0
blue_chip_count = 0
green_chip_count = 0
black_chip_count = 0
orange_chip_count = 0
yellow_chip_count = 0

# Declaring variables that will be used at the end for the calculations
total_points = 0
total_tickets_preround = 0.0
total_tickets = 0

# ** MAIN CODE **

print("\n\nWelcome to the Wentworth Events Board Casino Assistant Tool (WEB-CAT)!\n")

exit = 1

while (exit != 0):
    print("Please choose one of the following options:\n")
    print("1. Convert Chips to Points and Tickets")
    print("2. View Help/Instructions")
    print("3. View Legal Information")
    print("4. View Program Information")
    print("5. [COMING SOON!] Chip Exchanger")
    print("0. Exit the program")
    choice = int(input("Enter your Choice: "))

    if choice == 1: # chips to tickets calcualtor chosen
        print("\n*** Chip to Points and Tickets Conversion ***\n")
        print("Please enter the number of each chip you have:\n")

        white_chip_count = int(input("White Chips: "))
        if (white_chip_count < 0): white_chip_count = 0;  #if the user enters a negative number, set entered value to 0
        print(f"Value recorded for White Chips: {white_chip_count}\n")

        red_chip_count = int(input("Red Chips: "))
        if (red_chip_count < 0): red_chip_count = 0; 
        print(f"Value recorded for Red Chips: {red_chip_count}\n")

        blue_chip_count = int(input("Blue Chips: "))
        if (blue_chip_count < 0): blue_chip_count = 0; 
        print(f"Value recorded for Blue Chips: {blue_chip_count}\n")

        green_chip_count = int(input("Green Chips: "))
        if (green_chip_count < 0): green_chip_count = 0; 
        print(f"Value recorded for Green Chips: {green_chip_count}\n")

        black_chip_count = int(input("Black Chips: "))
        if (black_chip_count < 0): black_chip_count = 0; 
        print(f"Value recorded for Black Chips: {black_chip_count}\n")

        orange_chip_count = int(input("Orange Chips: "))
        if (orange_chip_count < 0): orange_chip_count = 0; 
        print(f"Value recorded for Orange Chips: {orange_chip_count}\n")

        yellow_chip_count = int(input("Yellow Chips: "))
        if (yellow_chip_count < 0): yellow_chip_count = 0; 
        print(f"Value recorded for Yellow Chips: {yellow_chip_count}\n")

        # calculates total points the player got
        total_points = (white_chip_count * WHITE_CHIP) + (red_chip_count * RED_CHIP) + (blue_chip_count * BLUE_CHIP) + (green_chip_count * GREEN_CHIP) + (black_chip_count * BLACK_CHIP) + (orange_chip_count * ORANGE_CHIP) + (yellow_chip_count * YELLOW_CHIP)

        # calculates total total tickets the player receives
        total_tickets_preround = total_points / 200
        num = Decimal(str(total_tickets_preround))

        total_tickets = num.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

        # displays player's points and tickets to user
        print("Calculated Values:")
        print(f"Total Points for Player: {total_points}\n")
        print(f"Total Tickets for Player: {total_tickets}\n")
        print("_____________________________________________\n\n")
    elif choice == 2: # help/instructions
        print ("\n*** Help/Instructions ***\n")

        print("Program Instructions:")
        print("1. Enter the number of each chip you have when prompted.")
        print("2. The program will calculate your total points and tickets based on the values you enter.")
        print("3. You can perform multiple conversions without exiting the program.")
        print("4. If you want to exit the program, choose option 0 from the start menu.")
        print("_____________________________________________\n")

        print("Chip Values:")
        print("White Chip: 10 points")
        print("Red Chip: 25 points")
        print("Blue Chip: 50 points")
        print("Green Chip: 100 points")
        print("Black Chip: 250 points")
        print("Orange Chip: 500 points")
        print("Yellow Chip: 1000 points")
        print("_____________________________________________\n")

        print("Additional Help/Instructions:")
        print("1. The conversion rate is 200 points = 1 ticket.")
        print("2. The program will round based on the tens place decimal value of the total points. For example, if you have 430 points, it will round down to 2 tickets. If you have 450 points, it will round up to 3 tickets.")
        print("3. This program will only accept integer values for the number of chips.")
        print("4. If you enter a negative number, the program will automatically set it to 0.")
        print("5. This UI is primarily text-based for now but will eventually be changed to GUI-based in the future.")
        print("_____________________________________________\n\n")
    elif choice == 3: # legal information
        print ("\n*** Legal Information ***\n")

        print("1. This program is a BETA and is subject to change at any point.")
        print("2. This program is not affiliated with the WEB or any of its affiliates. It was simply made because Joe is slow at counting chips and doing math")
        print("3. This program is not responsible for any errors or miscalculations that may occur. If you are unsure of a calculation for points or tickets, you should double check yourself that the math is correct")
        print("4. This program is an INTERNAL program and not for public use.")
        print("_____________________________________________\n\n")
    elif choice == 4: # program information
        print("\n*** Program Information ***\n")
        print("Program Name: WEB Casino Night - Chip to Tickets Converter [PYTHON VERSION]")
        print("Program Version: 1.0.0")
        print("Program Author: Joe Machado")
        print("Program Contribuiters: Ezra Doty, River Smith, Enzo Evola")
        print("Program Language: Python")
        print("Program License: Wentworth Events Board (WEB)/Internal Use Only")
        print("_____________________________________________\n\n")
    elif choice == 5: # chip exchanger
        print("\n*** Chip Exchanger ***\n")
        print("This feature is currently under development and will be available in a future update.")
        print("Please check back later for updates on this feature.")
        print("_____________________________________________\n\n")
    elif choice == 0: # exit program
        print("Exiting Program...")
        exit = 0    #ends the loop
    else:
        print("Invalid Choice Entered. Please Try Again")
        print("_____________________________________________\n\n")
