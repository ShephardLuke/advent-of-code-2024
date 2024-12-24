# Main method
def stonePredictor():
    BLINKS = 75

    FILE_NAME = "input.txt"

    amounts = toHashmap(getStonesFromFile(FILE_NAME))

    newAmounts = predictStonesMultiple(amounts, BLINKS)

    print(getAmounts(newAmounts))


# Returns new stones after x times blinked
def predictStonesMultiple(amounts, times):
    for i in range(times):
        amounts = predictStones(amounts)
    return amounts


# Returns new stones after 1 blink
def predictStones(amounts):

    newAmounts = {}

    for stone in list(amounts):
        if stone == 0:
            addToAmounts(newAmounts, 1, amounts[stone])
        elif len(str(stone)) % 2 == 0:
            stoneString = str(stone)
            stoneMiddle = int(len(stoneString) / 2)

            addToAmounts(newAmounts, int(stoneString[:stoneMiddle:]), amounts[stone])
            addToAmounts(newAmounts, int(stoneString[stoneMiddle::]), amounts[stone])
        else:
            addToAmounts(newAmounts, stone*2024, amounts[stone])

    return newAmounts


# Returns the total of all the amounts
def getAmounts(amounts):
    total = 0
    for item in list(amounts):
        total += amounts[item]
    return total


# Adds a value to the amounts hashmap
def addToAmounts(amounts, item, amount):
    if item in amounts:
        amounts[item] += amount
    else:
        amounts[item] = amount


def toHashmap(array):
    items = {}

    for item in array:
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    
    return items


# Reads stones from file and returns them as an array of ints
def getStonesFromFile(fileName):
    file = open(fileName, "r")

    stones = file.read().rstrip().split(" ")
    stones = list(map(int, stones))

    return stones


stonePredictor()