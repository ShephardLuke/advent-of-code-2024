# Main method
def guardPredictor():
    MODES = ["COUNT", "LOOPS"]
    SELECTED_MODE = MODES[1]

    FILE_NAME = "input.txt"

    lab = readFromFile(FILE_NAME)

    guard = removeGuard(lab)

    starting = getGuard(guard)

    simulateGuard(guard, lab)

    if SELECTED_MODE == MODES[0]:
            print(countDistinctPositions(lab))
    elif SELECTED_MODE == MODES[1]:
            print(len(findLoops(starting, lab)))

    writeOutput(lab)


# Writes lab to output.txt
def writeOutput(lab):
    file = open("output.txt", "w+")
    for line in lab:
        for char in line:
            file.write(char)
        file.write("\n")
    file.close()
                    

# Move the guard around the lab, marking their route in the lab array
def simulateGuard(guard, lab):
    nextX, nextY, direction = getGuard(guard)
    
    path = []

    while nextY >= 0 and nextX >= 0 and nextY < len(lab) and nextX < len(lab[nextY]):

        if lab[nextY][nextX] == "#":
            setGuardDirection(guard, (direction + 1) % 4)
            x, y, _ = getGuard(guard)
            lab[y][x] = "O"
            path.append((x, y, (direction + 1) % 4))
        else:
            if lab[nextY][nextX] == ".":
                lab[nextY][nextX] = getDirectionSymbol(direction)
                path.append((nextX, nextY, direction))
            setGuard(guard, nextX, nextY, direction)    

        nextX, nextY, direction = getForward(guard)


# find all of the loops along the guards path, add them to lab and return them, probably could be optimised a lot (it takes ages)
def findLoops(starting, lab):
    loops = []

    for y in range(len(lab)):
        for x in range(len(lab[y])):
            if ((y != starting[1] or x != starting[0]) and lab[y][x] != "#" and lab[y][x] != "."):
                temp = lab[y][x]
                lab[y][x] = "#"

                loop = isLoop(starting[0], starting[1], starting[2], lab)

                lab[y][x] = temp

                if loop != False:
                    loops.append((x, y))

    for loop in loops:
        lab[loop[1]][loop[0]] = "L"
    
    return loops


# True only if theres a loop in the lab
def isLoop(x, y, direction, lab):
    
    dummyGuard = createGuard(x, y, direction)
    nextX, nextY, direction = getGuard(dummyGuard)

    path = []

    while nextY >= 0 and nextX >= 0 and nextY < len(lab) and nextX < len(lab[nextY]):

        if path.count((nextX, nextY, direction)) > 0:
            path.append((nextX, nextY, direction))

            return True

        if lab[nextY][nextX] == "#":
            setGuardDirection(dummyGuard, (direction + 1) % 4)
            gX, gY, _ = getGuard(dummyGuard)
            path.append((gX, gY, (direction + 1) % 4))
        else:
            setGuard(dummyGuard, nextX, nextY, direction)
            path.append((nextX, nextY, direction))

        nextX, nextY, direction = getForward(dummyGuard)

    return False

        
# Returns symbol for given direction (0, 1, 2, 3)
def getDirectionSymbol(direction):
    match direction:
        case 0:
            return "^"
        case 1:
            return ">"
        case 2:
            return "v"
        case 3:
            return "<"


# Get the position of the space ahead of the guard
def getForward(guard):
    x, y, direction = getGuard(guard)

    match direction:
        case 0:
            y = y - 1
        case 1:
            x = x + 1
        case 2:
            y = y + 1
        case 3:
            x = x - 1

    return x, y, direction


# Returns count of a string inside a nested array
def countDistinctPositions(array):
    count = 0
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] != "#" and array[y][x] != ".":
                count += 1
    return count


# Removes the guard icon from the lab and replaces it with an X, returns the guard
def removeGuard(lab):

    guard = createGuard(0, 0, 0)

    for y in range(len(lab)):
        for x in range(len(lab[y])):
            match lab[y][x]:
                case "^":
                    setGuard(guard, x, y, 0)
                    lab[y][x] = getDirectionSymbol(0)
                case ">":
                    setGuard(guard, x, y, 1)
                    lab[y][x] = getDirectionSymbol(1)
                case "v":
                    setGuard(guard, x, y, 2)
                    lab[y][x] = getDirectionSymbol(2)
                case ">":
                    setGuard(guard, x, y, 3)
                    lab[y][x] = getDirectionSymbol(3)
    
    return guard


# Creating a guard
def createGuard(x, y, direction):
    guard = Guard()
    guard.x = x
    guard.y = y
    guard.direction = direction

    return guard


# Settings all of the values for a guard
def setGuard(guard, x, y, direction):
    guard.x = x
    guard.y = y
    guard.direction = direction


# Setting direction
def setGuardDirection(guard, direction):
    guard.direction = direction


# Getting all the values from the guard
def getGuard(guard):
    return guard.x, guard.y, guard.direction


# Getting lab from a file
def readFromFile(fileName):
    lab = []

    file = open(fileName)
    for line in file:
        lab.append(list(line.rstrip()))
    file.close()
    return lab


# Guard record
class Guard():
    x = 0
    y = 0
    direction = 0


guardPredictor()