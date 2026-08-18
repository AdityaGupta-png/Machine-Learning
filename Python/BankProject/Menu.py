# Import the BankAccount 
from BankAccount import BankAccount

class Menu :
    
    # Creating the empty list that stores allinformation 
    def __init__(self):
        self.accounts = []
        
    # Created bank account  methods 
    def create_Account(self):
        # Taking input 
        accountNumber = str(input("Enter your account number :"))
        name = str(input("Enter your name : "))
        age = int(input("Enter your age : "))
        phone = str(input("Enter your number : "))
        balance = int(input("Enter your balance : "))
                    
        account = BankAccount(
            accountNumber,
            name,
            age,
            phone,
            balance
        )
                    
        # Append all details to the accounts lists
        self.accounts.append(account)
        print("Account Created successfully !!!!")
        
    # Method to show user details 
    def show_user_details(self):
        
        account_number = str(input("Enter your account number : "))
        
        for account in self.accounts:
            
            # Check account numbers then show details 
            if account.getAccountNumber() == account_number:
                account.showInfo()
                return
        
        print("Account not found")
           
    # Method to deposite money 
    def deposite_money(self):
        
        # take input account number input 
        account_number = str(input("Enter your account number : "))
        
        
        # search for the accounts 
        for account in self.accounts:
            
            if account.getAccountNumber() == account_number:
                
                money = int(input("Enter the amount do you want to deposite : "))
                
                # deposite money 
                account.deposite(money)
                return
            
        print("Invalid account number !!!!")
                
    #   Method to withdraw money 
    def withdraw_money(self):
        
        # take input account number 
        account_number = str(input("Enter your account number : "))
        
        # search the account number 
        for account in self.accounts:
            
            if account.getAccountNumber() == account_number:
                
                money = int(input("How much do want to withdraw : "))
                
                # withdraw money 
                account.withdraw(money)
                return
        print("Inavlid Operation !!!!")
        
    # for the remove the user 
    def delete_user(self):
        
        # Take input of the user 
        account_number  = str(input("Enter your account number :  "))
        
        # search for the account number 
        for account in self.accounts :
            
            if account.getAccountNumber() == account_number:
                
                self.accounts.remove(account)
                print("User deleted permanetly!!")
                return 
            
        print("User not found")
    
    def show_menu(self):
    
        while(True):
            #  make the menu 
            menu = print("""
                1. Create a bank account
                2. Deposite Money 
                3. Withdraw Money
                4. details of account holder
                5. delete account details 
                6. To break the program 
                    """)
        
            user = int(input("What do you want to perform : "))
    
    # For created account
            if user == 1:
                self.create_Account()
            
    # For deposite money in account
            elif user == 2:
                self.deposite_money()
            
    #   for withdraw money
            elif user == 3:
                self.withdraw_money()
        
    # details of account holders 
            elif user == 4:
                self.show_user_details()
            
    #  delete account holders 
            elif user == 5:
                self.delete_user()
            
    # for break the loop 
            else:
                print("Program is closed successfully")
                break
            
        
    

    

