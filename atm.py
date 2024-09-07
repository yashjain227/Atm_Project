class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def verify_pin(self):
        entered_pin =int( input("Enter your PIN: "))
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN.")
            return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
        self.transaction_history.append("Checked balance")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"You have successfully withdrawn ${amount}. New balance: ${self.balance}")
            self.transaction_history.append(f"Withdrew ${amount}")

    def deposit(self, amount):
        self.balance += amount
        print(f"You have successfully deposited ${amount}. New balance: ${self.balance}")
        self.transaction_history.append(f"Deposited ${amount}")

    def change_pin(self):
        old_pin = int(input("Enter your current PIN: "))
        if old_pin == self.pin:
            new_pin = int(input("Enter your new PIN: "))
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("Changed PIN")
        else:
            print("Incorrect current PIN.")

    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transactions available.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

def atm_menu(atm):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            if atm.verify_pin():
                atm.check_balance()
        elif choice == '2':
            if atm.verify_pin():
                amount = float(input("Enter the amount to withdraw: "))
                atm.withdraw(amount)
        elif choice == '3':
            if atm.verify_pin():
                amount = float(input("Enter the amount to deposit: "))
                atm.deposit(amount)
        elif choice == '4':
            atm.change_pin()
        elif choice == '5':
            atm.show_transaction_history()
        elif choice == '6':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Initialize an ATM with a PIN and starting balance
my_atm = ATM(pin=1234, balance=1000)


# Run the ATM menu
atm_menu(my_atm)
