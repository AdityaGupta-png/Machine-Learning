

# Making the Dog class and the inherits the animal class 
from Animal import Animal


class Dog(Animal):
    
    # Constructor 
    def __init__(self,name,noOfEyes,noOfLegs):
        super().__init__(noOfEyes,noOfLegs)
        self.name = name;
        
    # Methods 
    def info(self):
        print(f"Name of the animal is {self.name}")
        print(f"{self.name} has {self.noOfEyes} eyses")
        print(f"{self.name} has  {self.noOfLegs} legs")
        


# Making the object of the class 
D1 = Dog("Tommy",2,4)
D1.info()
D1.running()
D1.eating()
D1.sleeping()
        
    