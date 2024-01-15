class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self.balance}")
            else:
                print("Insufficient funds. Cannot withdraw.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def get_balance(self):
        return self.balance


def create_account():
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: $"))
    return BankAccount(account_holder, initial_balance)


def main():
    print("Welcome to the Bank System!")
    account = create_account()

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            amount = float(input("Enter deposit amount: $"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: $"))
            account.withdraw(amount)
        elif choice == "3":
            balance = account.get_balance()
            print(f"Current balance: ${balance}")
        elif choice == "4":
            print("Thank you for using our bank!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()