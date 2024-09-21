import os
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def show_menu():
    print("Select an option:")
    print("1. Set DNS")
    print("2. Remove DNS")
    print("3. Display Dns")
    print("4. Exit")



def main():
    while True:
        show_menu()
        choice = input("Enter your Choice (1/2/3/4):")

        if choice == "1":
            os.system('python ActiveShecan.py')
        elif choice =="2":
            os.system('python DeactiveShecan.py')
        elif choice == "3":
            os.system('python DisplayDns.py')
        elif choice == "4":
            print('Exiting ...')
            break
        else:
            print(RED + "Invalid choise. Please try again" + RESET)

if __name__ == "__main__":
    main();