# Displays the grid to output.txt with a label saying the iteration and each point showing how many robots are on it
def saveGridToFile(space, iteration, robots):
    file = open("output.txt", "w+")
    spaceGrid = []
    for y in range(getY(space)):
        toAdd = []
        for x in range(getX(space)):
            toAdd.append(0)
        spaceGrid.append(toAdd)

    for robot in robots:
        position = getPosition(robot)

        spaceGrid[getY(position)][getX(position)] += 1
    
    file.write("Iteration: " + str(iteration)+ "\n")
    for y in spaceGrid:
        for x in y:
            toWrite = "."
            if x != 0:
                toWrite = str(x)
            file.write(toWrite)
        
        file.write("\n")
    
    file.close()


# Adds velocity * seconds to robots positions and contains it to the given space
def simulateRobots(SPACE, robots, seconds):
    
    for robot in robots:
        position = getPosition(robot)
        velocity = getVelocity(robot)

        newX = getX(position) + getX(velocity) * seconds
        newY = getY(position) + getY(velocity) * seconds

        newX = newX % getX(SPACE)
        newY = newY % getY(SPACE)

        newPosition = createPosition(newX, newY)
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
