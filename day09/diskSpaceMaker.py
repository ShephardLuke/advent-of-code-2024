# Main method
def diskSpaceMaker():
    FRAGMENTATION_ENABLED = False

    FILE_NAME = "input.txt"

    disk = getDiskFromFile(FILE_NAME)
    fillDiskGaps(disk, FRAGMENTATION_ENABLED)

    print(getChecksum(disk))


# Returns the checksum of a disk which is the sum of multiplying each id by its position
def getChecksum(disk):
    checksum = 0

    for i in range(len(disk)):
        if disk[i] == ".":
            continue
        else:
            checksum += int(disk[i]) * i
    
    return checksum


# Fills in the gaps at the front of the disk by checking if files at the back can fit in the front gaps
def fillDiskGaps(disk, fragmentation):
    leftPointer = 0
    rightPointer = -1

    freeSpaces = getFreeSpaces(disk)

    blocksToMove = (-1, 0)

    while leftPointer + abs(rightPointer) <= len(disk):
        if disk[leftPointer] != ".":
            leftPointer += 1
            continue
    
        if disk[rightPointer] == ".":
            if blocksToMove[1] == 0:
                rightPointer -= 1
                continue
        else:
            if blocksToMove[1] == 0:
                blocksToMove = (int(disk[rightPointer]), 1)
                rightPointer -= 1
                continue
            elif not fragmentation and blocksToMove[0] == int(disk[rightPointer]): 
                blocksToMove = (blocksToMove[0], blocksToMove[1] + 1)
                rightPointer -= 1
                continue
        
        lookForFreeSpace(disk, freeSpaces, len(disk) - abs(rightPointer), blocksToMove[0], blocksToMove[1])
        
        blocksToMove = (-1, 0)


# Tries to find a free space in front of the file, if so then it gets moved
def lookForFreeSpace(disk, freeSpaces, fileIndex, fileId, totalBlocks):
    for i in range(len(freeSpaces)):
        index, spaces = freeSpaces[i]
        if index < fileIndex and spaces >= totalBlocks:
            moveFile(disk, fileId, totalBlocks, fileIndex, index)
            freeSpaces[i] = (index + totalBlocks, spaces - totalBlocks)
            break


# Moves file to new index, deleting it from the old place on the disk
def moveFile(disk, fileId, totalBlocks, OldStartIndex, newStartIndex):
    for j in range(totalBlocks):
        disk[newStartIndex + j] = fileId
        disk[OldStartIndex + 1 + j] = "."


# Returns free spaces on the disk in the format (index, number of spaces)
def getFreeSpaces(disk):
    freeSpaces = []

    found = (-1, 0)
    for i in range(len(disk)):
        if disk[i] == ".":
            if found[0] == -1:
                found = (i, found[1])
            found = (found[0], found[1] + 1)
        else:
            if found != (-1, 0):
                freeSpaces.append(found)
                found = (-1, 0)
    
    return freeSpaces


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