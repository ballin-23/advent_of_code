# write a function with 3 levels of validation
# first level = 3 vowels = [a,e,i,o,u]
# second level = at least one letter appear twice in a row
# does not contain the strings ab, cd, pq, xy

def count_nice_string():
    nice_strings = 0
    with open('input.txt') as file:
        for line in file:
            if is_nice_string(line):
                nice_strings += 1
    return nice_strings
            
def is_nice_string(input):
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