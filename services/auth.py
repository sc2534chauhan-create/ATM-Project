def login():
    user_pin = "1234"
    attempts = 3

    while attempts > 0:
        pin = input("Enter your PIN: ")

        if pin == user_pin:
            print("Login Successful")
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN! Attempts left: {attempts}")

    return False
