import lists

# Main method
def totalDistanceCalculator():
    (list1, list2) = lists.getFromFile("input.txt")

    list1.sort()
    list2.sort()

    print(getTotalDistance(list1, list2))


# Returns a sum of the distances between each item in the lists in order
def getTotalDistance(list1, list2):
    totalDistance = 0

    for i in range(len(list1)):
        input1 = list1[i]
        input2 = list2[i]

        totalDistance += abs(input1 - input2)

    return totalDistance

    


        
totalDistanceCalculator()