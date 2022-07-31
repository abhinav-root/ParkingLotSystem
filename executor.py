from parking_slot import ParkingLot


def commandExecutor(command):
    global parkingLot
    args = command.split()
    command = args[0]
    if command == "Create_parking_lot":
        capacity = int(args[1])
        parkingLot = ParkingLot(capacity)

    elif command == 'Park':
        registrationId = args[1]
        driverAge = args[3]
        parkingLot.parkCar(registrationId, driverAge)

    elif command == "Slot_numbers_for_driver_of_age":
        age = args[1]
        parkingLot.getSlotNumbersHavingDriversAge(age)

    elif command == "Slot_number_for_car_with_number":
        registrationId = args[1]
        parkingLot.getSlotNumberByRegistrationId(registrationId)

    elif command == "Leave":
        slotNumber = int(args[1])
        parkingLot.clearSlot(slotNumber)

    elif command == "Vehicle_registration_number_for_driver_of_age":
        age = int(args[1])
        parkingLot.getAllSlotsOccupiedByAge(age)

    else:
        print(f"Invalid command {command}")

    # if parkingLot is not None:
    #     parkingLot.stats()
