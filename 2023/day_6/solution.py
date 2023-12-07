def readFile(path="input.txt"):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

def calculateWaysToWin(time, distance):
    count = 0
    print("time: ", time)
    print("distance: ", distance)
    for i in range(time+1):
        speed = i
        newTime = time - i
        distance2 = speed * newTime
        # print("i: ", i)
        # print("speed: ", speed, " time: ", time, " distance: ", distance2)
        if distance2 > distance:
            count += 1
    return count


input = readFile()
time = list(map(int, input[0].split(':')[1].split()))
distance = list(map(int,input[1].split(':')[1].split()))

time2 = ""
for t in time:
    time2 += str(t)
time2 = int(time2)
print(time2)

distance2 = ""
for t in distance:
    distance2 += str(t)
distance2 = int(distance2)
print(distance2)

# process the inputs now
answer = 1
# for i in range(len(distance)):
#     # just get the i here doesn't matter since arrays are the same
#     answer *= calculateWaysToWin(time[i], distance[i])
# print(answer)
answer *= calculateWaysToWin(time2, distance2)
print(answer)