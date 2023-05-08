import hashlib


def computeHash(input):
    hash_object = hashlib.md5()
    hash_object.update(input.encode())
    hex_dig = hash_object.hexdigest()
    first_five = hex_dig[:5]
    return first_five

flag = True
counter = 200000
while flag:
    hashedValue = computeHash("ckczppom"+str(counter))
    if hashedValue == "000000":
        print("found at : ", counter)
        flag = False
    counter += 1

# print(computeHash("ckczppom1000000000"))

