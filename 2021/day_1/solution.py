def readFile(path):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

def stringArrToNumArr(arr):
    return [int(x) for x in arr]

arr = readFile("input.txt")
numArr = stringArrToNumArr(arr)

# part 1
def greater_than_prev(nums):
    count = 0
    prev = nums[0]
    for i in range(1,len(nums)):
        if nums[i] > prev:
            count += 1
        prev = nums[i]
    print(count)
    return count

# part 2
def create_threes(nums):
    arr = []
    sum_arr = []
    for i in range(len(nums)):
        if len(arr) == 3:
            arr.pop(0)
            arr.append(nums[i])
            sum_arr.append(sum_numbers(arr))
        else:
            arr.append(nums[i])
            if len(arr) == 3:
                sum_arr.append(sum_numbers(arr))
    print(sum_arr)
    return sum_arr

def sum_numbers(arr):
    total = 0
    for num in arr:
        total+= num
    return total

# part 1 answer
# greater_than_prev(numArr)
# part 2 answer
new_arr = create_threes(numArr)
greater_than_prev(new_arr)