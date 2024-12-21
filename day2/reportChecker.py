import reports as r

# Main method
def reportChecker():
    PROBLEM_DAMPENER_ENABLED = True

    reports = r.getFromFile("input.txt")

    safeReports = 0

    if (PROBLEM_DAMPENER_ENABLED):
        safeReports = getSafeReports(reports, PROBLEM_DAMPENER_ENABLED)
    else:
        safeReports = getSafeReports(reports, False)
    
    print(safeReports)    


# Returns number of safe reports
def getSafeReports(reports, problem_dampener_enabled):
    safe = 0

    for report in reports:
        unsafeIndexes = getUnsafeIndexes(report)
        if len(unsafeIndexes) == 0:
            safe += 1
        elif problem_dampener_enabled:
            for index in unsafeIndexes: # Probably very inefficient but works and not many items anyway
                if len(getUnsafeIndexes(report[:index:] + report[index + 1::])) == 0:
                    safe += 1
                    break
    
    return safe


# Returns list with all incorrect indexes
def getUnsafeIndexes(report): 
    unsafeIndexes = []
    pastPattern = 0

    for i in range(len(report) - 1):
        current = int(report[i])
        next = int(report[i + 1])

        pattern = next - current

        if not validatePattern(pattern,  pastPattern):
            if (i > 0 and (len(unsafeIndexes) <= 1 or unsafeIndexes[-2] != i)):
                unsafeIndexes.append(i - 1)
            if (len(unsafeIndexes) == 0 or unsafeIndexes[-1] != i):
                unsafeIndexes.append(i)
            unsafeIndexes.append(i + 1)

        pastPattern = pattern

    return unsafeIndexes

# Returns true only if pattern is following the same trend as the previous pattern and the difference in patterns is between 1 and 3 inclusive
def validatePattern(pattern, pastPattern):
    if pattern == 0:
        return False
    if pattern < 0 and pastPattern > 0:
        return False
    if pattern > 0 and pastPattern < 0:
        return False
    
    difference = abs(pattern)

    if difference < 1 or difference > 3:
        return False
    
    return True

reportChecker()