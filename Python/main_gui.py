import functions as func
import tkinter as tk

# "Exit" Menu
def open_exit_menu():
    exit_window = tk.Toplevel()
    exit_window.title("Exit Program")
    exit_window.geometry("400x200")

    exit_label = tk.Label(exit_window, text="Are you sure you want to exit the program?", font=("Arial", 12))
    exit_label.pack(pady=20)

    yes_button = tk.Button(exit_window, text="Yes", command=lambda: func.exit_program(exit_window), width=10)
    yes_button.pack(side=tk.LEFT, padx=20)

    no_button = tk.Button(exit_window, text="No", command=exit_window.destroy, width=10)
    no_button.pack(side=tk.RIGHT, padx=20)


# start making main window which allows the user to choose between the different options available in the program

# "Cash Out (Chips to Points and Tickets)" Menu

# Chip Exchanger Menu

# (add other menus here)
