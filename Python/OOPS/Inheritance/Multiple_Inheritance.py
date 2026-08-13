
# Example on the Multiple inheritance 

# Class of the Dad
class Dad:
    
    # Constructor
    def __init__(self, name, hardWorker, notshowlove):
        self.dad_name = name
        self.hardWorker = hardWorker
        self.notshowlove = notshowlove

# Class of the Mom
class Mom:
    
    # Constructor of the mom
    def __init__(self, name, care):
        self.mom_name = name
        self.care = care

# Classs of the Child 
class Child(Dad, Mom):
    
    # Constructor of the child class
    def __init__(self, dad_name, hardWorker, notshowlove, mom_name, care, child_name):
        Dad.__init__(self, dad_name, hardWorker, notshowlove)  # call Dad constructor
        Mom.__init__(self, mom_name, care)                     # call Mom constructor
        self.child_name = child_name

    def my_Info(self):
        print(f"My name is {self.child_name}.")
        print(f"My father {self.dad_name} is hardworking: {self.hardWorker}, "
              f"but not showing love: {self.notshowlove}.")
        print(f"My mother {self.mom_name} takes lots of care: {self.care}.")

# Making the object of the child 
C1 = Child("Ajeet", True, "yes", "Sunita", True, "Aditya")
C1.my_Info()


        
    
        

