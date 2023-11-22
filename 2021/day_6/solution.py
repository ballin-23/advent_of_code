def readFile(path="input.txt"):
    with open(path, 'r') as file:
        lines = file.readlines()
        fish = lines[0].split(',')
        return stringArrToNumArr(fish)

def stringArrToNumArr(arr):
    return [int(x) for x in arr]

def simulateFish(fishList):
    fishToAdd = 0
    for i in range(len(fishList)):
        life = fishList[i]
        if life == 0:
            fishToAdd += 1
            fishList[i] = 6
        else:
            fishList[i] = fishList[i] - 1
    for i in range(fishToAdd):
        fishList.append(8)
    # print(fishList)
    return fishList


def calculateFishLifeExpectancy(days):
    initialState = readFile()
    for i in range(days):
        initialState = simulateFish(initialState)
    # print("final state")
    # print(initialState)
    print(len(initialState))

calculateFishLifeExpectancy(80)