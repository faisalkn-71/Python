from bank import Bank
from users import Customer, Admin

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

