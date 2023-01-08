def read_file():
    file = open("input.txt", mode="r")
    return file.readlines()

# part 1
def calculate_floors(arr):
    sum = 0
    for line in arr:
        for char in line:
            if char == "(":
                sum += 1
            else:
                sum -= 1
    return sum

# part 2
def first_negative_floor(arr):
    sum = 0
    seen = 0
    for line in arr:
        for char in line:
            if char == "(":
                sum += 1
                seen += 1
            else:
                sum -= 1
                seen += 1
            if sum < 0:
                return seen
    return sum

floors = read_file()
print(calculate_floors(floors))
print(first_negative_floor(floors))