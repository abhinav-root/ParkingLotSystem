from executor import commandExecutor

parkingLot = None


def startParkingSystem():
    inputFile = open("input.txt", "r")
    for line in inputFile:
        commandExecutor(line)
    inputFile.close()


def main():
    startParkingSystem()


if __name__ == "__main__":
    main()
