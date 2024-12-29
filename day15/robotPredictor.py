# Main method
def robotPredictor():
    WIDER_WAREHOUSE = True
    FILE_NAME = "input.txt"
    
    robot, warehouse, instructions = getFromFile(FILE_NAME)
    
    if WIDER_WAREHOUSE:
        warehouse, robot = enlargeWarehouse(warehouse, robot)
    
    robot = simulateRobot(robot, warehouse, instructions)

    print(sumGPS(warehouse))

    outputWarehouse(warehouse, robot)


# Displays warehouse on output.txt
def outputWarehouse(warehouse, robot):
    file = open("output.txt", "w+")

    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if robot == (x, y):
                file.write(getIcons()["robot"])
            else:
                file.write(warehouse[y][x])
        file.write("\n")
    
    file.close()


# Returns the total of all the boxes GPS coordinates
def sumGPS(warehouse):
    total = 0
    icons = getIcons()

    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == icons["box"] or warehouse[y][x] == icons["wideBoxLeft"]:
                total += 100 * y + x
    
    return total


# Runs instructions on robot
def simulateRobot(robot, warehouse, instructions):
    for instruction in instructions:
        robot = runInstruction(robot, warehouse, instruction)

    return robot


# Runs on instruction on the robot then returns the new position
def runInstruction(robot, warehouse, instruction):
    newPosition = addDirectionToPosition(robot, instruction)
    if move(warehouse, newPosition, instruction):
        robot = newPosition
    
    return robot


# Returns True only when its a valid move for the robot even if boxes are pushed
def move(warehouse, position, direction):
    icons = getIcons()
    inFront = warehouse[position[1]][position[0]]

    if inFront == icons["empty"]:
        return True
    if isBox(inFront):
        canPush = canPushBox(warehouse, position, direction)
        if canPush == False:
            return False

        for info in (canPush[0] + canPush[1]):
            warehouse[info[0][1]][info[0][0]] = info[1]
        return True
    if inFront == icons["wall"]:
        return False
    

# Checks if this box can be pushed by making sure any boxes in front can also be pushed (recursively)
# If the box takes up 2 spaces everything above the other side is checked as well
# Returns a nested array in the format [[toRemove], [toAdd]] where each is a position and icon to remove and add from the warehouse
# Returns False if box cannot be pushed
def canPushBox(warehouse, position, direction, otherSide=False):
    newPosition = addDirectionToPosition(position, direction)

    icons = getIcons()
    icon = warehouse[position[1]][position[0]]

    if not inBounds(warehouse, newPosition) or warehouse[newPosition[1]][newPosition[0]] == icons["wall"]:
        return False

    toRemove = [(position, icons["empty"])]
    toAdd = [(newPosition, icon)]

    next = [[], []]

    if isWideBox(icon) and (direction == 0 or direction == 2) and not otherSide:
        next = canPushBox(warehouse, getOtherBoxPosition(icon, position), direction, otherSide=True)
        if next == False:
            return False
        
    if warehouse[newPosition[1]][newPosition[0]] == icons["empty"]:
        return (toRemove + next[0], toAdd + next[1])
    
    canPush = canPushBox(warehouse, newPosition, direction)
    if canPush == False:
        return False

    return (toRemove + next[0] + canPush[0], toAdd + next[1] + canPush[1])


# Enlarges the warehouse by making everything double length
def enlargeWarehouse(warehouse, robot):
    newWarehouse = []
    for y in range(len(warehouse)):
        toAdd = []
        for x in range(len(warehouse[y])):
            for icon in enlargeIcon(warehouse[y][x]):
                toAdd.append(icon)
        newWarehouse.append(toAdd)
    
    robot = (robot[0] * 2, robot[1])
 
    return newWarehouse, robot


# Turns an icon into a icon with length of 2
def enlargeIcon(icon):
    icons = getIcons()
    if icon == icons["box"]:
        return icons["wideBoxLeft"] + icons["wideBoxRight"]
    return icon + icon


# Returns position for other side of the box
def getOtherBoxPosition(icon, position):
    icons = getIcons()
    if icon == icons["wideBoxLeft"]:
        return (position[0] + 1, position[1])
    if icon == icons["wideBoxRight"]:
        return (position[0] - 1, position[1])


# Returns True if the icon is a box
def isBox(icon):
    icons = getIcons()
    return icon == icons["box"] or isWideBox(icon)


# Returns True only when the icon is a wide box
def isWideBox(icon):
    icons = getIcons()
    return icon == icons["wideBoxLeft"] or icon == icons["wideBoxRight"]


# Returns True only when the position in the given nested array
def inBounds(nestedArray, position):
    if position[0] >= 0 and position[1] >= 0 and position[1] < len(nestedArray) and position[0] < len(nestedArray[position[1]]):
        return True
    return False


# Returns position with 1 place moved in the given direction
def addDirectionToPosition(position, direction):
    match direction:
        case 0:
            return (position[0], position[1] - 1)
        case 1:
            return (position[0] + 1, position[1])
        case 2:
            return (position[0], position[1] + 1)
        case 3:
            return (position[0] - 1, position[1])


# All icons in the map
def getIcons():
    return {
        "box": "O",
        "wideBoxLeft": "[",
        "wideBoxRight": "]",
        "wall": "#",
        "empty": ".",
        "robot": "@"
    }


# Returns robot, warehouse, instructions from file as a tuple for position, array of icons and array of directions respectively
def getFromFile(fileName):
    file = open(fileName, "r")

    warehouse = []
    instructions = []
    robot = (-1, -1)
    
    gettingMap = True

    y = 0
    for line in file:
        chars = list(line.rstrip())

        if len(chars) == 0:
            gettingMap = False
            continue

        if gettingMap:
            if robot == (-1, -1):
                robot = checkForRobot(chars, y)

            warehouse.append(chars)
            y += 1
        else:
            for char in chars:
                instructions.append(arrowToDirection(char))

    file.close()
        
    return robot, warehouse, instructions


# Checks array of characters/icons, if it matches the robot's icon the robots position becomes the position of the icon
def checkForRobot(chars, y):
    robot = (-1, -1)
    icons = getIcons()
    for x in range(len(chars)):
        if chars[x] == icons["robot"]:
            chars[x] = icons["empty"]
            robot = (x, y)
        
    return robot


# Returns direction from given arrow, 0, 1, 2, 3 is always up, right, down, left respectively (clockwise)
def arrowToDirection(arrow):
    match arrow:
        case "^":
            return 0
        case ">":
            return 1
        case "v":
            return 2
        case "<":
            return 3
                    

robotPredictor()