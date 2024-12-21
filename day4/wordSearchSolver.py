# Main method
def wordSearchSolver():
    PUZZLE_TYPES = ["XMAS", "X-MAS"]
    SELECTED_PUZZLE_TYPE = PUZZLE_TYPES[1]

    PUZZLE_ALGORITHMS = [defaultCheck, xCheck]
    PUZZLE_TERMS= ["XMAS", "MAS"]

    FILE_NAME = "input.txt"

    wordSearch = readFromFile(FILE_NAME)

    print(getCount(wordSearch, PUZZLE_TERMS[PUZZLE_TYPES.index(SELECTED_PUZZLE_TYPE)], PUZZLE_ALGORITHMS[PUZZLE_TYPES.index(SELECTED_PUZZLE_TYPE)]))


# Returns number of matches for the term in the word search
def getCount(wordSearch, term, checkAlgorithm):
    count = 0
    for y in range(len(wordSearch)):
        for x in range(len(wordSearch[y])):
            count += checkAlgorithm(term, wordSearch, y, x)
    return count
            

# Word search check, returns how many matches. Can be horizontal, vertical and diagonal while being forwards or backwards
def defaultCheck(term, wordSearch, y, x):
    matches = 0

    length = len(term)
    toCheck = []

    if (x + length <= len(wordSearch[y])):
        toCheck.append(wordSearch[y][x:x+length:])

    if (y + length <= len(wordSearch)):
        word = ""
        for row in wordSearch[y:y+length:]:
            word += row[x]
        toCheck.append(word)
    
    if (x + length <= len(wordSearch[y]) and y + length <= len(wordSearch)):
        word = ""
        for j in range(length):
            word += wordSearch[y + j][x + j]
        toCheck.append(word)
    
    if (x - length >= -1 and y + length <= len(wordSearch)):
        word = ""
        for j in range(length):
            word += wordSearch[y + j][x - j]
        toCheck.append(word)
    
    
    for check in toCheck:
        if matchesTerm(check, term):
            matches += 1

    return matches


# Checks if term is in an x shape, forwards or backwards
def xCheck(term, wordSearch, y, x):

    matches = 0

    length = len(term)

    if (x + length <= len(wordSearch[y]) and y + length <= len(wordSearch)):
        word = ""
        for j in range(length):
            word += wordSearch[y + j][x + j]

        if matchesTerm(word, term):
            word = ""
            for j in range(length):
                word += wordSearch[y + length - 1 - j][x + j]
            if (matchesTerm(word, term)):
                matches += 1

    return matches


# Returns if a string matches a term forwards or backwards
def matchesTerm(string, term):
    return string == term or string[::-1] == term 


# Reads a file and returns an array of all the lines (how a word search is implemented in this program)
def readFromFile(fileName):
    lines = []
    file = open(fileName, "r")
    for line in file:
        lines.append(line.rstrip())
    return lines


wordSearchSolver()