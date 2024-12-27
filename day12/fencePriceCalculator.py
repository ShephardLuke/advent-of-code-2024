# Main method
def fencePriceCalculator():
    BULK_DISCOUNT_ENABLED = True

    FILE_NAME = "input.txt"

    garden = readFromFile(FILE_NAME)

    print(getFencePrice(garden, BULK_DISCOUNT_ENABLED))


# Returns the number of sides from an array of points that share one axis
def getSides(array, sharedAxis):
    sameAxis = getSameAxis(array, sharedAxis)

    sides = 0
    
    for i in list(sameAxis.keys()):
        array = sameAxis[i]
        array.sort()

        sides += getGroups(array)

    return sides


# Returns a hashmap with all the shared axis of each point being the key and the other value being the value, so [(1, 2), (3, 2), (5, 6)], 1 would return {2: [1, 3], 6: [5]}
def getSameAxis(array, sharedAxis):
    sameAxis = {}
    
    for item in array:
        value = item[sharedAxis]
        otherAxis = (sharedAxis + 1) % 2
        if value in sameAxis:
            sameAxis[value].append(item[otherAxis])
        else:
            sameAxis[value] = [item[otherAxis]]

    return sameAxis


# Takes a sorted array and returns how many sections of consecutive numbers there are, for example [1, 2, 3, 5, 6] would return 2
def getGroups(sortedArray):
    pointer = sortedArray[0]
    groups = 1

    for item in sortedArray:
        if item == pointer:
            pointer += 1
        else:
            pointer = item
            pointer += 1
            groups += 1
    
    return groups


# Returns the price of all the fences for the garden 
# When bulk discount is enabled all the sides get calculated otherwise its just the count of the edges
def getFencePrice(garden, bulkDiscountEnabled):
    price = 0

    for y in range(len(garden)):
        for x in range(len(garden[y])):
            if not type(garden[y][x]) is int:
                details = getPlotDetails(garden, x, y, garden[y][x])

                if bulkDiscountEnabled:
                    sides = 0
                    for i in range(len(details[1])):
                        sides += getSides(details[1][i], (i + 1) % 2)
                    price += details[0] * sides
                else:
                    price += details[0] * lenNestedArray(details[1])

    return price


# Adds up all the area and get the edges of the plots recursively and returns it as (area, edges)
# Edges is an array [[], [], [], []] filled with which plots have an edge in that direction
# Direction is always top, right, bottom, left (clockwise)
def getPlotDetails(garden, x, y, label):
    if not inBounds(garden, x, y) or garden[y][x] != label:
        return (0,  [[], [], [], []])

    toAdd = [
        (x, y - 1),
        (x + 1, y),
        (x, y + 1),
        (x - 1, y)
    ]

    garden[y][x] = ord(garden[y][x])

    totalArea, totalEdges = getTotals(garden, x, y, label, toAdd)

    return (totalArea + 1, totalEdges)


# Returns totals of area and edges for the new edges that get checked
def getTotals(garden, x, y, label, toAdd):

    edges = getEdges(garden, label, toAdd)

    totalEdges = [[], [], [], []]
    totalArea = 0

    for i in range(len(edges)):
        if edges[i]:
            totalEdges[i].append((x, y))
        else:
            next = getPlotDetails(garden, toAdd[i][0], toAdd[i][1], label)
            totalArea += next[0]
            for j in range(len(next[1])):
                totalEdges[j] += next[1][j]
    
    return (totalArea, totalEdges)


# Returns a boolean array of which side has edges
def getEdges(garden, label, toAdd):
    edges = []

    for i in range(len(toAdd)):
        edges.append(isEdge(garden, toAdd[i][0], toAdd[i][1], label))
    
    return edges


# Returns False only when this plot has the same label as the plot thats checking it
def isEdge(garden, toCheckX, toCheckY, label):

    if inBounds(garden, toCheckX, toCheckY):
        if garden[toCheckY][toCheckX] != label and garden[toCheckY][toCheckX] != ord(label):
            return True

        return False
    
    return True


# Reads a garden from the given file and return it as a nested array
def readFromFile(fileName):
    file = open(fileName, "r")
    
    garden = []
    for line in file:
        garden.append(list(line.rstrip()))
    
    file.close()
    
    return garden


# Returns the total length of all the subarrays
def lenNestedArray(array):
    totalLen = 0
    for y in range(len(array)):
        totalLen += len(array[y])
    return totalLen


# Returns true on if x and y are inside the nested array
def inBounds(nestedArray, x, y):
    return x >= 0 and y >= 0 and y <= len(nestedArray) - 1 and x <= len(nestedArray[y]) - 1


fencePriceCalculator()