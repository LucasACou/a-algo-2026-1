# ==== 1 - Algoritmo de ordenação Merge Sort ======
# Calculo de Recorrência: T(n) = 2T(n/2)+n

# aplicando teorema mestre:
#   a = 2
#   b = 2
#   f(n) = n

# então:
#   logb(a) = log2(2) = 1
#   n^(logb(a)) = n^1 = n

# comparando:
#   f(n) = n
#   n^(logb(a)) = n^1 = n
#   sao iguais = caso 2 teorema

# Resultado: T(n) = O(n log n)

import time
import random

def merge_sort(arr):
    """
    Ordena uma lista utilizando o algoritmo Merge Sort.

    O algoritmo divide a lista em duas partes, ordena cada parte
    recursivamente e depois realiza a junção (merge) das duas
    listas ordenadas.

    Args:
        arr (list): Lista de elementos a serem ordenados.

    Returns:
        list: Nova lista contendo os elementos ordenados.
    """

    if len(arr) <= 1:
        return arr

    meio = len(arr) // 2
    esquerda = merge_sort(arr[:meio])
    direita = merge_sort(arr[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    """
    Realiza a junção (merge) de duas listas já ordenadas.

    Compara os elementos das duas listas e constrói uma nova
    lista ordenada contendo todos os elementos.

    Args:
        esquerda (list): Lista ordenada da metade esquerda.
        direita (list): Lista ordenada da metade direita.

    Returns:
        list: Lista ordenada contendo todos os elementos de
              esquerda e direita.
    """

    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


# Teste de tempo
for n in [1000, 2000, 4000, 8000]:
    arr = [random.randint(0, 10000) for _ in range(n)]

    inicio = time.time()
    merge_sort(arr)
    fim = time.time()

    print(f"N={n} | Tempo={fim - inicio:.6f}s")


