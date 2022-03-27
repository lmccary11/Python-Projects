class Car:
    name = "Bullet"
    color = "blue"
    doors = "sedan"
    year = 2020
    drive = "auto"
    def getAvailability(self):        
        entry_color = input("Enter color Blue, Yellow, Red, or Green: ")
        entry_doors = input("Enter sedan or coupe: ")
        entry_year = input("Enter year: ")
        entry_drive = input("Enter transmission: ")
        print("You want a {}, {} {} with {} transmission.".format(entry_year,entry_color,entry_doors,entry_drive).upper())

class SUV(Car):    
        name = "Avenger"
        color = "all"    
        year = "all"
        trans = "both"
        extended = "both"        
        def getAvailability(self):        
            entry_color = input("Enter SUV color Blue, Yellow, Red, or Green: ")
            entry_extended = input("Extended SUV? Yes or No: ")
            entry_year = input("Enter SUV year: ")
            entry_drive = input("Enter SUV transmission, A or M: ")
            if ((self.color == "all" or entry_color.lower() == self.color) and
                (self.extended == "both" or entry_extended.lower() == self.extended) and
                (self.year == "all" or entry_year >= self.year) and
                (self.trans == "both" or entry_drive.lower() == self.trans)):
                print("Yes, we have a {}, {} {}, in that cab size and transmission.".format(entry_year,entry_color,self.name).upper())
            else:
                print("Sorry, we don't have that SUV available, try again.".upper())
                Avenger.getAvailability()        

class Truck(Car):            
        name = "Jupiter"
        color = "all"    
        year = "all"
        trans = "both"
        cab = "all"        
        moon_roof = True
        def getAvailability(self):        
            entry_color = input("Enter Truck color Blue, Yellow, Red, or Green: ")
            entry_cab = input("Extended, crew or double cab Truck? ")
            entry_year = input("Enter Truck year: ")
            entry_drive = input("Enter Truck transmission, A or M: ")
            if ((self.color == "all" or entry_color.lower() == self.color) and
                (self.cab == "all" or entry_cab.lower() == self.cab) and
                (self.year == "all" or entry_year >= self.year) and
                (self.trans == "both" or entry_drive.lower() == self.trans)):
                print("Yes, we have a {}, {} {}, in that cab size and transmission.".format(entry_year,entry_color,self.name).upper())
                if self.moon_roof == True:
                    print("The {} also has a moon roof!".format(self.name).upper())
            else:
                print("Sorry, we don't have that Truck available, try again.".upper())
                Jupiter.getAvailability()           
    
Bullet = Car()
Bullet.getAvailability()
Avenger = SUV()
Avenger.getAvailability()
Jupiter = Truck()
Jupiter.getAvailability()


