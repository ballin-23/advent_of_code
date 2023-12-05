def readFile(path="input.txt"):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

def getSeeds(input):
    seeds = input[0].split(":")[1].split()
    return seeds

def getMaps(input):
    maps = []
    mapInput = input[2:]
    currentMap = []
    for line in mapInput:
        if line == "":
            maps.append(currentMap)
            currentMap = []
            continue
        else:
            currentMap.append(line)
    if currentMap != []:
        maps.append(currentMap)
    return maps

def createConversionDictionary(map):
    # destination, source, length
    mapping = {}
    for i in range(1,len(map)):
        destinationRange, sourceRange, rangeLength = convertLine(map[i])
        for j in range(rangeLength):
            if sourceRange+j not in mapping:
                mapping[sourceRange+j] = destinationRange + j
    # print("mapping: ", mapping)
    return mapping 


def convertLine(line):
    input = line.split()
    destinationRange = int(input[0])
    sourceRange = int(input[1])
    rangeLength = int(input[2])
    return destinationRange, sourceRange, rangeLength

def runTheConversion(seed, mapArr):
    changingSeed = seed
    for map in mapArr:
        if changingSeed in map:
            changingSeed = map[changingSeed]
    return changingSeed

def solvePart1():
    print("solving")
    input = readFile()
    seeds = getSeeds(input)
    maps = getMaps(input)
    print(maps)
    # conversionMapArr = []
    # locationNums = []
    # for map in maps:
    #     conversionMapArr.append(createConversionDictionary(map))
    # for seed in seeds:
    #     print("seed: ", seed)
    #     intSeed = int(seed)
    #     locationNums.append(runTheConversion(intSeed, conversionMapArr))
    # print("min: ",min(locationNums))
        

solvePart1()