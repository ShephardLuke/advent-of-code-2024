# Main method
def calibrationResultCalbulator():
    FILE_NAME = "input.txt"

    equations = getEquationsFromFile(FILE_NAME)

    print(sumEquations(equations))


# Returns total of all results that are valid
def sumEquations(equations):
    total = 0

    for equation in equations:
        results = applyOperations(equation.inputs, -1)
        if (results.count(equation.result)) > 0:
            total += equation.result
    
    return total


# Applies operations recursively by going to inputs[0] and then applying all operations to it with inputs[1] then those results to inputs[2] etc
def applyOperations(inputs, i):
    if i == -len(inputs):
        return [inputs[0]]
    
    results = []
    
    for result in applyOperations(inputs, i - 1):
        for operation in getOperators():
            results.append(runOperation(inputs[i], operation, result))
    
    return results


# Returns eqautions from a file
def getEquationsFromFile(fileName):
    equations = []

    file = open(fileName, "r")
    for line in file:
        parameters = line.rstrip().split(":")
        result = int(parameters[0])
        inputs = parameters[1].strip().split(" ")
        inputs = list(map(int, inputs))

        equations.append(createEquation(inputs, result))

    return equations


# Creates an equation
def createEquation(inputs, result):
    equation = Equation()
    equation.inputs = inputs
    equation.result = result

    return equation


# Returns all operators
def getOperators():
    return [
        "+",
        "*",
        "||"
    ]


# Runs the given string operation to both the parameters
def runOperation(num1, operator, num2):
    match operator:
        case "+":
            return num1 + num2
        case "*":
            return num1 * num2
        case "||":
            return int(str(num2) + str(num1))
    return -1


# Equation record
class Equation:
    inputs = []
    result = 0


calibrationResultCalbulator()