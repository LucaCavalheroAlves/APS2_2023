import math

# Função para ler números de um arquivo de texto e retornar uma lista de inteiros


def ler_numeros_do_arquivo_txt(nome_do_arquivo):
    numeros = []
    with open(nome_do_arquivo, 'r') as arquivo_txt:
        for linha in arquivo_txt:
            # Converte a linha em um inteiro
            numeros.append(int(linha.strip()))
    return numeros

# Função de ordenação Bucket Sort


def bucket_sort(arr):
    # Encontra o valor máximo e mínimo no array para determinar o intervalo
    max_val = max(arr)
    min_val = min(arr)

    # Cria um número de baldes igual ao tamanho do array
    buckets = [[] for _ in range(len(arr))]

    # Calcula o tamanho de intervalo de cada balde
    divisao_arredondada_cima = math.ceil((max_val - min_val) / len(arr))

    # Coloca cada elemento no balde apropriado
    for num in arr:
        index = math.floor((num - min_val) / divisao_arredondada_cima)
        buckets[index].append(num)

    # Ordena individualmente os elementos em cada balde
    for bucket in buckets:
        bucket.sort()

    return buckets


# Nome do arquivo de texto a ser lido
nome_do_arquivo = "1000_numbers.txt"

# Chama a função para ler os números do arquivo e armazená-los em 'arr'
arr = ler_numeros_do_arquivo_txt(nome_do_arquivo)

# Chama a função de ordenação Bucket Sort
sorted_arr = bucket_sort(arr)

# Imprime os baldes ordenados (baldes contendo elementos ordenados)
print(sorted_arr)
