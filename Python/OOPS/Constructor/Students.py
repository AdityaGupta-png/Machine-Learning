

# Constructor --> used to give the parameter inside the classs 
# Constructor --> it is magical method when we make the obejct of the class 
# constructor method run automatically 

class Students:
    
    # Constructor 
    def __init__(self,name,age,clg):
        self.name = name
        self.age = age
        self.clg = clg
        print(id(self))
        
    def greet(self):
        print("Hello Good Morning !!!!!!!!!!!")
        
        
    def info(self):
        print(f"My name is {self.name},age is {self.age} and clg name is {self.clg}")
        
        
# Making the Objects of the class 
S1 = Students("Aditya Gupta",21,"UCOE")
S1.info()
print(id(S1))

        
    
        
 
    
   
    