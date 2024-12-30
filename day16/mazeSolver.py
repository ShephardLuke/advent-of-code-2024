def mazeSolver():
    FILE_NAME = "demoInput.txt"

    maze, start, end = getMazeFromFile(FILE_NAME)

    print(getLowestScoreRec(maze, start, end, end, end, {}, 0))

def getLowestScore(maze, start, end):
    pass

def getLowestScoreRec(maze, start, end, position, pastPosition, previous, depth):

    x, y = position
    pastX, pastY = pastPosition

    if start == (x, y):
        if pastY == y:
            return 0
        else:
            return 1000

    toCheck = [
        (x, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y),
    ]

    lowest = -1

    for i in range(len(toCheck)):
        checkX, checkY = toCheck[i]
        if inBounds(maze, checkX, checkY) and hash((checkX, checkY)) not in previous and maze[checkY][checkX] == ".":
            newPrevious = previous.copy()
            newPrevious[hash((checkX, checkY))] = True
            check = getLowestScoreRec(maze, start, end, (checkX, checkY), position, newPrevious, depth + 1)

            if check < 0:
                continue

            if (pastX == x and x == checkX) or (pastY == y and y == checkY):
                check += 1
            else:
                check += 1001


            if lowest == -1 or check < lowest:
                lowest = check

    return lowest


def inBounds(nestedArray, x, y):
    if x >= 0 and y >= 0 and y < len(nestedArray) and x < len(nestedArray[y]):
        return True

    return False

def getMazeFromFile(fileName):
    file = open(fileName, "r")

    maze = []
    start = None
    end = None
    
    y = 0
    for line in file:
        toAdd = list(line.rstrip())
        if start == None or end == None:
            for x in range(len(line)):
                char = line[x]
                if char == "S":
                    start = (x, y)
                    toAdd[x] = "."
                elif char == "E":
                    end = (x, y)
                    toAdd[x] = "."
            y += 1

        maze.append(toAdd)

    file.close()

    return maze, start, end

mazeSolver()