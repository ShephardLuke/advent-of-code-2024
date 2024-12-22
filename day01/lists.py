# Returns two lists from a text file
def getFromFile(fileName):
    file = open(fileName, "r")
    list1 = []
    list2 = []

    for line in file:
        (input1, input2) = (line.rstrip().split("   "))
        list1.append(int(input1))
        list2.append(int(input2))
    
    file.close()

    return (list1, list2)