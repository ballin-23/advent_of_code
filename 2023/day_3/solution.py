def readFile(path):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

# function to create initial matrix
def createMatrix(input):
    matrix = []
    for line in input:
        lineArr = []
        for char in line:
            lineArr.append(char)
        matrix.append(lineArr)
    return matrix

# takes in the matrix and the known coordinates of a number adjacent to a star
def extractNumber(matrix, i, j):
    coords = [[i,j]]
    searchRight = True
    searchLeft = True
    copyJ = j
    while searchRight:
        j += 1
        if j < len(matrix[i]):
            char = matrix[i][j]
            # print("char found to right = ", char)
            if char.isdigit():
                coords.append([i,j])
            else:
                searchRight = False
        else:
            searchRight = False
    while searchLeft:
        copyJ -= 1
        if copyJ >= 0:
            char = matrix[i][copyJ]
            # print("char found to left = ", char)
            if char.isdigit():
                coords.append([i,copyJ])
            else:
                searchLeft = False
        else:
            searchLeft = False
    # print("coords: ",coords)
    return coords

def isDuplicateCoord(coords, currentCoords):
    for coordinate in currentCoords:
        if coordinate in coords:
            return True
    return False

def createNum(matrix, coords):
    # print(coords)
    sortedCoords = sorted(coords, key=lambda coord: coord[1])
    # print(sortedCoords)
    numString = ""
    for coord in sortedCoords:
        num = matrix[coord[0]][coord[1]]
        # print(num)
        numString += str(num)
    # print("number: ", numString)
    return int(numString)    

# search all coordinates: up, down, left, right, diagonally for numbers
def is2Adjacent(matrix, i, j):
    hits = 0
    coords = []
    nums = []
    # search left
    if j-1 >= 0:
        char = matrix[i][j-1]
        if char.isdigit():
            print("here left")
            currentCoords = extractNumber(matrix, i, j-1)
            if not isDuplicateCoord(coords, currentCoords):
                hits += 1
                nums.append(createNum(matrix, currentCoords))
                coords.extend(currentCoords)
    # search right
    if j+1 < len(matrix[i]):
        char = matrix[i][j+1]
        if char.isdigit():
            print("here right")
            currentCoords = extractNumber(matrix, i, j+1)
            if not isDuplicateCoord(coords, currentCoords):
                hits += 1
                nums.append(createNum(matrix, currentCoords))
                coords.extend(currentCoords)
    # search down
    if i-1 >= 0:
        char = matrix[i-1][j]
        if char.isdigit():
            print("here down")
            currentCoords = extractNumber(matrix, i-1, j)
            if not isDuplicateCoord(coords, currentCoords):
                hits += 1
                nums.append(createNum(matrix, currentCoords))
                coords.extend(currentCoords)
    # search up
    if i+1 < len(matrix):
        char = matrix[i+1][j]
        if char.isdigit():
            print("here up")
            currentCoords = extractNumber(matrix, i+1, j)
            if not isDuplicateCoord(coords, currentCoords):
                hits += 1
                nums.append(createNum(matrix, currentCoords))
                coords.extend(currentCoords)
    # search upper right
    if i-1 >= 0 and j+1 < len(matrix[i]):
        char = matrix[i-1][j+1]
        if char.isdigit():
            print("her righte")
            currentCoords = extractNumber(matrix, i-1, j+1)
            if not isDuplicateCoord(coords, currentCoords):
                hits += 1
                nums.append(createNum(matrix, currentCoords))
                coords.extend(currentCoords)

    # search upper left 
    if i-1 >= 0 and j-1 >= 0:
        char = matrix[i-1][j-1]
        if char.isdigit():
            print("her left e")
            currentCoords = extractNumber(matrix, i-1, j-1)
            if not isDuplicateCoord(coords, currentCoords):
                hits += 1
                nums.append(createNum(matrix, currentCoords))
                coords.extend(currentCoords)

    # search bottom right
    if i+1 < len(matrix) and j+1 < len(matrix[i]):
        char = matrix[i+1][j+1]
        if char.isdigit():
            print("here right")
            currentCoords = extractNumber(matrix, i+1, j+1)
            if not isDuplicateCoord(coords, currentCoords):
                hits += 1
                nums.append(createNum(matrix, currentCoords))
                coords.extend(currentCoords)

    # search bottom left 
    if i+1 < len(matrix) and j-1 >= 0:
        char = matrix[i+1][j-1]
        if char.isdigit():
            print("here left ")
            currentCoords = extractNumber(matrix, i+1, j-1)
            if not isDuplicateCoord(coords, currentCoords):
                hits += 1
                nums.append(createNum(matrix, currentCoords))
                coords.extend(currentCoords)

    print("hits: ", hits)  
    if hits == 2:
        return nums[0] * nums[1]
    return 0

# search all coordinates: up, down, left, right, diagonally
def isAdjacent(matrix, i, j):
    # search left
    if j-1 >= 0:
        char = matrix[i][j-1]
        if not char.isdigit() and char != ".":
            return True
    # search right
    if j+1 < len(matrix[i]):
        char = matrix[i][j+1]
        if not char.isdigit() and char != ".":
            return True
    # search down
    if i-1 >= 0:
        char = matrix[i-1][j]
        if not char.isdigit() and char != ".":
            return True
    # search up
    if i+1 < len(matrix):
        char = matrix[i+1][j]
        if not char.isdigit() and char != ".":
            return True
    # search upper right
    if i-1 >= 0 and j+1 < len(matrix[i]):
        char = matrix[i-1][j+1]
        if not char.isdigit() and char != ".":
            return True

    # search upper left 
    if i-1 >= 0 and j-1 >= 0:
        char = matrix[i-1][j-1]
        if not char.isdigit() and char != ".":
            return True

    # search bottom right
    if i+1 < len(matrix) and j+1 < len(matrix[i]):
        char = matrix[i+1][j+1]
        if not char.isdigit() and char != ".":
            return True

    # search bottom left 
    if i+1 < len(matrix) and j-1 >= 0:
        char = matrix[i+1][j-1]
        if not char.isdigit() and char != ".":
            return True
        
    return False

def runThroughMatrix(matrix):
    total = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == "*":
                print(matrix[i][j])
                total += is2Adjacent(matrix, i, j)
    print(total)
# def runThroughMatrix(matrix):
#     total = 0
#     goodToAdd = False
#     for i in range(len(matrix)):
#         currentNum = ""
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == "." and currentNum != "":
#                 if goodToAdd:
#                     print(int(currentNum))
#                     if currentNum.isdigit():
#                         total += int(currentNum)
#                     else:
#                         print("wtf")
#                     currentNum = ""
#                     goodToAdd = False
#                 else:
#                     if currentNum != "":
#                         print("miss: ", currentNum)
#                         currentNum = ""
#             elif matrix[i][j].isdigit():
#                 print(matrix[i][j])
#                 if (not goodToAdd):
#                     goodToAdd = isAdjacent(matrix,i,j)
#                 currentNum += matrix[i][j]
#                 print(currentNum)
#             elif not matrix[i][j].isdigit(): 
#                 if goodToAdd and currentNum != "":
#                     print(currentNum)
#                     total += int(currentNum)
#                 currentNum = ""
#                 goodToAdd = False
#         if goodToAdd and currentNum != "":
#             print(currentNum)
#             total += int(currentNum)
#             currentNum = ""
#             goodToAdd = False
#     print(total)
    




input = readFile('input.txt')
matrix = createMatrix(input)
runThroughMatrix(matrix)

# logic to solve this
# 1 create a matrix
# for each char that is a number check to see if there is a symbol around it
# keep track of the current number as you do this
# if we hit a symbol keep iterating until the num is finished and then add it

