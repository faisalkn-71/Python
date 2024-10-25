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
