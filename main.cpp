//WEB Casino Night Chip to Points Conversion + Ticket Conversion
#include <iostream>
#include <cmath>

using namespace std;

//***declaring constant values for each of the chips***
const int WHITE_CHIP = 10;      //white chip is worth 10 points
const int RED_CHIP = 25;        //red chip is worth 25 points
const int BLUE_CHIP = 50;       //blue chip is worth 50 points
const int GREEN_CHIP = 100;     //green chip is worth 100 points
const int BLACK_CHIP = 250;     //black chip is worth 250 points
const int ORANGE_CHIP = 500;    //orange chip is worth 500 points
const int YELLOW_CHIP = 1000;   //yellow chip is worth 1000 points

//Main function
int main() 
{
    //variables that will hold onto the number of chips for each color tha that the user has - setting to 0 to start
    int white_chip_count = 0;
    int red_chip_count = 0;
    int blue_chip_count = 0;
    int green_chip_count = 0;
    int black_chip_count = 0;
    int orange_chip_count = 0;
    int yellow_chip_count = 0; 

    //variables that will be used in the final calculation of the total points and tickets to be then shown to the user
    int total_points = 0;   //holds onto the total points (all the chips added up)
    float total_tickets_preround = 0;  //holds onto the total tickets WITH the decimal part before the rounding occurs
    int total_tickets = 0;  //holds onto the total tickets WITHOUT the decimal part which is after tghe rounding occurs and will be the value displayed to the user for their tickets


    //welcome messages:
    cout << "Welcome to the WEB Casino Night Chip to Points Conversion + Ticket Conversion!" << endl;
    cout << "Please keep in mind the following:" << endl;
    cout << "----------------------------------------" << endl;

    //** main code **
    int exit = 1; //variable that will be used to determine if the user wants to exit the program or not
    int choice;   //variable that will be used to hold onto the user's choice of what they want to do in the program
    
    while (exit != 0) //infinite loop that will keep the program running until the user decides to exit
    {
        cout << "Please choose one of the following options:" << endl;
        cout << "1. Convert Chips to Points and Tickets" << endl;
        cout << "2. View Help/Instructions" << endl;
        cout << "3. View Legal Information" << endl;
        cout << "4. View Program Information" << endl;
        cout << "0. Exit the program" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        if (choice == 1) //if the user chooses to convert chips to points and tickets
        {
            cout << "*** Chip to Points and Tickets Conversion ***" << endl << endl;
            cout << "Please enter the number of each chip you have:" << endl;
            cout << "White Chips: ";
            cin >> white_chip_count;
            if (white_chip_count < 0) { white_chip_count = 0; } //if the user enters a negative number, set it to 0
            cout << "Value entered for White Chips: " << white_chip_count << endl << endl; //display the value entered for white chips

            cout << "Red Chips: ";
            cin >> red_chip_count;
            if (red_chip_count < 0) { red_chip_count = 0; }
            cout << "Value entered for Red Chips: " << red_chip_count << endl << endl; //display the value entered for red chips

            cout << "Blue Chips: ";
            cin >> blue_chip_count;
            if (blue_chip_count < 0) { blue_chip_count = 0; }
            cout << "Value entered for Blue Chips: " << blue_chip_count << endl << endl; //display the value entered for blue chips

            cout << "Green Chips: ";
            cin >> green_chip_count;
            if (green_chip_count < 0) { green_chip_count = 0; }
            cout << "Value entered for Green Chips: " << green_chip_count << endl << endl; //display the value entered for green chips

            cout << "Black Chips: ";
            cin >> black_chip_count;
            if (black_chip_count < 0) { black_chip_count = 0; }
            cout << "Value entered for Black Chips: " << black_chip_count << endl << endl; //display the value entered for black chips

            cout << "Orange Chips: ";
            cin >> orange_chip_count;
            if (orange_chip_count < 0) { orange_chip_count = 0; }
            cout << "Value entered for Orange Chips: " << orange_chip_count << endl << endl; //display the value entered for orange chips

            cout << "Yellow Chips: ";
            cin >> yellow_chip_count;
            if (yellow_chip_count < 0) { yellow_chip_count = 0; }
            cout << "Value entered for Yellow Chips: " << yellow_chip_count << endl << endl; //display the value entered for yellow chips

            //calculating total points
            total_points = (white_chip_count * WHITE_CHIP) + (red_chip_count * RED_CHIP) + (blue_chip_count * BLUE_CHIP) + (green_chip_count * GREEN_CHIP) + (black_chip_count * BLACK_CHIP) + (orange_chip_count * ORANGE_CHIP) + (yellow_chip_count * YELLOW_CHIP);

            //calculating total tickets
            total_tickets_preround = static_cast<float>(total_points) / 200.0f;
            total_tickets = static_cast<int>(round(total_tickets_preround));

            //displaying results to the user
            cout << "Total Points of User: " << total_points << endl;
            cout << "Total Tickets of User: " << total_tickets << endl;
            cout << "----------------------------------------" << endl << endl << endl;
        }
        else if (choice == 2) //if the user chooses to view help/instructions
        {
            cout << "*** Help/Instructions ***" << endl << endl;

            cout << "Program Instructions:" << endl;
            cout << "1. Enter the number of each chip you have when prompted." << endl;
            cout << "2. The program will calculate your total points and tickets based on the values you enter." << endl;
            cout << "3. You can perform multiple conversions without exiting the program." << endl;
            cout << "4. If you want to exit the program, choose option 0 from the start menu." << endl;
            cout << "----------------------------------------" << endl << endl;

            cout << "Help/Instructions for Each Chip Type:" << endl;
            cout << "1. White Chip: Worth 10 points." << endl;
            cout << "2. Red Chip: Worth 25 points." << endl;
            cout << "3. Blue Chip: Worth 50 points." << endl;
            cout << "4. Green Chip: Worth 100 points." << endl;
            cout << "5. Black Chip: Worth 250 points." << endl;
            cout << "6. Orange Chip: Worth 500 points." << endl;
            cout << "7. Yellow Chip: Worth 1000 points." << endl;
            cout << "----------------------------------------" << endl << endl;

            cout << "Additional Help/Instructions:" << endl;
            cout << "1. The conversion rate is 200 points = 1 ticket." << endl;
            cout << "2. The program will round based on the tenths place decimal value. For example, if you have 430 tickets, it will round down to 2 tickets. If you have 450 tickets, it will round up to 3 tickets." << endl;
            cout << "3. This program will only accept integer values for the number of chips." << endl;
            cout << "4. If you enter a negative number, the program will automatically set it to 0." << endl;
            cout << "5. This UI is primarily text-based for now but will eventually be changed to GUI-based in the future." << endl;
            cout << "----------------------------------------" << endl << endl << endl;
        }
        else if (choice == 3) //if the user chooses to view legal information
        {
            cout << "*** Legal Information ***" << endl << endl;

            cout << "1. This program is a BETA and is subject to change at any point." << endl;
            cout << "2. This program is not affiliated with the WEB or any of its affiliates. It was simply made because Joe is slow at counting chips and doing math" << endl;
            cout << "3. This program is not responsible for any errors or miscalculations that may occur." << endl;
            cout << "4. This program is an INTERNAL program and not for public use." << endl;
            cout << "----------------------------------------" << endl << endl << endl;
        }
        else if (choice == 0) //if the user chooses to exit the program
        {
            cout << "Exiting the program..." << endl;
            exit = 0; //set exit to 0 to break the loop and exit the program
        }
        else if (choice == 4) //if the user chooses to view program information
        {
            cout << "*** Program Information ***" << endl << endl;
            cout << "Program Name: WEB Casino Night Chip to Points Conversion + Ticket Conversion" << endl;
            cout << "Program Version: 1.0.0" << endl;
            cout << "Program Author: Joe Machado" << endl;
            cout << "Program Language: C++" << endl;
            cout << "Program License: Internal Use Only" << endl;
            cout << "----------------------------------------" << endl << endl << endl;
        }
        else //if the user enters an invalid choice
        {
            cout << "Invalid choice. Please try again." << endl;
            cout << "----------------------------------------" << endl << endl << endl;
        }
    }

    return 0;
}