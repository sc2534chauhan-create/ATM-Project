balance = 10000.0
transactions = []


def check_balance():
    print(f"\nYour current balance is: ₹{balance:.2f}")


def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        balance += amount
        transactions.append(f"Deposited:  ₹{amount:.2f}  |  Balance: ₹{balance:.2f}")
        print(f"₹{amount:.2f} deposited successfully. New balance: ₹{balance:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")


def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return
        if amount > balance:
            print("Insufficient balance.")
            return
        balance -= amount
        transactions.append(f"Withdrawn:  ₹{amount:.2f}  |  Balance: ₹{balance:.2f}")
        print(f"₹{amount:.2f} withdrawn successfully. Remaining balance: ₹{balance:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")


def statement():
    print("\n===== TRANSACTION HISTORY =====")
    if not transactions:
        print("No transactions yet.")
    else:
        for i, t in enumerate(transactions, 1):
            print(f"{i}. {t}")
    print("================================")
