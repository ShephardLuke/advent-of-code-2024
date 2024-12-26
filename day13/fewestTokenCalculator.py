# Main method
def fewestTokenCalculator():
    FILE_NAME = "input.txt"

    machines = getMachinesFromFile(FILE_NAME)

    print(getTotalPrice(machines))


# Returns total price of every machine
def getTotalPrice(machines):
    total = 0

    for machine in machines:
        total += getLowestPrice(machine)
    
    return total


# Gets lowest amount of tokens needed to win the prize
def getLowestPrice(machine):
    result1 = getLowestMultiple(machine.a.x, machine.b.x, machine.prize.x, machine.a.y, machine.b.y, machine.prize.y, 100)

    if result1 == (-1, -1):
        return 0

    result2 = getLowestMultiple(machine.b.x, machine.a.x, machine.prize.x, machine.b.y, machine.a.y, machine.prize.y, result1[1] - 1)

    prices = getButtonPrices()

    cost1 = result1[0] * prices[0] + result1[1] * prices[1]
    cost2 = result2[0] * prices[1] + result2[1] * prices[0]

    if result2 == (-1, -1):
        return cost1

    if cost1 <= cost2:
        return cost1

    return cost2


# Gets the lowest n that when multipled by m it will rusult in the goal
def getLowestMultiple(num1, num2, goal, otherNum1, otherNum2, otherGoal, max):
    for i in range(max + 1):
        result = (goal - (num1 * i)) / num2 

        if result < 0:
            return (-1, -1)
        
        otherResult = (otherGoal - (otherNum1 * i)) / otherNum2
  
        if result == otherResult:
            return (i, int(result))

    return (-1, -1)


# Returns an array of machines from the file given
def getMachinesFromFile(fileName):
    file = open(fileName, "r")

    machinesText = file.read().rstrip().split("\n\n")
    machines = []

    for machineInfo in machinesText:
        a, b, prize = machineInfo.split("\n")
        machine = Machine()

        machine.a = getPositionFromString(a, "+")
        machine.b = getPositionFromString(b, "+")
        machine.prize = getPositionFromString(prize, "=")

        machines.append(machine)

    return machines


# Turns a string X and Y into a position, using the breaker character
def getPositionFromString(string, breaker):
    broken = string.split(",")
    position = Position()

    broken[0] = broken[0][broken[0].index(breaker) + 1::]
    broken[1] = broken[1][broken[1].index(breaker) + 1::]
    
    position.x = int(broken[0])
    position.y = int(broken[1])

    return position


# Gets the prices of the buttons, a and b in order
def getButtonPrices():
    return [
        3,
        1,
    ]


# Position record
class Position:
    x: 0
    y: 0


# Machine record
class Machine:
    a: Position
    b: Position 
    prize = Position


fewestTokenCalculator()