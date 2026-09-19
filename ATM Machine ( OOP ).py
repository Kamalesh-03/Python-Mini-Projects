class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234

    def check_pin(self):
        pin = int(input("Enter your PIN: "))

        if pin == self.pin:
            return True
        else:
            print("Incorrect PIN")
            return False

    def check_balance(self):
        print("Your balance is ₹", self.balance)

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        print("₹", amount, "deposited successfully")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= self.balance:
            self.balance -= amount
            print("₹", amount, "withdrawn successfully")
        else:
            print("Insufficient balance")


atm = ATM()

if atm.check_pin():

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            atm.check_balance()

        elif choice == 2:
            atm.deposit()

        elif choice == 3:
            atm.withdraw()

        elif choice == 4:
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice")