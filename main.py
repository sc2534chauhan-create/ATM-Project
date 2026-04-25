from services.auth import login
from services.atm import check_balance, deposit, withdraw, statement

if login():

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Statement")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            statement()

        elif choice == "5":
            print("Thank you for using ATM ")
            break

        else:
            print("Invalid choice, try again!")

else:
    print("Account blocked due to wrong PIN attempts.")
