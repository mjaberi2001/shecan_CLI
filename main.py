import os
import sys
import subprocess

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def get_file_path(file_name):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, file_name)

def show_menu():
    print("Select an option:")
    print("1. Set DNS")
    print("2. Remove DNS")
    print("3. Display DNS")
    print("4. Live Network Traffic")
    print("5. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your Choice (1/2/3/4/5):")

        if choice == "1":
            script_path = get_file_path('ActiveShecan.py')
            subprocess.run(['python', script_path])
        elif choice == "2":
            script_path = get_file_path('DeactiveShecan.py')
            subprocess.run(['python', script_path])
        elif choice == "3":
            script_path = get_file_path('DisplayDns.py')
            subprocess.run(['python', script_path])
        elif choice == "4":
            script_path = get_file_path('LiveTraffic.py')
            subprocess.run(['python', script_path])
        elif choice == "5":
            print('Exiting ...')
            break
        else:
            print(RED + "Invalid choice. Please try again." + RESET)

if __name__ == "__main__":
    main()
