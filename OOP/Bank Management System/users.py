class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")


class Admin(User):
    def __init__(self, name, email, address, password):
        super().__init__(name, email, address)
        self.password = password

    def display_admin_info(self):
        print(f"Admin Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")

    def check_admin_credentials(self, password):
        return self.password == password


class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.accounts = []
        self.loans_taken = 0  
        self.max_loans = 2     
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)
    
    def check_balance(self):
        total_balance = sum(account.check_balance() for account in self.accounts)
        print(f"Total balance across all accounts: {total_balance}")
        return total_balance

    def withdraw(self, amount):
        for account in self.accounts:
            if account.balance >= amount:
                account.withdraw(amount)
                return
        print("Insufficient funds across all accounts.")

    def deposit(self, amount):
        if self.accounts:
            self.accounts[0].deposit(amount)  
        else:
            print("No accounts found.")

    def take_loan(self, amount, bank):
        if not bank.loan_enabled:  
            print("Loan feature is currently disabled. Cannot take a loan.")
            return
        
        if self.loans_taken < self.max_loans:
            
            if self.accounts:
                
                self.accounts[0].balance += amount  
                print(f"Loan of {amount} approved. Added to account balance.")
                self.loans_taken += 1  
            else:
                print("You need to open an account first.")
        else:
            print("Maximum loan limit reached. You can only take two loans.")



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




central_bank = Bank("Central Bank")

def customer_menu(customer):
    while True:
        print(f"\n***** Welcome {customer.name} to The Central Bank!! *****")
        print("1. Open Savings Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Check Transaction History")
        print("6. Take Loan")
        print("7. Transfer Money")
        print("8. Exit")
        
        choice = int(input("Enter Your Choice : "))
        
        if choice == 1:
            initial_deposit = float(input("Enter initial deposit: "))
            central_bank.open_account(customer, "savings", initial_deposit)
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            customer.accounts[0].deposit(amount)  
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            customer.accounts[0].withdraw(amount)
        elif choice == 4:
            customer.accounts[0].check_balance()
        elif choice == 5:
            customer.accounts[0].check_transaction_history()
        elif choice == 6:
            amount = float(input("Enter loan amount: "))
            customer.take_loan(amount, central_bank)
        elif choice == 7:
            recipient_name = input("Enter recipient's name: ")
            amount = float(input("Enter amount to transfer: "))
            central_bank.transfer_funds(customer, recipient_name, amount)
        elif choice == 8:
            break
        else:
            print("Invalid Input")

def admin_menu(admin):
    while True:
        print(f"\nWelcome {admin.name}!!")
        print("1. Add New Customer")
        print("2. Delete Customer Account")
        print("3. View All Customers")
        print("4. Check Total Bank Balance")
        print("5. Check Total Loans")
        print("6. Toggle Loan Feature")
        print("7. Exit")
        
        choice = int(input("Enter Your Choice : "))
        
        if choice == 1:
            name = input("Enter Customer Name: ")
            email = input("Enter Customer Email: ")
            address = input("Enter Customer Address: ")
            customer = Customer(name=name, email=email, address=address)
            central_bank.add_customer(customer)
        elif choice == 2:
            customer_name = input("Enter customer name to delete: ")
            central_bank.delete_customer(customer_name)
        elif choice == 3:
            central_bank.view_all_customers()
        elif choice == 4:
            central_bank.check_total_balance()
        elif choice == 5:
            central_bank.check_total_loan()
        elif choice == 6:
            central_bank.toggle_loan_feature()
        elif choice == 7:
            break
        else:
            print("Invalid Input")


while True:
    print("Welcome to the Bank Management System!")
    print("1. Customer Login")
    print("2. Admin Login")
    print("3. Exit")
    choice = int(input("Enter your choice : "))
        
    if choice == 1:
        name = input("Enter Your Name: ")
        email = input("Enter Your Email: ")
        address = input("Enter Your Address: ")
        customer = Customer(name=name, email=email, address=address)
        central_bank.add_customer(customer)
        customer_menu(customer)
    elif choice == 2:
        name = input("Enter Admin Name: ")
        email = input("Enter Admin Email: ")
        address = input("Enter Admin Address: ")
        password = input("Enter Admin Password: ")
        admin = Admin(name=name, email=email, address=address, password=password)
        central_bank.add_admin(admin)
        admin_menu(admin)
    elif choice == 3:
        break
    else:
        print("Invalid Input!!")

