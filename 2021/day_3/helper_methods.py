class helperClass:

    @classmethod
    def readFile(path):
        file_arr = []
        with open(path, 'r') as file:
            for line in file:
                file_arr.append(line.strip())
        return file_arr

    @classmethod
    def stringArrToNumArr(arr):
        return [int(x) for x in arr]
