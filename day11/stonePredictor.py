# Main method
def stonePredictor():
    BLINKS = 25

    FILE_NAME = "input.txt"

    stones = getStonesFromFile(FILE_NAME)

    print(len(predictStonesMultiple(stones, BLINKS)))


# Returns new stones after x times blinked
def predictStonesMultiple(stones, times):
    newStones = stones

    for _ in range(times):
        newStones = predictStones(newStones)
    
    return newStones


# Returns new stones after 1 blink
def predictStones(stones):
    newStones = []

    for stone in stones:
        if stone == 0:
            newStones.append(1)
        elif len(str(stone)) % 2 == 0:
            stoneString = str(stone)
            stoneMiddle = int(len(stoneString) / 2)

            newStones.append(int(stoneString[:stoneMiddle:]))
            newStones.append(int(stoneString[stoneMiddle::])) 
        else:
            newStones.append(stone * 2024)

    return newStones


# Reads stones from file and returns them as an array of ints
def getStonesFromFile(fileName):
    file = open(fileName, "r")

    stones = file.read().rstrip().split(" ")
    stones = list(map(int, stones))

    return stones


stonePredictor()
