def readFile(path):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

def evaluateGame(game_input, red, green, blue):
    sets = game_input.split(';')
    for set in sets:
        redc = red
        greenc = green
        bluec = blue
        colors = set.strip().split(',')
        for color in colors:
            colorMap = color.strip().split()
            # print(colorMap)
            if colorMap[1] == "green":
                greenc -= int(colorMap[0])
                print("green: ", green)
            elif colorMap[1] == "red":
                redc -= int(colorMap[0])
            else:
                bluec -= int(colorMap[0])
            # print(red)
            if 0 > redc or 0 > bluec or 0 > greenc:
                print("couldn't finish game")
                # print("Game Finished")
                return False
    print("good game")
    # print("Game Finished")
    return True

def findMax(game_input):
    sets = game_input.split(';')
    maxr = 0
    maxg = 0
    maxb = 0
    for set in sets:
        colors = set.strip().split(',')
        for color in colors:
            colorMap = color.strip().split()
            # print(colorMap)
            if colorMap[1] == "green":
                if int(colorMap[0]) > maxg:
                    maxg = int(colorMap[0])
            elif colorMap[1] == "red":
                if int(colorMap[0]) > maxr:
                    maxr = int(colorMap[0])
            else:
                if int(colorMap[0]) > maxb:
                    maxb = int(colorMap[0])
    print("green: ", maxg)
    print("red: ", maxr)
    print("blue: ", maxb)
    print("game finished")
    return maxr * maxg * maxb


games = readFile('input.txt')
total = 0
for game in games:
    game_input = game.split(':')
    id = int(game_input[0].split()[1].strip())
    total += findMax(game_input[1])
    # if(evaluateGame(game_input[1], 12, 13, 14)):
        # print(id)
        # count += id
print(total)
        

