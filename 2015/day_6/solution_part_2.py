import numpy as np

grid = np.zeros((1000, 1000))

def read_file(fileName):
    return open(fileName, 'r').readlines()

# part 2
def adjust_brightness(grid, x1, y1, x2, y2, brightness):
    # we start at x1 and y1 and go until x2, y2
    for i in range(x1, x2+1, 1):
        for j in range(y1, y2+1, 1):
            if brightness == -1:
                if grid[i,j] == 0:
                    continue
                else:
                    grid[i,j] = grid[i,j] + brightness
            else:
                grid[i,j] = grid[i,j] + brightness


def add(grid):
    counter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            counter += grid[i][j]
    print(counter)
    return counter


def solve_part_2(fileName):
    lines = read_file(fileName)
    for line in lines:
        if line[:2] == "to":
            tokens = line.split()
            x1,y1 = tokens[1].split(',')
            x2, y2 = tokens[3].split(',')
            adjust_brightness(grid, int(x1), int(y1), int(x2), int(y2),2)
        else:
            tokens = line.split()
            x1,y1 = tokens[2].split(',')
            x2, y2 = tokens[4].split(',')
            if tokens[1] == "off":
                adjust_brightness(grid, int(x1), int(y1), int(x2), int(y2),-1)
            else:
                adjust_brightness(grid, int(x1), int(y1), int(x2), int(y2),1)
    add(grid)
solve_part_2("input.txt")