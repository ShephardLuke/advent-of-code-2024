import lists

# Main method
def similarityScoreCalculator():
    (list1, list2) = lists.getFromFile("inputs.txt")

    frequencies = calculateFrequencies(list2)

    print(getSimilarityScore(list1, frequencies))


# Returns a score based on how many of each item appear in the frequencies hashmap
def getSimilarityScore(li, frequencies):
    similarityScore = 0

    for item in li:
        if item in frequencies:
            similarityScore += item * frequencies[item]
    
    return similarityScore


# Returns a hashmap holding the numbers of each distinct item in the given list
def calculateFrequencies(li):
    frequencies = {}

    for item in li:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1

    return frequencies

similarityScoreCalculator()