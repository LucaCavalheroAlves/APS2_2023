def insertion_sort(arr):
    array = list(array)

    for i in range(1, len(array)):
        element = array[i]
        j = i
        while j > 0 and element < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = element

    return array


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

print("Array original:", numbers_array)
arrayorganizada = insertion_sort(numbers_array)
print("Array ordenado:", arrayorganizada)
