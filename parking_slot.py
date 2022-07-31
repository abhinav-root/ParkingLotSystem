from slot import Slot


class ParkingLot:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.slots = [None] * capacity
        self.occupiedSlots = 0
        print(f'Created parking of {capacity} slots')

    def getNearestEmptySlot(self):
        if (self.isParkingFull()):
            print("Parking is full. No empty slots available")
            return None
        else:
            for index, slot in enumerate(self.slots):
                if slot is None:
                    return index

    def isParkingFull(self):
        return self.occupiedSlots == self.capacity

    def stats(self):
        print('-------------------------------')
        for slot in self.slots:
            print(slot)
        print('-------------------------------')

    def parkCar(self, registrationId: str, driverAge: int):
        emptySlotIndex = self.getNearestEmptySlot()
        slotNumber = emptySlotIndex + 1
        if emptySlotIndex is None:
            print("Cannot park. No parking slots available")
        else:
            self.slots[emptySlotIndex] = Slot(driverAge, registrationId,
                                              slotNumber)
            print(
                f"Car with vehicle registration number \"{registrationId}\" has been parked at slot number {slotNumber}"
            )

    def getSlotNumbersHavingDriversAge(self, age: int):
        result = ""
        for slot in self.slots:
            if slot is not None:
                slot.getDriverAge() == age
                result = result + str(slot.getSlotNumber()) + ","

        if (len(result) == 0):
            print(f"No vehicles found having driver age {age}")
        else:
            result = result[0:-1]
            print(result)

    def getSlotNumberByRegistrationId(self, registrationId: str):
        slot = -1
        for slot in self.slots:
            if slot is not None and slot.getRegistrationId() == registrationId:
                slot = slot.getSlotNumber()
                break

        if slot == -1:
            print(
                f"No slot number found with registration id \"{registrationId}\""
            )
        else:
            print(slot)

    def getSlotDetailsBySlotNumber(self, slotNumber: int):
        result = None
        for slot in self.slots:
            if slot is not None and slot.getSlotNumber() == slotNumber:
                result = slot
                break
        return result

    def clearSlot(self, slotNumber: int):
        slot = self.getSlotDetailsBySlotNumber(slotNumber)
        if slot is None:
            print("Slot already vacant")
        else:
            slotIndex = slotNumber - 1
            self.slots[slotIndex] = None
            print(
                f"Slot number 2 vacated, the car with vehicle registration number \"{slot.getRegistrationId()}\" left the space, the driver of the car was of age {slot.getDriverAge()}"
            )

    def getAllSlotsOccupiedByAge(self, age: int):
        slots = []
        for slot in self.slots:
            if slot is not None and slot.getDriverAge() == age:
                slots.append(slot)

        for slot in slots:
            print(
                f'Car with vehicle registration number \"{slot.getRegistrationId()}\" has been parked at slot number {slot.getSlotNumber()}'
            )
