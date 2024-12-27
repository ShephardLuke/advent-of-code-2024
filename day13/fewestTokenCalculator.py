import math

# Main method
def fewestTokenCalculator():
    PRIZE_MODIFIER = 10000000000000

    FILE_NAME = "input.txt"

    machines = getMachinesFromFile(FILE_NAME)
    applyModifier(machines, PRIZE_MODIFIER)

    print(getTotalPrice(machines))


# Returns total price of every machine
def getTotalPrice(machines):
    total = 0

    for machine in machines:
        lowest = getLowestPrice(machine)
        if (lowest != -1):
            total += lowest
    
    return total


# Gets lowest amount of tokens needed to win the prize
def getLowestPrice(machine):
    a = getA(machine)
    b = getB(machine)
    prize = getPrize(machine)

    resultAB = getLowestMultiple(a, b, prize)

    resultBA = getLowestMultiple(b, a, prize)

    prices = getButtonPrices()

    cost1 = resultAB[0] * prices[0] + resultAB[1] * prices[1]
    cost2 = resultBA[0] * prices[1] + resultBA[1] * prices[0]

    if resultAB == (-1, -1) and resultBA == (-1, -1):
        return -1

    if resultAB == (-1, -1):
        return cost2

    if resultBA == (-1, -1):
        return cost1

    if cost1 <= cost2:
        return cost1

    return cost2


# Logarithmically gets the lowest n in (n, m) where n and m are positive integers and when multiplied give the prize
def getLowestMultiple(button, otherButton, prize):

    x = getX(button)
    otherX = getX(otherButton)
    y = getY(button)
    otherY = getY(otherButton)

    prizeX = getX(prize)
    prizeY = getY(prize)

    min = 0
    max = math.ceil(prizeX / x)
    mid = math.floor(min + ((max - min) / 2))
    
    best = (-1, -1)
    while min <= max:
        result = (prizeX - (x * mid)) / otherX 
        otherResult = y * mid + otherY * result

        min, max = getNewMinMax(min, max, mid, otherResult, prizeY)

        if result == math.floor(result) and otherResult == float(prizeY):
            best = (mid, int(result))

        mid = math.floor(min + ((max - min) / 2))

    return best


# Returns an array of machines from the file given
def getMachinesFromFile(fileName):
    file = open(fileName, "r")

    machinesText = file.read().rstrip().split("\n\n")
    file.close()

    machines = []

    for machineInfo in machinesText:
        a, b, prize = machineInfo.split("\n")

        machine = createMachine(
            getPositionFromString(a, "+"),
            getPositionFromString(b, "+"),
            getPositionFromString(prize, "=")
        )

        machines.append(machine)

    return machines


# Changes max or min so the next result will be closer to the prize
def getNewMinMax(min, max, mid, result, prize):
    if result < prize:
        max = mid - 1
    else:

        min = mid + 1
    return min, max


# Adds the modifier to the prize of each machine
def applyModifier(machines, modifier):
    for machine in machines:
        prize = getPrize(machine)
        newPosition = createPosition(getX(prize) + modifier, getY(prize) + modifier)
        
        setPrize(machine, newPosition)


# Turns a string X and Y into a position, using the breaker character
def getPositionFromString(string, breaker):
    broken = string.split(",")

    position = createPosition(
        int(broken[0][broken[0].index(breaker) + 1::]),
        int(broken[1][broken[1].index(breaker) + 1::])
    )

    return position


# Creating a machine
def createMachine(a, b, prize):
    machine = Machine()
    machine.a = a
    machine.b = b
    machine.prize = prize

    return machine


# Getting A
def getA(machine):
    return machine.a


# Getting B
def getB(machine):
    return machine.b


# Setting the prize
def setPrize(machine, prize):
    machine.prize = prize


# Getting the prize
def getPrize(machine):
    return machine.prize


# Creating a position
def createPosition(x, y):
    position = Position()
    position.x = x
    position.y = y

    return position


# Getting X
def getX(position):
    return position.x


# Getting Y
def getY(position):
    return position.y


# Gets the prices of the buttons, a and b in order
def getButtonPrices():
    return [
        3,
        1,
    ]


# Position record
class Position:
    x: int
    y: int


# Machine record
class Machine:
    a: Position
    b: Position
    prize = Position


fewestTokenCalculator()