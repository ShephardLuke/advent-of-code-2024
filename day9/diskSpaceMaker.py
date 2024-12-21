# Main method
def diskSpaceMaker():
    FILE_NAME = "input.txt"

    disk = getDiskFromFile(FILE_NAME)
    newDisk = fillDiskGaps(disk)
    
    print(getChecksum(newDisk))


# Returns the checksum of a disk which is the sum of multiplying each id by its position
def getChecksum(disk):
    checksum = 0

    for i in range(len(disk)):
        if disk[i] == ".":
            continue
        else:
            checksum += int(disk[i]) * i
    
    return checksum


# Fills in the gaps at the front of the disk by moving blocks from the back so all the free space is at the end
def fillDiskGaps(disk):
    leftPointer = 0
    rightPointer = -1
    newDisk = []
    freeDisk = []

    while leftPointer + abs(rightPointer) <= len(disk):
        if disk[leftPointer] != ".":
            newDisk.append(disk[leftPointer])
            leftPointer += 1
            continue
        if disk[rightPointer] == ".":
            freeDisk.append(".")
            rightPointer -= 1
            continue
        
        newDisk.append(disk[rightPointer])
        leftPointer += 1
        
        freeDisk.append(".")
        rightPointer -= 1

    return newDisk + freeDisk


# Gets a disk from a file as blocks in array format
def getDiskFromFile(fileName):
    file = open(fileName, "r")
    diskMap = file.read().rstrip()

    file.close()

    disk = []

    id = 0
    for i in range(len(diskMap)):
        mode = i % 2
        if mode == 0:
            appendMultiple(disk, str(id), int(diskMap[i]))
            id += 1
        else:
            appendMultiple(disk, ".", int(diskMap[i]))

    return disk


# Append multiple of an item to an array
def appendMultiple(array, toAdd, times):
    for _ in range(times):
        array.append(toAdd)


diskSpaceMaker()