
import re
import os
import platform
from forest import forest_path
from cave import cave_path

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def display_rules():
    print("""
    Welcome to the Adventure Game!
    Rules:
    - Make the right choices at each stage to win.
    - One wrong move and you lose!
    - You can replay if you lose.
    """)

def validate_name(name):
    # Name must start with alphabet, contain only alphanumerics, and length > 3
    return bool(re.match(r'^[A-Za-z][A-Za-z0-9]{3,}$', name))

def display_username_rules():
    print("Rules for username:")
    print("- Must start with an alphabet (A-Z or a-z)")
    print("- Can contain alphabets and numbers only")
    print("- Length must be greater than 3 characters")

def start_game():
    display_rules()
    first_attempt = True
    while True:
        name = input("Enter your username: ").strip()
        if validate_name(name):
            print(f"Welcome, {name}! Let's begin your adventure.")
            break
        else:
            print("Invalid username!")
            display_username_rules()
        first_attempt = False
    choose_path()


def choose_path():
    print("You stand at a crossroad. Choose your path:")
    print("1. Forest Path : Explore the mysterious forest.")
    print("2. Cave Path : Enter the dark cave.")
    while True:
        choice = input("Enter 1 for Forest or 2 for Cave: ").strip()
        if choice == '1':
            forest_path()
            break
        elif choice == '2':
            cave_path()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    replay_option()

def replay_option():
    while True:
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay in ["yes", "y"]:
            clear_screen()
            start_game()
            break
        elif replay in ["no", "n"]:
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    clear_screen()
    start_game()
