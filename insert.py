def ler_numeros_do_arquivo_txt(nome_do_arquivo):
    numeros = []
    with open(nome_do_arquivo, 'r') as arquivo_txt:
        for linha in arquivo_txt:
            # Converte a linha em um inteiro
            numeros.append(int(linha.strip()))
    return numeros


def insertion_sort(arr):

    for i in range(1, len(arr)):
        element = arr[i]
        j = i
        while j > 0 and element < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = element

    return arr


txt = '1000_numbers.txt'
numbers_array = ler_numeros_do_arquivo_txt(txt)

print("Array original:", numbers_array)
arrayorganizada = insertion_sort(numbers_array)
print("Array ordenado:", arrayorganizada)
