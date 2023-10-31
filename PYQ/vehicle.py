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
