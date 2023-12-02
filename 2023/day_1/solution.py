def readFile(path):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

def findFirstLetterWord(arr):
    lowestIndex = float('inf')
    word = ""
    for num in numArr:
        # print(num)
        # print(arr.find(num))
        idx = arr.find(num)
        if lowestIndex > idx and idx != -1:
            lowestIndex = idx
            word = num
    # print(word)
    return word, lowestIndex

def findLastLetterWord(arr):
    highestIndex = -2
    word = ""
    for num in numArr:
        # print(num)
        # print(arr.find(num))
        idx = arr.rfind(num)
        if highestIndex < idx and idx != -1:
            highestIndex = idx
            word = num
    # print(word)
    return word, highestIndex

def findFirstNum(arr):
    index = -2
    for i in range(len(arr)):
        if arr[i].isdigit():
            index = i
            return arr[i], index
    return index, index

def findLastNum(arr):
    index = -1
    for i in range(len(arr)-1,-1,-1):
        if arr[i].isdigit():
            return arr[i], i
    return index, index
    
numArr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def word_to_number(word):
    number_mapping = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    return number_mapping[word]

def evaluateLineFirst(arr):
    value1, index1 = findFirstNum(arr)
    value2, index2 = findFirstLetterWord(arr)
    # print(index1, index2)
    if index1 == -2:
        (word_to_number(value2))
        return str(word_to_number(value2))
    if (index1 > index2):
        print(word_to_number(value2))
        return str(word_to_number(value2))
    else:
        print(value1)
        return str(value1)


def evaluateLineLast(arr):
    value1, index1 = findLastNum(arr)
    value2, index2 = findLastLetterWord(arr)
    # print(value1, index1)
    if index1 == -1:
        print((word_to_number(value2)))
        return str(word_to_number(value2))
    if (index1 > index2):
        print(value1)
        return (value1)
    else:
        print(word_to_number(value2))
        return str(word_to_number(value2))


arr = readFile("input.txt")
count = 0
for line in arr:
    first = evaluateLineFirst(line)
    last = evaluateLineLast(line)
    print(type(first), type(last))
    count += int(first+last)
print(count)