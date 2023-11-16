def readFile(path):
    file_arr = []
    with open(path, 'r') as file:
        for line in file:
            file_arr.append(line.strip())
    return file_arr

def handleInstructionPart1(direction, num, verticalPosition, horizontalPosition):
    if direction == "forward":
        horizontalPosition += num
    elif direction == "down":
        verticalPosition += num
    else:
        verticalPosition -= num
    return verticalPosition, horizontalPosition

def handleInstructionPart2(direction, num, verticalPosition, horizontalPosition, aim):
    if direction == "forward":
        horizontalPosition += num
        verticalPosition += (aim * num)
    elif direction == "down":
        aim += num
    else:
        aim -= num
    return verticalPosition, horizontalPosition, aim   

instructionArr = readFile("input.txt")

# def determine_position(func):
#     verticalPosition = 0
#     horizontalPosition = 0

#     for instruction in instructionArr:
#         tokenizedInstruction = instruction.split()
#         direction = tokenizedInstruction[0]
#         num = int(tokenizedInstruction[1])
#         verticalPosition, horizontalPosition = func(direction, num, verticalPosition, horizontalPosition)
#     print("vertical position: ",verticalPosition,"horizontal position", horizontalPosition)
#     print(horizontalPosition * verticalPosition)
#     return horizontalPosition * verticalPosition

def determine_position():
    verticalPosition = 0
    horizontalPosition = 0
    aim = 0

    for instruction in instructionArr:
        tokenizedInstruction = instruction.split()
        direction = tokenizedInstruction[0]
        num = int(tokenizedInstruction[1])
        verticalPosition, horizontalPosition, aim = handleInstructionPart2(direction, num, verticalPosition, horizontalPosition, aim)
    print("vertical position: ",verticalPosition,"horizontal position", horizontalPosition, " aim: ", aim)
    print(horizontalPosition * verticalPosition)
    return horizontalPosition * verticalPosition

determine_position()
