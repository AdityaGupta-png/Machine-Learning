# Making the example on the every type of the inheritance 

# Perfect example of the single Inheritance 

class Car:
    # Attribute 
    def __init__(self,model,noOfTyres,noOfLights,noOfDoors):
        self.__model = model
        self.__noOfTyres = noOfTyres
        self.__noOfLights = noOfLights
        self.__noOfDoors = noOfDoors
        
    # Methods 
    def showInfo(self):
        print(f"model of the car is {self.__model}")
        print(f"noOftyres in the car is {self.__noOfTyres}")
        print(f"Lights are in car is {self.__noOfLights}")
        
    # We should make the method private but we have to acces the methods like the getter and setter 
        
    def engineStart(self):   
        print("The car is started ")
        
    def stopEngine(self):
        print("The car is stopped")
        
    def noOfDoors(self):
        print(f"The no of doors present in the car is {self.__noOfDoors}")
        
    # Generate the getter and setter of the car class 
    
    # For the model 
    def getModel(self):
        return self.__model
    
    def setModel(self,new_Model):
        self.__model = new_Model
        
    # For the noOfTyres 
    def getNoOfTyres(self):
        return self.__noOfTyres
    
    def setNoOfTyres(self,new_TyresNo):
        self.__noOfTyres = new_TyresNo
        
    # For the noOfLights 
    def getNoOfLights(self):
        return self.__noOfLights
    
    def setNoOfLights(self,new_Lights):
        self.__noOfLights = new_Lights
        
    # For the noOfDoors 
    def getNoOfDoors(self):
        return self.__noOfDoors
    
    def setNoOFDoors(self,new_NoOfDoors):
        self.__noOfDoors = new_NoOfDoors
        

# Making the Gwagon class that inherits the car class 
class Gwagon(Car):
    
    # Constructor of the class 
    def __init__(self, model, noOfTyres, noOfLights, noOfDoors,name):
        super().__init__(model, noOfTyres, noOfLights, noOfDoors)
        self.__name = name
        
    # Generate getter and the setter 
    def getName(self):
        return self.__name
    
    def setName(self,new_name):
        
        if(len(new_name) > 0):
            self.__name = new_name
        else:
            print("Name could not be empty")
            

# Making the object of the Gwagon class that inherits the Car class 
G1 = Gwagon("G20",4,2,4,"Gwagon_new")
G1.showInfo()
print(G1.getName())
G1.engineStart()
G1.setNoOfTyres(6)
print(G1.getNoOfTyres())
    


