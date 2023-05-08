# write a function with 3 levels of validation
# first level = 3 vowels = [a,e,i,o,u]
# second level = at least one letter appear twice in a row
# does not contain the strings ab, cd, pq, xy

def count_nice_string():
    nice_strings = 0
    with open('input.txt') as file:
        for line in file:
            if is_nice_string_p2(line):
                nice_strings += 1
    return nice_strings


def is_nice_string_p2(input):
    if (findTwiceNoOverlap(input) and containsPair(input)):
        return True
    return False

def findTwiceNoOverlap(input):
    prev = ""
    between = ""
    after_next_of_prev = ""
    for i in range(len(input)):
        if i == 0:
            prev = input[i]
        elif i == 1:
            between = input[i]
        elif i == 2:
            after_next_of_prev = input[2]
            if prev == after_next_of_prev and prev != between:
                return True
        else:
            if prev == after_next_of_prev:
                return True
            else:
                prev = between
                between = after_next_of_prev
                after_next_of_prev = input[i]     
    return False

def containsPair(input):
    if len(input) < 1:
        return False
    else:
        first = input[0]
        second = input[1]
        for i in range(len(input)):
            pair = str(first)+str(second)
            if input.count(pair) > 1:
                return True
            else:
                first = second
                second = input[i]
    return False

def is_nice_string_p1(input):
    if (validateCombinations(input) and findTwiceInRow(input) and atLeastNVowels(3, input)):
        return True
    return False

def validateCombinations(input):
    combinations = ['ab', 'cd', 'pq', 'xy']
    for combination in combinations:
        if combination in input:
            return False
    return True

def findTwiceInRow(input):
    prev = ""
    for i in range(len(input)):
        if input[i] == prev:
            return True
        prev = input[i]
    return False

def atLeastNVowels(num, input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    counter = 0
    for i in range(len(input)):
        if input[i] in vowels:
            counter += 1
            if counter >= num:
                return True
    return False

 
print(count_nice_string())