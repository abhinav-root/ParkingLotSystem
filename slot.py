from vehicle import Vehicle


class Slot(Vehicle):
    def __init__(self, driverAge: int, registrationId: str, slotNumber: int):
        super().__init__(driverAge, registrationId)
        self.slotNumber = slotNumber

    def __str__(self):
        return f'Slot({self.slotNumber},{self.registrationId},{self.driverAge})'

    def getSlotNumber(self):
        return self.slotNumber
