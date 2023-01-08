def calculate_area(l,w,h):
    side1 = l * w
    side2 = w * h
    side3 = h * l
    extra = min(side1, side2, side3)
    return (side1*2) + (side2*2) + (side3*2) + extra

def calculate_volume(l,w,h):
    return l*w*h

def calculate_area_ribbon(l,w,h):
    side1 = l * w
    side2 = w * h
    side3 = h * l
    smallest_side = min(side1, side2, side3)
    if smallest_side == side1:
        return l + l + w + w
    elif smallest_side == side2:
        return w + w + h + h
    else:
        return h + h + l + l

def calculate_total_area():
    dimensions = open("input.txt", mode="r").readlines()
    area = 0
    for dimension in dimensions:
        arr = dimension.split("x")
        area += calculate_area_ribbon(int(arr[0]), int(arr[1]), int(arr[2]))
        area += calculate_volume(int(arr[0]), int(arr[1]), int(arr[2]))
    return area

print(calculate_total_area())