import numpy as np

grid = np.zeros((1000, 1000))

def read_file(fileName):
    return open(fileName, 'r').readlines()


def turn_on_lights(grid, x1, y1, x2, y2):
    # we start at x1 and y1 and go until x2, y2
    for i in range(x1, x2+1, 1):
        for j in range(y1, y2+1, 1):
            grid[i,j] = 1

def toggle_lights(grid, x1, y1, x2, y2):
    # we start at x1 and y1 and go until x2, y2
    for i in range(x1, x2+1, 1):
        for j in range(y1, y2+1, 1):
            grid[i,j] = abs(grid[i,j]-1)

def turn_off_lights(grid, x1, y1, x2, y2):
    # we start at x1 and y1 and go until x2, y2
    for i in range(x1, x2+1, 1):
        for j in range(y1, y2+1, 1):
            grid[i,j] = 0

def count_lights_on(grid):
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                counter += 1
    print(counter)
    return counter

def solve(fileName):
    lines = read_file(fileName)
    for line in lines:
        if line[:2] == "to":
            tokens = line.split()
            x1,y1 = tokens[1].split(',')
            x2, y2 = tokens[3].split(',')
            toggle_lights(grid, int(x1), int(y1), int(x2), int(y2))
        else:
            tokens = line.split()
            x1,y1 = tokens[2].split(',')
            x2, y2 = tokens[4].split(',')
            if tokens[1] == "off":
                turn_off_lights(grid, int(x1), int(y1), int(x2), int(y2))
            else:
                turn_on_lights(grid, int(x1), int(y1), int(x2), int(y2))
    count_lights_on(grid)

# part 1
solve("input.txt")
