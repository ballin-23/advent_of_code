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

def getValidChildren(matrix, current):
    if matrix[current[0]][current[1]] == "S":
        return getChildrenFromStart(matrix, current)
    else:
        translateValueAndGetChildren(matrix, current)

def getChildrenFromStart(matrix, current):
    row = current[0]
    position = current[1]
    children = []
    # check row below
    if row - 1 >= 0:
        children.append(matrix[row-1][position])
    # check row above
    if row + 1 < len(matrix):
        children.append(matrix[row+1][position])
    # check left
    if position - 1 >= 0:
        children.append(matrix[row][position-1])
    if position + 1 > len(matrix[0]):
        children.append(matrix[row][position+1])
    filteredChildren = [child for child in children if child != "."]
    print("current: ", current, " children: ",filteredChildren)
    return filteredChildren

# we need the start to detect a cycle
def dfs(matrix, current, visited, start):
    if current not in visited:
        visited.append(current)
        children = getValidChildren(current)
        for child in children:
            dfs(matrix, child, visited, start)

def solvePart1():
    input = readFile()
    matrix = createMatrix(input)
    startingPoint = findStartingPoint(matrix)
    print("starting point: ",startingPoint)
    # from here we dfs and find our loop