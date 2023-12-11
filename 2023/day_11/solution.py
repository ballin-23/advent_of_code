def createGalaxies(path="input.txt"):
    galaxies = []
    with open(path, 'r') as file:
        for line in file:
            galaxies.append([c for _,c in enumerate(line.strip())])
    return galaxies

def add_row_of(matrix, index_to_insert, arr):
    for i in range(len(matrix)):
        matrix[i].insert(index_to_insert + 1, arr[i])
    return matrix

def expandRows(matrix):
    rowsToExpand = []
    for i in range(len(matrix)):
        if "#" not in matrix[i]:
            rowsToExpand.append(i)
    rowsToExpand.reverse()
    for i in range(len(rowsToExpand)):
        new_row = ["."] * len(matrix[i])
        matrix.insert(rowsToExpand[i], new_row)
    return matrix

def expandCols(matrix):
    colsToExpand = []
    columns = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    for i in range(len(columns)):
        if "#" not in columns[i]:
            colsToExpand.append(i)
    colsToExpand.reverse()
    for i in range(len(colsToExpand)):
        for j in range(len(matrix)):
            matrix[j].insert(colsToExpand[i]+1, ".")
    return matrix

def getGalaxyCoords(matrix):
    coords = []
    for i in range(len(matrix)):
        if "#" in matrix[i]:
            indices_of_hash = [index for index, value in enumerate(matrix[i]) if value == "#"]
            for index in indices_of_hash:
                coords.append([i, index])
    return coords

def expand(matrix):
    expand_rows = expandRows(matrix)
    expanded_cols = expandCols(expand_rows)
    return expanded_cols

def generatePairs(coords):
    all_pairs = []

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            pair = (coords[i], coords[j])
            all_pairs.append(pair)
    return all_pairs

def findChildren(matrix, row, position, seen):
    children = []
    # check above
    if row-1 >= 0 and (row-1, position) not in seen:
        children.append((row-1, position))
    # check below
    if row+1 < len(matrix) and (row+1, position) not in seen:
        children.append((row+1, position))
    # check left
    if position -1 >= 0 and (row, position-1) not in seen:
        children.append((row, position-1))
    # check right
    if position +1 < len(matrix[row]) and (row, position+1) not in seen:
        children.append((row, position+1))
    return children

# bfs that searches for a start and finish
def bfs(matrix, start, end):
    if start == end:
        return 0
    else:
        steps = 0
        nodesToExplore = [start]
        seen = []
        while len(nodesToExplore) > 0:
            childrenCurrentStep = []
            # print("nodes to explore: ", nodesToExplore)
            for node in nodesToExplore:
                if node not in seen:
                    # print("node: ", node, " end: ", end)
                    seen.append(node)
                    if node[0] == end[0] and node[1] == end[1]:
                        return steps
                    childrenCurrentStep.extend(findChildren(matrix, node[0], node[1], seen))
            nodesToExplore = childrenCurrentStep
            steps += 1

# Manhattan distance=∣x2−x1∣+∣y2−y1∣
def manhattanDistance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def solvePart1():
    galaxies = createGalaxies()
    new_galaxies = expand(galaxies)
    coords = getGalaxyCoords(galaxies)
    pairs = generatePairs(coords)
    total = 0
    for i in range(len(pairs)):
        total += manhattanDistance(pairs[i][0][0], pairs[i][0][1], pairs[i][1][0], pairs[i][1][1])
    return total
