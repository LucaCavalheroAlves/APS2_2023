import math


def ler_numeros_do_arquivo_txt(nome_do_arquivo):
    numeros = []
    with open(nome_do_arquivo, 'r') as arquivo_txt:
        for linha in arquivo_txt:
            # Converte a linha em um inteiro
            numeros.append(int(linha.strip()))

    return numeros


def bucket_sort(arr):
    max_val = max(arr)
    min_val = min(arr)

    buckets = [[] for _ in range(len(arr))]

    divisao_arredondada_cima = math.ceil((max_val - min_val) / len(arr))

    for num in arr:
        index = math.floor((num - min_val) / divisao_arredondada_cima)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    return buckets


nome_do_arquivo = "1000_numbers.txt"
arr = ler_numeros_do_arquivo_txt(nome_do_arquivo)
sorted_arr = bucket_sort(arr)
print(sorted_arr)
