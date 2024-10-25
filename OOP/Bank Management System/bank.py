from accounts import SavingsAccount, CheckingAccount  
from users import Customer

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.admins = []
        self.total_balance = 0
        self.total_loans = 0
        self.loan_enabled = True

    def add_admin(self, admin):
        self.admins.append(admin)
        print(f"Admin {admin.name} added to {self.name}")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} added to {self.name}")

    def open_account(self, customer, account_type, initial_deposit=0):
        if account_type == "savings":
            account = SavingsAccount(customer, initial_deposit)
        elif account_type == "checking":
            account = CheckingAccount(customer, initial_deposit)
        else:
            print("Invalid account type")
            return None

        customer.create_account(account)  
        print(f"{account_type.capitalize()} account opened for {customer.name}. Account number: {account.account_number}")
        return account

    def check_total_balance(self):
        total_balance = sum(account.balance for customer in self.customers for account in customer.accounts)
        self.total_balance = total_balance
        print(f"Total available balance in the bank: {self.total_balance}")

    def check_total_loan(self):
        total_loans = sum(customer.loans_taken for customer in self.customers)
        self.total_loans = total_loans
        print(f"Total loan amount: {self.total_loans}")

    def delete_customer(self, customer_name):
        customer = next((cust for cust in self.customers if cust.name == customer_name), None)
        if customer:
            
            if customer.accounts:  
                for account in customer.accounts:
                    print(f"Deleting account {account.account_number} associated with {customer.name}.")
                    

            self.customers.remove(customer)
            print(f"Customer {customer.name} deleted from {self.name}.")
        else:
            print(f"Customer {customer_name} not found.")

    def view_all_accounts(self):
        print("Viewing all accounts.")
        
    def view_all_customers(self):
        if not self.customers:
            print("No customers in the bank.")
            return
        print("List of Customers:")
        for customer in self.customers:
            print(f"Name: {customer.name}, Email: {customer.email}, Address: {customer.address}")
    
    def transfer_funds(self, sender, recipient_name, amount):
        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        recipient = next((cust for cust in self.customers if cust.name == recipient_name), None)
        if not recipient:
            print("Account does not exist.")
            return

        if sender.check_balance() >= amount:
            sender.withdraw(amount)  
            recipient.deposit(amount)  
            print(f"Successfully transferred {amount} from {sender.name} to {recipient.name}.")
        else:
            print("Withdrawal amount exceeded.")
    
    def toggle_loan_feature(self):
        self.loan_enabled = not self.loan_enabled  
        if self.loan_enabled:
            print("Loan feature is now enabled.")
        else:
            print("Loan feature is now disabled.")
