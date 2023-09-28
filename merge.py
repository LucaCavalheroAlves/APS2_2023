# Função para ler números de um arquivo de texto e retornar uma lista de inteiros
def ler_txt(nome_do_arquivo):
    numeros = []
    with open(nome_do_arquivo, 'r') as arquivo_txt:
        for linha in arquivo_txt:
            # Converte a linha em um inteiro
            numeros.append(int(linha.strip()))
    return numeros
# Função que combina as duas metades ordenadas em um único array


def merged(metadeL, metadeR):

    merged = []
    L, R = 0, 0

    while L < len(metadeL) and R < len(metadeR):
        if metadeL[L] < metadeR[R]:
            merged.append(metadeL[L])
            L += 1
        else:
            merged.append(metadeR[R])
            R += 1

    # Adiciona os elementos restantes de ambas as metades, se houver
    merged.extend(metadeL[L:])
    merged.extend(metadeR[R:])

    return merged


# Função de ordenação Merge


def merge_sort(arr):
    # Caso base: se o array tiver 0 ou 1 elemento, ele já está ordenado
    if len(arr) <= 1:
        return arr

    # Divide o array ao meio
    mid = len(arr) // 2
    metadeL = arr[:mid]
    metadeR = arr[mid:]

    # Chama a função merge_sort recursivamente para as duas metades
    metadeL = merge_sort(metadeL)
    metadeR = merge_sort(metadeR)
    # Chama a função merged pra combinar as duas metades
    return merged(metadeL, metadeR)


# Nome do arquivo de texto a ser lido
txt = '1000_numbers.txt'

# Chama a função para ler os números do arquivo e armazená-los em 'numbers_array'
arr = ler_txt(txt)

# Imprime a lista original antes da ordenação
print("\nLista antes da ordenação:", arr)

# Chama a função de ordenação Merge Sort
array_ordenada = merge_sort(arr)

# Imprime a lista ordenada
print("\nLista ordenada:", array_ordenada)
