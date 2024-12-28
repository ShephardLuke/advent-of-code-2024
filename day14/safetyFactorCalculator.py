from robot import createPosition, getRobotsFromFile, simulateRobots, saveGridToFile, getX, getY, getPosition, multiplyNestedArray
import math

# Main method
def safetyFactorCalculator():
    SPACE = createPosition(101, 103)
    SIMULATION_SECONDS = 100

    FILE_NAME = "input.txt"

    robots = getRobotsFromFile(FILE_NAME)
    simulateRobots(SPACE, robots, SIMULATION_SECONDS)

    print(getSafetyFactor(SPACE, robots))

    saveGridToFile(SPACE, SIMULATION_SECONDS, robots)


# Returns the safety factor of the robots
def getSafetyFactor(space, robots):
    x = getX(space)
    y = getY(space)
    gapX = math.floor(x / 2)
    gapY = math.floor(y / 2)

    total = [[0, 0], [0, 0]]

    for robot in robots:
        position = getPosition(robot)
        xInSpace = getX(position)
        yInSpace = getY(position)

        if xInSpace != gapX and yInSpace != gapY:
            total [math.floor(yInSpace / (y / 2))][math.floor(xInSpace / (x / 2))] += 1

    return multiplyNestedArray(total)


safetyFactorCalculator()