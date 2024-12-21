# Returns a list of reports from a text file
def getFromFile(fileName):
    file = open(fileName, "r")

    reports = []

    for line in file:
        reports.append(line.rstrip().split(" "))
    
    file.close()

    return reports