class Menu :
    
    def show_menu(self):
    
        while(True):
            #  make the menu 
            menu = print("""
                1. Create a bank account
                2. Deposite Money 
                3. Withdraw Money
                4. Update details 
                5. details of account holder
                6. delete account details 
                7. To break the program 
                    """)
        
            user = int(input("What do you want to perform : "))
    
    # For created account
            if user == 1:
                print("Account created successfully")
            
    # For deposite money in account
            elif user == 2:
                print("Money deposite successfully")
            
    #   for withdraw money
            elif user == 3:
                print("Money withdraw successfully")
        
    # update details 
            elif user == 4:
                print("Details updated successfully ")
            
    # details of account holders 
            elif user == 5:
                print("details of account holders ")
            
    #  delete account holders 
            elif user == 6:
                print("delete account details ")
            
    # for break the loop 
            else:
                print("Program is closed successfully")
                break
    

    
menu = Menu()
menu.show_menu()

