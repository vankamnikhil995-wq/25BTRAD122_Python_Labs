class BankAccount:

    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount! Deposit must be positive.")
        else:
            self.__balance += amount
            print("Amount deposited successfully!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount! Withdrawal must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully!")

    def balance_enquiry(self):
        print("Account Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Available Balance: Rs.", round(self.__balance, 2))


print("===== BANK ACCOUNT SYSTEM =====")

account_number = input("Enter account number: ")
account_holder = input("Enter account holder name: ")

account = BankAccount(account_number, account_holder)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif choice == 3:
            account.balance_enquiry()

        elif choice == 4:
            print("Thank you for using Bank Account System!")
            break

        else:
            print("Invalid choice! Please select 1 to 4.")

    except ValueError:
        print("Please enter a valid number.")
