import os

def show_menu():
    print("Select an option:")
    print("1. Set DNS")
    print("2. Remove DNS")
    print("3. Exit")



def main():
    while True:
        show_menu()
        choice = input("Enter your Choice (1/2/3):")

        if choice == "1":
            os.system('python ActiveShecan.py')
        elif choice =="2":
            os.system('python DeactiveShecan.py')
        elif choice == "3":
            print('Exiting ...')
            break
        else:
            print("Invalid choise. Please try again")

if __name__ == "__main__":
    main();