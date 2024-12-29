# Main method
def robotPredictor():
    FILE_NAME = "input.txt"
    
    robot, warehouse, instructions = getFromFile(FILE_NAME)
    
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
            if warehouse[y][x] == icons["box"]:
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
    if canMove(warehouse, newPosition, instruction):
        robot = newPosition
    
    return robot


# Returns True only when its a valid move for the robot
def canMove(warehouse, position, direction):
    icons = getIcons()
    inFront = warehouse[position[1]][position[0]]

    if inFront == icons["empty"]:
        return True
    if inFront == icons["box"]:
        return pushBox(warehouse, position, direction)
    if inFront == icons["wall"]:
        return False
    

# Recursively pushes boxes, if all cannot be pushed it will return False otherwise True and they all get pushed
def pushBox(warehouse, position, direction):
    newPosition = addDirectionToPosition(position, direction)
    icons = getIcons()

    if not inBounds(warehouse, newPosition) or warehouse[newPosition[1]][newPosition[0]] == icons["wall"]:
        return False
    
    if warehouse[newPosition[1]][newPosition[0]] == icons["empty"]:
        warehouse[newPosition[1]][newPosition[0]] = icons["box"]
        warehouse[position[1]][position[0]] = icons["empty"]
        return True
    
    if pushBox(warehouse, newPosition, direction):
        warehouse[newPosition[1]][newPosition[0]] = icons["box"]
        warehouse[position[1]][position[0]] = icons["empty"]
        return True
    
    return False


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
            robot = (y, x)
        
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