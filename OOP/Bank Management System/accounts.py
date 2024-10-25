class Account:
    def __init__(self, customer, initial_balance=0):
        self.customer = customer
        self.balance = initial_balance
        self.account_number = self.generate_account_number()
        self.transaction_history = []

    def generate_account_number(self):
        import random
        return f"AC{random.randint(100000, 999999)}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            print(f"Successfully deposited {amount}. New balance: {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Successfully withdrew {amount}. New balance: {self.balance}.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
            
            
class SavingsAccount(Account):
    def __init__(self, customer, initial_deposit):
        super().__init__(customer, initial_deposit)
        self.account_type = "savings"


class CheckingAccount(Account):
    def __init__(self, customer, initial_deposit):
        super().__init__(customer, initial_deposit)
        self.account_type = "checking"
