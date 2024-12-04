class car:
    def __init__(self, Reg, Make, Mil, DOI):
        self.registration = Reg
        self.Make = Make
        self.Mileage = Mil
        self.DateOfInspection = DOI

    def getReg(self):
        return self.registration
    
    def getmake(self):
        return self.make
    
    def getmileage(self):
        return self.mileage
    
    def getDate(self):
        return self.DateOfInspection
    
    def setDate(self):
        self.DateOfInspection = int(input("Give date other buckets (in form DDMMYYYY): "))


thiscar = car("BMT 216A", "Aston Martin DB5", 0)

print(thiscar.getReg())
print(thiscar.getmake())
print(thiscar.getmileage())
print(thiscar.getDate())
print(thiscar.setDate())