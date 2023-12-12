def readFile(path="input.txt"):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

def analyzeHand(hand):
    arr = []
    handValues = {}
    uniqueCards = set(hand)
    for card in uniqueCards:
        arr.append(hand.count(card))
    arr.sort(reverse=True)
    # print(arr)
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


input = readFile()
overallDictionary = {}
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
                      '2': 1}


# def group_strings(strings):
#     groups = {}
#     for string in strings:
#         # print(string)
#         if string[0][0] in groups:
#             groups[string[0][0]].append(string)
#         else:
#             groups[string[0][0]] = [string]
#     print(groups)
#     return groups

# Custom sorting function based on the strength value of the first character
def custom_sort(string, i):
    first_char = string[0][i]
    return strengthDictionary.get(first_char, 0)

def initialSort(arr):
    handDictionary = {}
    for key in strengthDictionary.keys():
        for hand in arr:
            if hand[0][0] == key:
                if key in handDictionary:
                    handDictionary[key].append(hand)
                else:
                    handDictionary[key] = [hand]
    # print(handDictionary)
    return handDictionary

def fiveIndexSort(dict):
    for key in dict.keys():
        for i in range(5):
            dict[key] = sorted(dict[key], key=lambda x: custom_sort(x, i=i))
        print(dict[key])
    return dict

for line in input:
    row = line.split()
    hand = row[0]
    bid = row[1]
    # print(hand)
    sortedHand = analyzeHand(hand)
    cardKey = breakDownHand(sortedHand)
    # print("key: ", cardKey)
    if cardKey in overallDictionary:
        overallDictionary[cardKey].append((hand, bid))
    else:
        overallDictionary[cardKey] = [(hand, bid)]
# print(overallDictionary)

sortedDictionary = dict(sorted(overallDictionary.items()))
for key in sortedDictionary.keys():
    # here we have lists of each hand in this format ('hand', bid)
    # print(sortedDictionary[key])
    initalDictionary = initialSort(sortedDictionary[key])
    secondPass = fiveIndexSort(initalDictionary)

# initialSort([])
