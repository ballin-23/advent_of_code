def readFile(path="input.txt"):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

def getSequences(input):
    sequences = []
    for sequence in input:
        sequences.append(list(map(int, sequence.split())))
    print(sequences)
    return sequences

def getDifference(sequence):
    diffArr = []
    if len(sequence) > 1:
        for i in range(1, len(sequence)):
            diffArr.append(sequence[i] - sequence[i-1])
    # print('diff arr: ', diffArr)
    return diffArr

def checkZeroes(sequence):
    allZeroes = all(element == 0 for element in sequence)
    print("check zeroes: ", allZeroes)
    return allZeroes

def extrapolate(sequence):
    isAllZeroes = False
    pattern = []
    while not isAllZeroes != 0:
        differenceArr = getDifference(sequence)
        print("difference arr: ", differenceArr)
        isAllZeroes = checkZeroes(sequence)
        if not isAllZeroes:
            pattern.append(differenceArr)
            sequence = differenceArr
    pattern.reverse()
    print('pattern ', pattern)
    return pattern

def solve(sequence, pattern):
    prev = 0
    for i in range(len(pattern)):
        # print("pattern: ", pattern)
        prev =  pattern[i][0] - prev
        # print("prev: ", prev)
    total = sequence[0] - prev
    # print("total: ", total)
    return total

answer = 0
input = readFile()
sequences = getSequences(input)
for sequence in sequences:
    pattern = extrapolate(sequence)
    extrapolatedNum = solve(sequence, pattern)
    answer += extrapolatedNum
print(answer)


# answer = 0
# input = readFile()
# sequences = getSequences(input)
# for sequence in sequences:
#     pattern = extrapolate(sequence)
#     extrapolatedNum = solve(sequence, pattern)
#     answer += extrapolatedNum
# print(answer)