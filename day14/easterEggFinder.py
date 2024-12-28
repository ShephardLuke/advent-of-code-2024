from robot import createPosition, getRobotsFromFile, simulateRobots, saveGridToFile, getPosition, getX, getY

# Main method
def easterEggFinder():
    SPACE = createPosition(101, 103)
    SECONDS_TO_CHECK = 10000

    FILE_NAME = "input.txt"

    robots = getRobotsFromFile(FILE_NAME)

    longestRow = getLongestRowIteration(SPACE, robots, SECONDS_TO_CHECK)

    print(longestRow)

    displayEasterEgg(SPACE, FILE_NAME, longestRow)


# Displays the easter egg's iteration in output.txt
def displayEasterEgg(SPACE, fileName, iteration):
    outputRobots = getRobotsFromFile(fileName)
    simulateRobots(SPACE, outputRobots, iteration)

    saveGridToFile(SPACE, iteration, outputRobots)


# Returns the longest row in all of the given iterations
def getLongestRowIteration(SPACE, robots, simulationSeconds):
    longestRow = (-1, -1)
    for i in range(1, simulationSeconds + 1):

        simulateRobots(SPACE, robots, 1)

        rowData = getRowData(robots)

        currentLongest = getLongestRowData(rowData)

        if currentLongest > longestRow[1]:
            longestRow = (i, currentLongest)

    return longestRow[0]


# Returns the longest row when given a hashmap with y values as keys pointing to arrays of x values
def getLongestRowData(rowData):
    longestInARow = 0
    for row in list(rowData.keys()):
        data = rowData[row]
        data.sort()

        longestConsecutive = getMostConsecutive(data)

        if longestConsecutive > longestInARow:
            longestInARow = longestConsecutive
       
    return longestInARow


# Returns the number of most consecutive numbers in order in the array, e.g [1, 2, 3, 6, 7] would return 3
def getMostConsecutive(data):
    inARow = -1
    current = -1
    longestRow = -1

    for d in data:
        if current == -1:
            current = d
            inARow = 1
        else:
            if current + 1 == d:
                current = d
                inARow += 1
            else:
                if inARow > longestRow:
                    longestRow = inARow
                inARow = -1
                current = -1

    if inARow > longestRow:
        longestRow = inARow

    return longestRow


# Returns the robots positions as a hashmap with y keys pointing to arrays of x values
def getRowData(robots):
    rowData = {}

    for robot in robots:
        position = getPosition(robot)
        x = getX(position)
        y = getY(position)

        if y in rowData:
            rowData[y].append(x)
        else:
            rowData[y] = [x]

    return rowData


easterEggFinder()