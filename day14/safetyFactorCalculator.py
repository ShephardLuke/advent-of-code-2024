import math

# Main method
def safetyFactorCalculator():
    SPACE = createPosition(101, 103)
    SIMULATION_SECONDS = 100

    FILE_NAME = "input.txt"

    robots = getRobotsFromFile(FILE_NAME)

    simulateRobots(robots, SIMULATION_SECONDS)

    print(getSafetyFactor(SPACE, robots))


# Returns the safety factor of the robots
def getSafetyFactor(space, robots):
    x = getX(space)
    y = getY(space)
    gapX = math.floor(x / 2)
    gapY = math.floor(y / 2)

    total = [[0, 0], [0, 0]]

    for robot in robots:
        position = getPosition(robot)
        xInSpace = getX(position) % x
        yInSpace = getY(position) % y

        if xInSpace != gapX and yInSpace != gapY:
            total [math.floor(yInSpace / (y / 2))][math.floor(xInSpace / (x / 2))] += 1
    
    return multiplyNestedArray(total)


# Adds velocity * seconds to robots positions
def simulateRobots(robots, seconds):
    for robot in robots:
        position = getPosition(robot)
        velocity = getVelocity(robot)

        newPosition = createPosition(getX(position) + getX(velocity) * seconds, getY(position) + getY(velocity) * seconds)
        setPosition(robot, newPosition)


# Returns a list of robots from the given file
def getRobotsFromFile(fileName):
    file = open(fileName, "r")

    robots = []
    for line in file:
        paramters = line.rstrip().split(" ")

        position = getPositionFromString(paramters[0])
        velocity = getPositionFromString(paramters[1])
        robots.append(createRobot(position, velocity))
    
    file.close()

    return robots


# Turns a string p=x,y into a position where p is a letter and x and y are integers
def getPositionFromString(positionString):
    position = positionString.split(",")
    position[0] = position[0][position[0].index("=") + 1::]
    
    return createPosition(int(position[0]), int(position[1]))


# Returns all the items in the nested array multiplied together
def multiplyNestedArray(nestedArray):
    total = 1

    for y in nestedArray:
        for x in y:
            total *= x

    return total


# Returns a new robot
def createRobot(position, velocity):
    robot = Robot()
    robot.position = position
    robot.velocity = velocity

    return robot


# Sets position
def setPosition(robot, position):
    robot.position = position


# Returns position
def getPosition(robot):
    return robot.position


# Returns velocity
def getVelocity(robot):
    return robot.velocity


# Returns a new position
def createPosition(x, y):
    position = Position()
    position.x = x
    position.y = y

    return position


# Returns x
def getX(position):
    return position.x


# Returns y
def getY(position):
    return position.y


# Position record
class Position:
    x: int
    y: int


# Robot record
class Robot:
    position: Position
    velocity: Position


safetyFactorCalculator()