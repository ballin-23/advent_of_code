import itertools
def setup():
    return open("input.txt", mode="r").readlines()

def calculate_houses_with_present(directions):
    x1,y1 = 0,0
    x2,y2 = 0,0
    # santa_set = set({str(x1)+","+str(y1)})
    # robo_santa_set = set({str(x2)+","+str(y2)})
    coordinate_set = set({str(x1)+","+str(y1)})
    santas_turn = True
    for line in directions:
        for character in line:
            if santas_turn:
                x1,y1 = update_coordinates(x1,y1,character)
                coordinate_set.add(str(x1)+","+str(y1))
                santas_turn = False
            else:
                # case where it is robo santas turn
                x2,y2 = update_coordinates(x2,y2,character)
                coordinate_set.add(str(x2)+","+str(y2))
                santas_turn = True
    # final_set = set(itertools.chain(santa_set, robo_santa_set))
    return len(coordinate_set)

def update_coordinates(x,y,character):
    if character == ">":
        x += 1
    elif character == "<":
        x -= 1
    elif character == "^":
        y += 1
    else:
        y -= 1
    return x,y

directions = setup()
print(calculate_houses_with_present(directions))
