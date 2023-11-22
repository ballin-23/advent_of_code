def readFile(path="input.txt"):
    grid = createGrid(1000)
    with open(path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            x1, y1, x2, y2 = parseCoordinates(line.strip().replace(" ", ""))
            coords = getCoordinates(x1, y1, x2, y2)
            # print("coords: ",coords)
            grid = updateGrid(coords, grid)
    scanGrid(grid)

def parseCoordinates(input):
    split = input.split("->")
    # print("original: ", split)
    left = split[0].split(',')
    x1 = int(left[0])
    y1 = int(left[1])
    right = split[1].split(',')
    x2 = int(right[0])
    y2 = int(right[1])
    # print("x1: ", x1, " y1: ", y1)
    # print("x2: ", x2, " y2: ", y2)
    return x1, y1, x2, y2


def createGrid(n):
    arr = []
    for i in range(n):
        new_arr = [0]*n
        arr.append(new_arr)
    return arr

def getCoordinates(x1, y1, x2, y2):
    coords = []
    ranges = []
    if x1 == x2:
        if y1 > y2:
            ranges = list(range(y2, y1+1))
        else:
            ranges = list(range(y1, y2+1))
        for num in ranges:
            coords.append([x1, num])
    elif y1 == y2:
        if x1 > x2:
            ranges = list(range(x2, x1+1))
        else:
            ranges = list(range(x1, x2+1))
        for num in ranges:
            coords.append([num, y1])
    else:
        diagnolLines = handleDiagnolLines(x1, y1, x2, y2)
        coords.extend(diagnolLines)
    return coords

def handleDiagnolLines(x1, y1, x2, y2):
    arr = [[x1, y1]]
    if x1 < x2 and y1 < y2:
        while x1 != x2:
            x1 += 1
            y1 += 1
            arr.append([x1, y1])
    elif x1 > x2 and y1 < y2:
        while x1 != x2:
            x1 -= 1
            y1 += 1
            arr.append([x1, y1])
    elif x1 < x2 and y1 > y2:
        while x1 != x2:
            x1 += 1
            y1 -= 1
            arr.append([x1, y1])
    elif x1 > x2 and y1 > y2:
        while x1 != x2:
            x1 -= 1
            y1 -= 1
            arr.append([x1, y1])
    return arr


def updateGrid(coordinates, grid):
    for coordinate in coordinates:
        grid[coordinate[1]][coordinate[0]] = grid[coordinate[1]][coordinate[0]] + 1
    return grid

def scanGrid(grid):
    count = 0
    for row in grid:
        for val in row:
            if val > 1:
                count += 1
    print(count)
    return count


readFile()
# getCoordinates(0,9,2,9)
# handleDiagnolLines(9,7,7,9)