
# Polymorphism --> Many faces 
#  In PYTHON Polymorphism --> support only the Method overriding 
# python not support the Method Overlaoding 

# Making the class of student1 
class Student1 :
    
    # Constructor 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    # Method 
    def showInfo(self):
        print(f"Student name is {self.name} and its age  is {self.age}")
        
        
# Making second class of the student2 
class Stduent2(Student1):
    
    # Constructor of the class 
    def __init__(self, name, age):
        super().__init__(name, age)

        
    # Method 

    def showInfo(self):
        print(f"Name of the student is {self.name} and age is {self.age}")
        
# Making the obejct of the Student2 class 
S2 = Stduent2("Chandan Gupta",21)
S2.showInfo()

# Making the object of the student1 class 
S1  = Student1("Aditya Gupta",21)
S1.showInfo()
        
    
    