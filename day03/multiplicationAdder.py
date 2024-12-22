import memory as m
import re

# Main method
def multiplicationAdder():
    FILE_NAME = "input.txt"

    memory = m.getFromFile(FILE_NAME)
    instructions = uncorruptMemory(memory)

    results = runInstructions(instructions)

    print(sumArray(results))


# Returns an array of all allowed instructions using regex
def uncorruptMemory(memory):

    return re.findall(getReString(), memory)


# Returns a regex string that allows only accepted instructions and their required parameters
def getReString():
    accepted = m.getInstructions()

    reString = ""

    for i in range(len(accepted)):
        (operation, arguments) = accepted[i]

        reString += operation + r"\("

        for j in range(arguments):
            reString += r"[0-9]*"
            if j != arguments - 1:
                reString += r","

        reString += r"\)"
        if i != len(accepted) - 1:
            reString += r"|"

    return reString


# Runs all of the instructions in the array and returns array of results
def runInstructions(instructions):
    results = []

    running = True
    for i in range(len(instructions)):
        current = instructions[i]
        operation = current[:current.index("("):]

        match operation:
            case "mul":
                if not running:
                    continue
                (a, b) = instructions[i].split(",")
                results.append(int(a[4::]) * int(b[:-1:]))
            case "do":
                running = True
            case "don't":
                running = False

    return results


# Adds up every item in an array
def sumArray(arr):
    total = 0

    for n in arr:
        total += n
    
    return total


multiplicationAdder()