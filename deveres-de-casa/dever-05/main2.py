# ==== 2 - Multiplicação de matrizes ======
# Analise: 3 loops

# para calcular a recorrência de uma multiplicação de matrizes
# é preciso lembrar que esse calculo utiliza-se 3 loops

# então:
#   n*n*n = n^3

# Resultado: O(n^3)

import time
import random

def gerar_matriz(n):
    """
    Gera uma matriz quadrada de dimensão n x n com valores aleatórios.

    Cada elemento da matriz é um número inteiro entre 0 e 10.

    Args:
        n (int): Tamanho da matriz (número de linhas e colunas).

    Returns:
        list: Matriz (lista de listas) de dimensão n x n preenchida
              com valores aleatórios.
    """
    return [[random.randint(0, 10) for _ in range(n)] for _ in range(n)]

def multiplicar(A, B):
    """
    Realiza a multiplicação de duas matrizes quadradas A e B.

    A multiplicação segue a definição clássica:
    cada elemento da posição (i, j) é a soma dos produtos
    dos elementos da linha i de A pelos elementos da coluna j de B.

    Args:
        A (list): Matriz quadrada n x n.
        B (list): Matriz quadrada n x n.

    Returns:
        list: Matriz resultado da multiplicação A x B.
    """

    n = len(A)
    resultado = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                resultado[i][j] += A[i][k] * B[k][j]

    return resultado


for n in [50, 100, 150]:
    A = gerar_matriz(n)
    B = gerar_matriz(n)

    inicio = time.time()
    multiplicar(A, B)
    fim = time.time()

    print(f"N={n} | Tempo={fim - inicio:.6f}s")
