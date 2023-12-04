def readFile(path):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

# def handleCard(card):
#     print(card)
#     splitCard = card.split("|")
#     winningNumbers = splitCard[0].split(":")[1]
#     winNumbsArr = winningNumbers.split()
#     inputNumsArr = splitCard[1].split()
#     matches = 0
#     total = 1
#     for num in inputNumsArr:
#         if num in winNumbsArr:
#             matches += 1
#     if matches == 0:
#         return 0
#     else:
#         for i in range(matches-1):
#             total *= 2
#         return total

def getMatches(card):
    winNumbArr,inputNumsArr = parseCard(card)
    return compareCards(winNumbArr, inputNumsArr)

def parseCard(card):
    splitCard = card.split("|")
    winningNumbers = splitCard[0].split(":")[1]
    winNumbArr = winningNumbers.split()
    inputNumsArr = splitCard[1].split()
    return winNumbArr, inputNumsArr

def compareCards(winNumsArr, inputNumsArr):
    matches = 0
    for num in inputNumsArr:
        if num in winNumsArr:
            matches += 1
    return matches

def handleMatches(matches, currentCardKey, cards):
    numToAdd = cards[currentCardKey][1]
    for i in range(matches):
        currentCardKey += 1
        cards[currentCardKey][1] += numToAdd
    return cards

def createCardsDictionary(input):
    cards = {}
    currentCard = 1
    for card in input:
        splitCard = card.split("|")
        winningNumbers = splitCard[0].split(":")[1]
        winNumbsArr = winningNumbers.split()
        inputNumsArr = splitCard[1].split()
        cards[currentCard] = [(winNumbsArr, inputNumsArr), 1]
        currentCard += 1
    return cards


total = 0
input = readFile("input.txt")
# split the input into winning numbers and my numbers per card
cards = createCardsDictionary(input)
currentCard = 1
for card in input:
    matches = getMatches(card)
    cards = handleMatches(matches, currentCard, cards)
    currentCard += 1

for key in cards.keys():
    total += cards[key][1]
print("final answer: ",total)