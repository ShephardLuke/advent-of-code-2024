# Main method
def antinodeMapper():
    FILE_NAME = "input.txt"

    antennas, mapSize = getAntennasFromFile(FILE_NAME)

    antinodes = getAntinodes(antennas)

    antinodesInMap = getArrayInMap(antinodes, mapSize)

    print(len(antinodesInMap))

    outputAntinodesMap(antinodesInMap, antennas, mapSize)


# Outputs antinodes to output.txt in same format as the examples given
def outputAntinodesMap(antinodes, antennas, mapSize):
    file = open("output.txt", "w")

    map = []
    for y in range(mapSize[1]):
        toAdd = []
        for x in range(mapSize[0]):
            toAdd.append(".")
        map.append(toAdd)

    for frequency in list(antennas.keys()):
        for (x, y) in antennas[frequency]:
            map[y][x] = frequency


    for antinode in antinodes:
        map[antinode[1]][antinode[0]] = "#"
        

    for line in map:
        for char in line:
            file.write(char)
        file.write("\n")
    
    file.close()


# Returns an array with only the positions that are in the maps boundaries
def getArrayInMap(array, mapSize):
    newArray = []

    for (x, y) in array:
        if x >= 0 and y >= 0 and x < mapSize[0] and y < mapSize[1]:
            newArray.append((x, y))
    
    return newArray


# Calculates antinode positions for each frequency
def getAntinodes(antennas):
    antinodes = []

    frequencies = list(antennas.keys())

    for frequency in frequencies:
        antennaLocations = antennas[frequency]
        for (x1, y1) in antennaLocations:
            for (x2, y2) in antennaLocations:
                if (x1 == x2 and y1 == y2):
                    continue
                difference = (x1 - x2, y1 - y2)
                place1 = (x1 - difference[0], y1 - difference[1])
                place2 = (x1 + difference[0], y1 + difference[1])

                if antennaLocations.count(place1) == 0 and antinodes.count(place1) == 0:
                    antinodes.append(place1)

                if antennaLocations.count(place2) == 0 and antinodes.count(place2) == 0:
                    antinodes.append(place2)
    
    return antinodes


# Turns a map from the given file into a hashmap of frequencies -> positions
def getAntennasFromFile(fileName):
    file = open(fileName, "r")
    antennas = {}

    y = 0
    for line in file:
        line = line.rstrip()
        for x in range(0, len(line)):
            char = line[x]
            if char != ".":
                if char in antennas:
                    antennas[char].append((x, y))
                else:
                    antennas[char] = [(x, y)]
        y += 1

    mapSize = (x + 1, y)

    file.close()

    return antennas, mapSize


antinodeMapper()