
def readFile(path="input.txt"):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

input = readFile()
instructions = [char for char in input[0]]
# print(instructions)

starting_keys = []
map = {}
coords = input[2:]
for coord in coords:
    split = coord.split("=")
    key = split[0].strip()
    if key[2] == "A":
        starting_keys.append(key)
    map[key] = my_tuple = tuple(split[1][2:-1].split(', '))
print(map)
print("starting keys ", starting_keys)

def isKey(key):
    if key == "ZZZ":
        return True
    return False

def lcm(nums):
    result = nums[0]

    for num in nums[1:]:
        result *= num

    return result

def endsWithZ(key):
    if key[2] == "Z":
        return True
    return False

def getSteps(key):
    i = 0
    while not endsWithZ(key):
        index = i % len(instructions)
        currentPosition = map[key]
        if instructions[index] == "L":
            key = currentPosition[0]
            # print("went left")
        else:
            key = currentPosition[1]
            # print("went right")
        # print("current key: ", currentKey)
        i += 1
        print(i)
    print(i)
    return i

indices = []
for key in starting_keys:
    index = getSteps(key)
    indices.append(index)
print("----")
for item in indices:
    print(item)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_list(numbers):
    result = numbers[0]

    for num in numbers[1:]:
        result = lcm(result, num)

    return result

print(lcm_of_list(indices))

# print(math.lcm())
# print(lcm(indices))
# def allCoordsContainEndingZ(keys):
#     for key in keys:
#         if key[2] != "Z":
#             # print('should return false')
#             return False
#     return True

# # solve part 2
# i = 0
# while not allCoordsContainEndingZ(starting_keys):
#     new_keys = []
#     index = i % len(instructions)
#     for key in starting_keys:
#         currentPosition = map[key]
#         if instructions[index] == "L":
#             currentKey = currentPosition[0]
#             # print("went left")
#         else:
#             currentKey = currentPosition[1]
#             # print("went right")
#         # print("current key: ", currentKey)
#         new_keys.append(currentKey)
#     i += 1
#     starting_keys = new_keys
#     print(i)
# print(i)
# start solving here with the map
currentKey = "AAA"
i = 0

# def getSteps(key):
#     i = 0
#     while not isKey(key):
#         index = i % len(instructions)
#         currentPosition = map[key]
#         if instructions[index] == "L":
#             key = currentPosition[0]
#             # print("went left")
#         else:
#             key = currentPosition[1]
#             # print("went right")
#         # print("current key: ", currentKey)
#         i += 1
#         # print(i)
#     print(i)
#     return i

# getSteps(currentKey)

# while not isKey(currentKey):
#     index = i % len(instructions)
#     currentPosition = map[currentKey]
#     if instructions[index] == "L":
#         currentKey = currentPosition[0]
#         # print("went left")
#     else:
#         currentKey = currentPosition[1]
#         # print("went right")
#     print("current key: ", currentKey)
#     i += 1
    
# print("we out")
# print(i)