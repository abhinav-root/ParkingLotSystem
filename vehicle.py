class Vehicle:
    def __init__(self, driverAge: int, registrationId: str):
        self.driverAge = driverAge
        self.registrationId = registrationId

    def getDriverAge(self):
        return self.driverAge

    def getRegistrationId(self):
        return self.registrationId
