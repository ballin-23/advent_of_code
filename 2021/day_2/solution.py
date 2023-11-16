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

instructionArr = readFile("input.txt")

def determine_position(func):
    verticalPosition = 0
    horizontalPosition = 0

    for instruction in instructionArr:
        tokenizedInstruction = instruction.split()
        direction = tokenizedInstruction[0]
        num = int(tokenizedInstruction[1])
        verticalPosition, horizontalPosition = func(direction, num, verticalPosition, horizontalPosition)
    print("vertical position: ",verticalPosition,"horizontal position", horizontalPosition)
    print(horizontalPosition * verticalPosition)
    return horizontalPosition * verticalPosition

determine_position(handleInstructionPart1)
