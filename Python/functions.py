# this will be file that holds onto all the functions that the tool will use

from decimal import Decimal, ROUND_HALF_UP   # used later for rounding up for total tickets
from colorama import Fore, Style, init  # used for colored text in the terminal
import webbrowser

# Initialize colorama (autoreset=True automatically resets color after every print)
init(autoreset=True)

# Declaring Chip Values
WHITE_CHIP = 10
RED_CHIP = 25
BLUE_CHIP = 50
GREEN_CHIP = 100
BLACK_CHIP = 250
ORANGE_CHIP = 500
YELLOW_CHIP = 1000


def chips_to_tix():     # runs the chips to points & tickets calculator
    # when this function is called, it will ask the user to enter the amount of each chip they have.
    # the program will then calculate the total points and tickets that the player has based on the entered chip values.
    # these values will then get sent back to the main.py file where they will be displayed to the user (and can be used in other functions in the future when called)

    # Declaring variables to hold onto the entered chip values from the user
    white_chip_count = 0
    red_chip_count = 0
    blue_chip_count = 0
    green_chip_count = 0
    black_chip_count = 0
    orange_chip_count = 0
    yellow_chip_count = 0

    print("\n*** Chips to Points & Tickets Calculator ***")
    print("Please enter the number of each chip you have:\n")
    
    white_chip_count = int(input("White Chips: "))
    if (white_chip_count < 0): white_chip_count = 0;  #if the user enters a negative number, set entered value to 0
    print(Fore.WHITE + f"Value recorded for White Chips: {white_chip_count}\n")
    
    red_chip_count = int(input("Red Chips: "))
    if (red_chip_count < 0): red_chip_count = 0; 
    print(Fore.RED + f"Value recorded for Red Chips: {red_chip_count}\n")
    
    blue_chip_count = int(input("Blue Chips: "))
    if (blue_chip_count < 0): blue_chip_count = 0; 
    print(Fore.BLUE + f"Value recorded for Blue Chips: {blue_chip_count}\n")
    
    green_chip_count = int(input("Green Chips: "))
    if (green_chip_count < 0): green_chip_count = 0; 
    print(Fore.GREEN + f"Value recorded for Green Chips: {green_chip_count}\n")
    
    black_chip_count = int(input("Black Chips: "))
    if (black_chip_count < 0): black_chip_count = 0; 
    print(Fore.BLACK + Style.BRIGHT + f"Value recorded for Black Chips: {black_chip_count}\n")
    
    orange_chip_count = int(input("Orange Chips: "))
    if (orange_chip_count < 0): orange_chip_count = 0; 
    print(Fore.YELLOW + f"Value recorded for Orange Chips: {orange_chip_count}\n")
    
    yellow_chip_count = int(input("Yellow Chips: "))
    if (yellow_chip_count < 0): yellow_chip_count = 0; 
    print(Fore.LIGHTYELLOW_EX + f"Value recorded for Yellow Chips: {yellow_chip_count}\n")
    
    # calculates total points the player got
    total_points = (white_chip_count * WHITE_CHIP) + (red_chip_count * RED_CHIP) + (blue_chip_count * BLUE_CHIP) + (green_chip_count * GREEN_CHIP) + (black_chip_count * BLACK_CHIP) + (orange_chip_count * ORANGE_CHIP) + (yellow_chip_count * YELLOW_CHIP)
    
    # calculates total total tickets the player receives
    total_tickets_preround = total_points / 200
    num = Decimal(str(total_tickets_preround))
    
    total_tickets = num.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

    return total_points, total_tickets

def display_help():  # displays program's help/instructions to the user
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

def display_legal_info():  # displays program's legal information to the user
        print ("\n*** Legal Information ***\n")
        
        print("This program is a BETA and is subject to change at any point.")
        print("This program is not affiliated with WEB or any of its affiliates. It was simply made because Joe is slow at counting chips and doing math")
        print("This program is not responsible for any errors or miscalculations that may occur. If you are unsure of a calculation for points or tickets, you should double check yourself that the math is correct")
        print("This program is an INTERNAL program and not for public use.")
        print("_____________________________________________\n\n")

def display_program_info():  # displays program's information to the user
        print("\n*** Program Information ***\n")

        print("Program Name: Wentworth Events Board Casino Assistant Tool (WEB-CAT)")
        print("Program Version: 1.0.1")
        print("Program Author: Joe Machado")
        print("Program Contribuiters: Ezra Doty, River Smith, Enzo Evola")
        print("Program Language: Python")
        print("Program License: Wentworth Events Board (WEB)/Internal Use Only")
        print("_____________________________________________\n\n")

def chip_exchanger():  # chip exchanger function (currently under development)
    # allows the user to exchange lower chip values (white, red, blue & green) for higher chip values (black, orange, & yellow)
    # for example: if the user has 10 green chips (100pts each) they can exchange them for 1 yellow chip (1000pts)

    print("\n*** Chip Exchanger ***\n")
    print("This feature is currently under development and will be available in a future update.")
    print("Please check back later for updates on this feature!")
    print("_____________________________________________\n\n")

def launch_randompicker():  # launches randompicker (WEB's raffle ticket software) 
    # when launched it will allow the casino staff to enter in the user's name, email, and what they put their raffle tickets towards
    print("\n*** Launching RandomPicker (WEB's Raffle Ticket Software)! ***\n")
    print("Please ask a WEB Events Director for the Username and Password to log into the software!\n\n")

    webbrowser.open("https://app.randompicker.com/User/Account.aspx")  # opens the raffle ticket software in the user's default web browser
  
# add more functions here
