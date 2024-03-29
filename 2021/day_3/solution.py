def readFile(path):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

reportNumbers = readFile("input.txt")

def analyzeReport(reportNumbers):
    mostCommonBits, leastCommonBits = "", ""
    for i in range(len(reportNumbers[0])):
        onesMostCommon = oneMostCommon(reportNumbers, i)
        if (onesMostCommon):
            mostCommonBits += "1"
            leastCommonBits += "0"
        else:
            mostCommonBits += "0"
            leastCommonBits += "1"
    answer = int(mostCommonBits, 2) * int(leastCommonBits, 2)
    return answer

def oneMostCommon(reportNumbers, index):
    zeroes = 0
    ones = 0
    for num in reportNumbers:
        if int(num[index]) == 1:
            ones += 1
        else:
            zeroes += 1
    return ones >= zeroes

def zeroMostCommon(reportNumbers, index):
    zeroes = 0
    ones = 0
    for num in reportNumbers:
        if int(num[index]) == 1:
            ones += 1
        else:
            zeroes += 1
    return zeroes >= ones

def pruneList(reportNumbers, numberNotToRemove, index):
    if len(reportNumbers) == 1:
        return reportNumbers
    for i in range(len(reportNumbers)):
        if int(reportNumbers[i][index]) == int(numberNotToRemove):
            continue
        else:
            reportNumbers[i] = float('inf')
    reportNumbers = [element for element in reportNumbers if element != float('inf')]
    return reportNumbers


def analyzeReportByElimination(reportNumbers):
    copy = reportNumbers[:]
    while len(reportNumbers) > 1:
        for i in range(len(reportNumbers[0])):
            onesMostCommon = oneMostCommon(reportNumbers, i)
            if onesMostCommon:
                reportNumbers = pruneList(reportNumbers, 1, i)
            else:
                reportNumbers = pruneList(reportNumbers, 0, i)
    oxygen = int(reportNumbers[0], 2)
    while len(copy) > 1:
        for i in range(len(copy[0])):
            onesMostCommon = oneMostCommon(copy, i)
            if onesMostCommon:
                copy = pruneList(copy, 0, i)
            else:
                copy = pruneList(copy, 1, i)
    carbon = int(copy[0], 2)
    return carbon * oxygen



# part 1
analyzeReport(reportNumbers)
# part 2
analyzeReportByElimination(reportNumbers)