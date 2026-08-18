class BankAccount:
    
    # Making the constructor 
    def __init__(self,account_number,name,age,phone,balance):
        self.account_number = account_number
        self.name = name
        self.age = age 
        self.phone = phone
        self.balance = balance
        
    # methods to show info 
    def showInfo(self):
        print(f"Account Number of the user is {self.account_number}")
        print(f"Name of the user is {self.name}")
        print(f"Balance in the user account is {self.balance}")
        print(f"Phone number of the user is {self.phone}")
        print(f"Age of the user is {self.age}")
        

    


