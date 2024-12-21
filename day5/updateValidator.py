import math

# Main method
def updateValidator():
    MODE = ["GET VALID UPDATES", "CORRECT INVALID UPDATES"]
    SELECTED_MODE = MODE[1]

    FILE_NAME = "input.txt"

    rulesArray, updatesArray = readFromFile(FILE_NAME)

    rules = createRulesFromArray(rulesArray)

    validUpdates, invalidUpdates = getValidUpdates(updatesArray, rules)

    if (SELECTED_MODE == MODE[0]):
        print(sumMiddle(validUpdates))
    elif (SELECTED_MODE == MODE[1]):
        correctedUpdates = getCorrectedUpdates(invalidUpdates, rules)
        print(sumMiddle(correctedUpdates))


# Returns all of the invalid updates corrected
def getCorrectedUpdates(invalidUpdates, rules):
    correctedUpdates = []

    for update in invalidUpdates:
        correctedUpdates.append(correctUpdate(update, rules))
    
    return correctedUpdates


# Corrects an update by moving any later dependencies before the page that requires it
def correctUpdate(update, rules):
    correctedUpdate = []

    done = {}
    contains = {}

    for page in update:
        contains[page] = True

    for page in update:
        if page in done:
            continue

        addDependencies(correctedUpdate, page, rules, done, contains)

        correctedUpdate.append(page)
        done[page] = True

    return correctedUpdate


# Adds a dependency by recursively checking if its dependency needs some added first
def addDependencies(correctedUpdate, d, rules, done, contains):
    if d not in rules:
        return

    for dependency in rules[d]:
        if dependency in contains and dependency not in done:
            addDependencies(correctedUpdate, dependency, rules, done, contains)
            correctedUpdate.append(dependency)
            done[dependency] = True


# Returns only the updates that are valid
def getValidUpdates(updates, rules):
    valid = []
    invalid = []

    for update in updates:
        if isValidUpdate(update, rules):
            valid.append(update)
        else:
            invalid.append(update)

    return (valid, invalid)


# Checks if an update is valid by making sure all dependencies are before it
def isValidUpdate(update, rules):
    done = {}
    contains = {}

    for page in update:
        contains[page] = True

    for page in update:
        if page in rules:
            for dependency in rules[page]:
                if dependency in contains and dependency not in done:
                    return False
        done[page] = True
    
    return True


# Takes in a list of rules and returns them as a hashmap as page -> [dependencies]
def createRulesFromArray(rulesList):
    SPLIT_CHARACTER = "|"
    rules = {}

    for rule in rulesList:
        split = rule.index(SPLIT_CHARACTER)
        dependency = rule[:split:]
        page = rule[split + 1::]
        
        if page in rules:
            rules[page].append(dependency)  
        else:
            rules[page] = [dependency]
    
    return rules


# Opens the file with the given name and returns an array of rules and updates
def readFromFile(fileName):
    file = open(fileName, "r")
    noLinesFile = file.read().split("\n")

    split = noLinesFile.index("")

    rules = noLinesFile[:split:]

    updates = noLinesFile[noLinesFile.index("") + 1:-1:]

    file.close()

    for i in range(len(updates)):
        updates[i] = updates[i].split(",")


    return (rules, updates)


# Returns the sum of the middle of each inner array
def sumMiddle(nestedArray):
    total = 0
    for arr in nestedArray:
        total = total + int(arr[math.floor(len(arr) / 2)])
    return total

updateValidator()