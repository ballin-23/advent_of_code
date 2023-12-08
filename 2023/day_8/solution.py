def readFile(path="input.txt"):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

input = readFile()
instructions = [char for char in input[0]]
# print(instructions)

map = {}
coords = input[2:]
for coord in coords:
    split = coord.split("=")
    # print(split[0])
    # print(split[1].strip())
    map[split[0].strip()] = my_tuple = tuple(split[1][2:-1].split(', '))
print(map)

# start solving here with the map
currentKey = "AAA"
currentPosition = map[currentKey]
goal = "ZZZ"
# i = list(map.keys()).index(currentKey)
# print(i)
i = 0

while currentKey != "ZZZ":
    index = i % len(instructions)
    currentPosition = map[currentKey]
    if instructions[index] == "L":
        currentKey = currentPosition[0]
        print("went left")
    else:
        currentKey = currentPosition[1]
        print("went right")
    print("current key: ", currentKey)
    i += 1

print("we out")
print(i)