def readFile(path="input.txt"):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

def createMatrix(input):
    matrix = []
    for line in input:
        arr = []
        for symbol in line:
            arr.append(symbol)
        matrix.append(arr)
    return matrix

# we deal in row and position in row
def findStartingPoint(matrix):
    coords = (0,0)
    for i in range(len(matrix)):
        if "S" in matrix[i]:
            coords = (i, matrix[i].index("S"))
    return coords

def bfs(matrix, start):
    seen = []
    nodesToVisit = [start]

    while len(nodesToVisit) > 0:
        currentNode = nodesToVisit.pop(-1)
        if currentNode not in seen:
            seen.append(currentNode)
            children = exploreNode(matrix, currentNode[0], currentNode[1], seen)
            # print("children: ",children)
            nodesToVisit.extend(children)
            # print("nodes to visit: ",nodesToVisit)
    # print('seen: ', seen)
    return seen

def exploreNode(matrix, row, position, seen):
    discovered = []
    currentValue = matrix[row][position]
    print("current value: ", currentValue)
    print("matrix: ", row,",",position, " value: ", currentValue)
    # check if we can go up and if the row above can recieve upwards motion
    if row-1 >= 0:
        if currentValue in "S|LJ" and matrix[row-1][position] in "|7F" and (row-1, position) not in seen:
            discovered.append((row-1, position))
    # check the row below
    if row+1 < len(matrix):
        if currentValue in "S|7F" and matrix[row+1][position] in "|LJ" and (row+1, position) not in seen:
            print("here")
            discovered.append((row+1, position))
    # check the position to the left
    if position - 1 >= 0:
        if currentValue in "S-J7" and matrix[row][position-1] in "-FL" and (row, position-1) not in seen:
            discovered.append((row, position-1))
    # check the position to the right
    if position + 1 < len(matrix[row]):
        if currentValue in "S-FL" and matrix[row][position+1] in "-J7" and (row, position+1) not in seen:
            discovered.append((row, position+1))
    # print("returning discovered: ",discovered)
    return discovered

def solvePart1():
    global counter
    input = readFile()
    matrix = createMatrix(input)
    startingPoint = findStartingPoint(matrix)
    print(startingPoint)
    path = bfs(matrix, startingPoint)
    print(len(path)//2)

solvePart1()