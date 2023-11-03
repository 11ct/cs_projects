import pickle 

class Vehicle:
    def __init__(self, VehicleID="", Registration="", DateOfRegistration=None, EngineSize=0,PurchasePrice=0.00):
        self.VehicleID = VehicleID
        self.Registration = Registration
        self.DateOfRegistration = DateOfRegistration
        self.EngineSize = EngineSize
        self.PurchasePrice = PurchasePrice

MyCar = Vehicle() #Created an instance of Vehicle

MyCar.VehicleID = "00100101"
MyCar.Registration = "PYT009"
MyCar.DateOfRegistration = "23/11/2023"
MyCar.EngineSize = 2500
MyCar.PurchasePrice = 21000.00



Cars = [Vehicle() for i in range(100)]
Cars[0].EngineSize = 2000

#Write to a binary file
CarFile = open("Cars.dat", "wb")
for item in Cars:
    pickle.dump(item, CarFile)
CarFile.close()


#Read from a binary file
CarFile = open("Cars.dat", "rb")
Car = []
count = 0
while count < 100:
    Car.append(pickle.load(CarFile))
    count += 1
CarFile.close()



JoWee = Vehicle()
JoWee.VehicleID = "00100102"
JoWee.Registration = "PYT010"
JoWee.DateOfRegistration = "23/11/2023"
JoWee.EngineSize = 2500
JoWee.PurchasePrice = 21000.00

#Write JoWee's car to a raddom file
CarFile = open("Cars2.dat", "wb")
Address = hash(JoWee.VehicleID)
CarFile.seek(Address)
pickle.dump(JoWee, CarFile)
CarFile.close()

#Find a car record using the VehicleID

CarFile = open("Cars2.dat", "rb")
Address = hash(JoWee.VehicleID)
CarFile.seek(Address)
JoWee = pickle.load(CarFile)
CarFile.close()

