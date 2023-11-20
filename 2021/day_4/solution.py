def readBingo(path):
    cards = []
    bingoNumbers = []
    with open(path, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            # this gets out the numbers
            if i == 0:
                bingoNumbers.append(lines[i].strip())
            else:
                cards.append(lines[i].strip())
    # print("bingo numbers: ", bingoNumbers)
    cards = convertToBingoCards(cards)
    return bingoNumbers, cards

def convertToBingoCards(arr):
    cards = []
    currentCards = []
    count = 0
    for card in arr:
        # print('current card: ', card)
        if card == "":
            continue
        else:
            currentCards.append(card.split())
            count += 1
        if count == 5:
            cards.append(currentCards)
            currentCards = []
            count = 0
    return cards

def checkBoardForWinner(board):
    if checkRows(board):
        return True
    if checkColumns(board):
        return True
    # if checkLeftDiagnol(board):
    #     return True
    # if checkRightDiagnol(board):
    #     return True
    return False

def checkRows(board):
    for row in board:
        marked = True
        for val in row:
            if val == "x":
                continue
            else:
                marked = False
        if marked:
            return True
    return False


def checkColumns(board):
    for i in range(len(board)):
        marked = True
        col = getColumn(board, i)
        for val in col:
            if val == "x":
                continue
            else:
                marked = False
        if marked:
            return True
    return False


def getColumn(board, index):
    arr = []
    for row in board:
        arr.append(row[index])
    return arr


def checkLeftDiagnol(board):
    if checkLeftDiagnolTop(board):
        return True
    if checkLeftDiagnolBottom(board):
        return True

def checkLeftDiagnolTop(board):
    row = 0
    column = 0
    marked = True
    while row < len(board) and column < len(board[0]) and marked:
        if board[row][column] == "x":
            row += 1
            column += 1
        else:
            marked = False
    return marked

def checkLeftDiagnolBottom(board):
    row = len(board)-1
    column = 0
    marked = True
    while row > -1 and column < len(board[0]) and marked:
        if board[row][column] == "x":
            row -= 1
            column += 1
        else:
            marked = False
    return marked

def checkRightDiagnol(board):
    if checkRightDiagnolTop(board):
        return True
    if checkRightDiagnolBottom(board):
        return True

def checkRightDiagnolTop(board):
    row = 0 
    column = len(board[0]) - 1
    marked = True
    while row < len(board) and column > -1 and marked:
        # print(board[row][column])
        if board[row][column] == "x":
            row +=1 
            column -=1
        else:
            marked = False
    return marked
    
def checkRightDiagnolBottom(board):
    row = len(board) -1 
    column = len(board[0]) - 1
    marked = True
    while row > -1 and column > -1 and marked:
        print(board[row][column])
        if board[row][column] == "x":
            # print("found an x: ", board[row][column])
            row -=1 
            column -=1
        else:
            marked = False
    return marked
            

# sampleInput = [["x", "1", "x"],
#                ["1", "x", "1"],
#                ["x", "1", "x"]]

# print(checkRightDiagnolBottom(sampleInput))

def updateBoard(cards, num):
    for card in cards:
        for i in range(len(card)):
            for j in range(len(card[i])):
                if card[i][j] == num:
                    card[i][j] = "x"
    return cards

def sumCard(card):
    sum = 0
    for row in card:
        for val in row:
            if val != "x":
                sum += int(val)
    return sum


# def solve():
#     bingoNumbers, cards = readBingo("input.txt")
#     realBingoNumbers = bingoNumbers[0].split(',')
#     print(realBingoNumbers)
#     for num in realBingoNumbers:
#         print("current num: ", num)
#         cards = updateBoard(cards, num)
#         print("updated")
#         for card in cards:
#             print("card")
#             for row in card:
#                 print(row)
#             print("---")
#         print("---")
#         for card in cards:
#             for row in card:
#                 print(row)
#             isWinner = checkBoardForWinner(card)
#             if (isWinner):
#                 print("found a winner")
#                 sumOfCard = sumCard(card)
#                 print(sumOfCard)
#                 print(int(num))
#                 print(sumOfCard * int(num))
#                 return

# part 2
def solve():
    bingoNumbers, cards = readBingo("input.txt")
    realBingoNumbers = bingoNumbers[0].split(',')
    print(realBingoNumbers)
    for num in realBingoNumbers:
        print("number of cards: ", len(cards))
        print("current num: ", num)
        cards = updateBoard(cards, num)
        print("updated")
        for card in cards:
            print("card")
            for row in card:
                print(row)
            print("---")
        print("---")
        cardsToRemove = []
        for i in range(len(cards)):
            for row in cards[i]:
                print(row)
            isWinner = checkBoardForWinner(cards[i])
            if (isWinner):
                if len(cards) == 1:
                    print("found last winner")
                    sumOfCard = sumCard(card)
                    print(sumOfCard)
                    print(int(num))
                    print(sumOfCard * int(num))
                    return
                else:
                    print("found a winner but we keep going")
                    cardsToRemove.append(i)
        print("indices to remove: ", cardsToRemove)
        newCards = []
        for i in range(len(cards)):
            if i in cardsToRemove:
                continue
            else:
                newCards.append(cards[i])
        cards = newCards
        cardsToRemove = []
        
    

solve()