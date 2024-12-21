# Returns a program from a file
def getFromFile(fileName):
    file = open(fileName, "r")
    read =  file.read()
    file.close()
    return read

# Returns a list of all possible instructions and their number of arguments
def getInstructions():
    return [
        ("mul", 2),
        ("do", 0),
        ("don't", 0)
    ]
