from abc import ABC, abstractmethod
class Car(ABC):
    
    @abstractmethod
    def getAvailability(self):        
        pass

class SUV(Car):    
    
    def getAvailability(self):
        entry_color = input("Enter color Blue, Yellow, Red, or Green: ")
        entry_doors = input("Enter sedan or coupe: ")
        entry_year = input("Enter year: ")
        entry_drive = input("Enter transmission: ")
        print("You want a {}, {} {} with {} transmission for a good price.".format(entry_year,entry_color,entry_doors,entry_drive).upper())

class lot:
    def shop(self, j):
        print("I need to find a car for a reasonable price")
        j.getAvailability()
    

Avenger = SUV()
Avenger.getAvailability()


ford = lot()
ford.shop(Avenger)


