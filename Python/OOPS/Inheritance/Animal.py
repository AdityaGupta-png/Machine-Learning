# There are 5 types of the Inheritance 

""""
1 --> Single Inheritance 
2 --> Multilevel Inheritance 
3 --> Multiple Inheritance 
4 --> Heriachical Inheritance 
5 --> Hybrid Inhritance --> (Mix of any 2 inheritance)
"""

# Making the Animal class 
class Animal:
    
    # Constructor of class 
    def __init__(self,noOfEyes,noOfLegs):
        self.noOfEyes = noOfEyes
        self.noOfLegs = noOfLegs
        
    # Methods 
    def eating(self):
        print("Animal is eating ")
        
    def running(self):
        print("Animal is running")
        
    def sleeping(self):
        print("Animal is sleeping")
        