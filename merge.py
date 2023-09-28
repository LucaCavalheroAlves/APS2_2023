def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    metadeL = arr[:mid]
    metadeR = arr[mid:]

    metadeL = merge_sort(metadeL)
    metadeR = merge_sort(metadeR)

    merged = []
    L, R = 0, 0

    while L < len(metadeL) and R < len(metadeR):
        if metadeL[L] < metadeR[R]:
            merged.append(metadeL[L])
            L += 1
        else:
            merged.append(metadeR[R])
            R += 1

    merged.extend(metadeL[L:])
    merged.extend(metadeR[R:])
    return merged


def ler_txt(file_path):
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.isdigit():
                numbers.append(int(line))
    return numbers


txt = 'C:\\Users\\lucac\\OneDrive\\workspace\\facul\\lalala.txt'
numbers_array = ler_txt(txt)


print("Lista antes da ordenação:", numbers_array)


arrayorganizada = merge_sort(numbers_array)
print("Lista ordenada:", arrayorganizada)
