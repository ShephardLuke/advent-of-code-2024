# Main method
def fencePriceCalculator():
    FILE_NAME = "input.txt"

    garden = readFromFile(FILE_NAME)

    print(getFencePrice(garden))


# Returns the price of all the fences for the garden 
def getFencePrice(garden):
    price = 0

    for y in range(len(garden)):
        for x in range(len(garden[y])):
            if not type(garden[y][x]) is int:
                details = getPlotDetails(garden, x, y, garden[y][x])
                price += details[0] * details[1]

    return price


# Adds up all the area and perimeters of the plots recursively and returns it as (area, perimeter)
def getPlotDetails(garden, x, y, label):
    if garden[y][x] != label:
        return (0, 0)

    total = (0, 0)

    toAdd = [
        (x - 1, y),
        (x, y - 1),
        (x + 1, y),
        (x, y + 1)
    ]

    garden[y][x] = ord(label)

    for pos in toAdd:
        result = checkSurroundingPlots(garden, pos, label)
        total = (total[0] + result[0], total[1] + result[1])

    return (total[0] + 1, total[1])


# Checks the surrounding plots, if they match then their plots are checked, but if they dont match the perimeter goes up. Returns in the form (area, perimeter)
def checkSurroundingPlots(garden, pos, label):

    if inBounds(garden, pos[0], pos[1]):
        if (garden[pos[1]][pos[0]] == ord(label)):
            return (0, 0)

        result = getPlotDetails(garden, pos[0], pos[1], label)

        if result == (0, 0):
            return (0, 1)
        
        return (result[0], result[1])
    
    return (0, 1)


# Returns true on if x and y are inside the nested array
def inBounds(nestedArray, x, y):
    return x >= 0 and y >= 0 and y <= len(nestedArray) - 1 and x <= len(nestedArray[y]) - 1


# Reads a garden from the given file and return it as a nested array
def readFromFile(fileName):
    file = open(fileName, "r")
    
    garden = []
    for line in file:
        garden.append(list(line.rstrip()))
    
    return garden


fencePriceCalculator()