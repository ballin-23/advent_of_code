from functools import cmp_to_key


hands = []
input = open("input.txt").readlines()
for pair in input:
    hand, bid = pair.strip().split()
    hands.append((hand, int(bid)))

strengthDictionary = {'A': 13, 
                      'K': 12, 
                      'Q': 11, 
                      'J': 10, 
                      'T': 9, 
                      '9': 8, 
                      '8': 7, 
                      '7': 6, 
                      '6': 5, 
                      '5': 4, 
                      '4': 3, 
                      '3': 2, 
                      '2': 1,
                      'J': 0
                            }

def compareHands(a, b):
    aHandType = evaluateHand(a)
    bHandType = evaluateHand(b)
    
    if aHandType == bHandType:
        for i,j in (zip(a,b)):
            if i == j:
                continue
            else:
                # if we have different characters evaluate strength
                if strengthDictionary[i] > strengthDictionary[j]:
                    return 1
                else:
                    return -1
    else:
        if aHandType > bHandType:
            return 1
        return -1


def evaluateHand(hand):
    analyzedHand = analyzeHand(hand)
    typeOfHand = breakDownHand(analyzedHand)
    return typeOfHand

def analyzeHand(hand):
    arr = []
    uniqueCards = set(hand)
    jokers = 0
    print(hand) 
    for card in uniqueCards:
        if card == "J":
            jokers = hand.count(card)
        else:
            arr.append(hand.count(card))
    arr.sort(reverse=True)
    if jokers == 5:
        return [5]
    if jokers != 0:
        arr[0] += jokers
    return arr

def breakDownHand(hand):
    greatest = hand[0]
    if greatest == 5:
        return 50
    elif greatest == 4:
        return 40
    elif greatest == 3:
        if hand[1] == 2:
            return 35
        else:
            return 30
    elif greatest == 2:
        if hand[1] == 2:
            return 20
        else:
            return 10
    elif greatest == 1:
        return 1

hands = sorted(hands, key=cmp_to_key(lambda x,y: compareHands(x[0], y[0])))
# hands.reverse()

answer = 0
for i in range(len(hands)):
    answer += hands[i][1] * (i+1)
for hand in hands:
    print(hand)
print(answer)