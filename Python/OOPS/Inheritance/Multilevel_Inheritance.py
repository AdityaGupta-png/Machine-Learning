# Making the example on the multilevel inheritance 

class Animal:
    # Constructor 
    def __init__(self,species):
        self.species = species
        
    # methods
    def showSpecies(self):
        print(f"Species : {self.species}")
        
class mammal(Animal) :
    
    # Constructor
    def __init__(self, species,has_fur):
        super().__init__(species)
        self.has_fur = has_fur
        
    def show_features(self):
        print(f"has_fur : {self.has_fur}")
        
class Dog(mammal) :
    
    # constructor 
    def __init__(self, species, has_fur,name,noOfLegs):
        super().__init__(species, has_fur)
        self.name = name
        self.noOfLegs = noOfLegs
        
    def showInfo(self):
        print(f"Name : {self.name}")
        print(f"noOfLegs : {self.noOfLegs}")
        
        
# Making the object of the Dog class --> Mammal --> Animal

A1 = Dog("Dog",True,"Tommy",4)
print(A1.name)
print(A1.noOfLegs)
print(A1.species)
print(A1.showSpecies())
print(A1.show_features())
print(A1.showInfo())

    

