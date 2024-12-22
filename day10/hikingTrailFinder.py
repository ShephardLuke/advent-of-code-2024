# Main method
def hikingTrailFinder():
    FILE_NAME = "input.txt"
    
    trailMap = getMapFromFile(FILE_NAME)

    headLocations = getTrailHeadLocations(trailMap)

    foundEnds = getAllTrailEnds(trailMap, headLocations)

    print(len(foundEnds))


# Get the ends of all the valid trails
def getAllTrailEnds(trailMap, headLocations):
    foundEnds = []

    for location in headLocations:
        foundEnds += getTrailEnds(trailMap, location, 0)
    
    return foundEnds


# If target matches it recursively checks target + 1 in the 4 spaces around it. Returns an array of locations with 9 that are valid trails
def getTrailEnds(trailMap, location, target):
    END = 9
    x, y, = location

    if trailMap[y][x] == ".":
        return []
    
    current = int(trailMap[y][x])

    if current != target:
        return []
    if current == target and target == END:
        return [location]
    
    allFound = []

    newLocations = getNewLocations(trailMap, x, y)

    for newLocation in newLocations:
        found = getTrailEnds(trailMap, newLocation, target + 1)
        if len(found) != 0:
            for f in found:
                if allFound.count(f) == 0:
                    allFound.append(f)
    
    return allFound


# Returns all locations next to x, y that are on the map
def getNewLocations(trailMap, x, y):
    newLocations = []
    if x > 0:
        newLocations.append((x - 1, y))
    if x < len(trailMap[y]) - 1:
        newLocations.append((x + 1, y))
    if y > 0:
        newLocations.append((x, y - 1))
    if y < len(trailMap) - 1:
        newLocations.append((x, y + 1))
    
    return newLocations


# Returns all of the trail head locations
def getTrailHeadLocations(trailMap):
    TRAILHEAD = "0"

    locations = []

    for y in range(len(trailMap)):
        for x in range(len(trailMap[y])):
            if trailMap[y][x] == TRAILHEAD:
                locations.append((x, y))
    
    return locations


# Returns the file as a nested array of characters
def getMapFromFile(fileName):
    file = open(fileName, "r")
    lines = []

    for line in file:
        lines.append(list(line.rstrip()))
    
    return lines


hikingTrailFinder()