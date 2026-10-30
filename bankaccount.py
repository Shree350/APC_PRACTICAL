
class BankAccount:
    account_number = 1001

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        self.account_number = BankAccount.account_number
        BankAccount.account_number += 1

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(self.account_holder, "Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful!")
        else:
            print("Insufficient balance for transfer!")


# Create two bank accounts
a1 = BankAccount("Rahul")
a2 = BankAccount("Amit")

# Perform transactions
a1.deposit(5000)
a1.withdraw(1000)
a1.transfer(2000, a2)

# Display account details
print("\nAccount Number:", a1.account_number)
a1.display_balance()

print("\nAccount Number:", a2.account_number)
a2.display_balance()
