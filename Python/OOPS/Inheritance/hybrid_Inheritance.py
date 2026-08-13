
# making the example on the hybrid inheritance
# 
class Animal:
    
    # Constructor of the class 
    def __init__(self,species):
        self.species = species
        
    # Methods 
    def show_species(self):
        print(f"species : {self.species}")
        
# class name is Dog 
class Dog(Animal) :
    
    # Constructor 
    def __init__(self, species,name,noOfLegs):
        super().__init__(species)
        self.name = name
        self.noOfLegs = noOfLegs
        
    # Methods 
    def eating(self):
        print(f"{self.name} is eating ")
        
    def running(self):
        print(f"{self.name} is running")
        
    def sleeping(self):
        print(f"{self.name} is sleeping")
        
    def showInfo(self):
        print(f"Species is {self.species},name is {self.name} and legs are {self.noOfLegs}")
        
# class name is Cat 
class Cat(Animal):
    
    # Constructor 
    def __init__(self, species,name ,noOfLegs):
        super().__init__(species)
        self.name = name
        self.noOfLegs = noOfLegs
        
    # Methods 
    def eating(self):
        print(f"{self.name} is eating ")
        
    def running(self):
        print(f"{self.name} is running")
        
    def sleeping(self):
        print(f"{self.name} is sleeping")
        
    def showInfo(self):
        print(f"Species is {self.species},name is {self.name} and legs are {self.noOfLegs}")
    
    
# making the object of the Dog class 
D1 = Dog("Dog","Tommy",4)
D1.showInfo()

# making the object of the cat class 
C1 = Cat("Cat","Jully",4)
C1.showInfo()