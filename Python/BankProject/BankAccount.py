class BankAccount:
    
    # Making the constructor 
    def __init__(self,account_number,name,age,phone,balance):
        self.__account_number = account_number
        self.__name = name
        self.__age = age 
        self.__phone = phone
        self.__balance = balance
        
    # methods to show info 
    def showInfo(self):
        print(f"Account Number of the user is {self.__account_number}")
        print(f"Name of the user is {self.__name}")
        print(f"Balance in the user account is {self.__balance}")
        print(f"Phone number of the user is {self.__phone}")
        print(f"Age of the user is {self.__age}")
        
        
    # method for the deposite money 
    def deposite(self,money):
        
        if money <= 0:
            print("Invalid numbers ")
            return
        
        self.__balance += money
        
        print("Money deposite successfully !!")
        print(f"{money} amount is credited in your account")
        print(f"Total amount in your account is {self.__balance}")
        
    # Method for withdraw mwthods 
    def withdraw(self,money):
        
        if money <= 0:
            print("Invalid operation ")
            return
        
        self.__balance -= money
        print("Money withdraw successfully!!")
        print(f"{money} amount is debited from your account ")
        print(f"Total amount in your account is {self.__balance}")
        
    # Generate getter and setter methods 
    # for the account number 
    def getAccountNumber(self):
        return self.__account_number
    
    def setAccountNumber(self,new_acc_number):
        self.__account_number = new_acc_number
        
    # for the name 
    def getName(self):
        return self.__name
    
    def setName(self,new_name):
        self.__name = new_name
        
    # for the balance 
    def getBalance(self):
        return self.__balance
    
    def setBalance(self,new_Balance):
        self.__balance = new_Balance
        
    # for the phone 
    def getPhoneNumber(self):
        return self.__phone
    
    def setPhoneNumber(self,new_number):
        self.__phone = new_number
        
    # for the age 
    def getAge(self):
        return self.__age
    
    def setAge(self,new_age):
        self.__age = new_age
    

        
    
        

    


