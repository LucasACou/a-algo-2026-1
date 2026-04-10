# ==== 3 - Recorrências ======
# a - Calculo de Recorrência: T(n) = 2T(n/4)+sqrt(n)

# aplicando teorema mestre:
#   a = 2
#   b = 4
#   f(n) = sqrt(n)

# então:
#   logb(a) = log4(2) = 1/2
#   n^(logb(a)) = n^(1/2)

# comparando:
#   f(n) = sqrt(n)
#   n^(logb(a)) = n^(1/2)
#   sao iguais = caso 2 teorema mestre

# Resultado: T(n) = O(sqrt(n) log n)

import math
print("\nT1:")
def T1(n):
    """
    Calcula recursivamente a recorrência:

        T(n) = 2T(n/4) + √n

    Args:
        n (int): Tamanho da entrada.

    Returns:
        float: Valor da recorrência para n.
    """

    if n <= 1:
        return 1
    return 2*T1(n//4) + math.sqrt(n)

for n in [4, 16, 64, 256]:
    print(n, T1(n))

# b - Calculo de Recorrência: T(n) = 2T(n/4)+n

# aplicando teorema mestre:
#   a = 2
#   b = 4
#   f(n) = n

# então:
#   logb(a) = log4(2) = 1/2
#   n^(logb(a)) = n^(1/2)

# comparando:
#   f(n) = n
#   n^(logb(a)) = n^(1/2)
#   n é maior = caso 3 teorema mestre

# Resultado: T(n) = O(n)
print("\nT2:")
def T2(n):
    """
    Calcula recursivamente a recorrência:

        T(n) = 2T(n/4) + n

    Args:
        n (int): Tamanho da entrada.

    Returns:
        int: Valor da recorrência para n.
    """

    if n <= 1:
        return 1
    return 2*T2(n//4) + n

for n in [4, 16, 64, 256]:
    print(n, T2(n))

# c - Calculo de Recorrência: T(n) = 16T(n/4)+n^2

# aplicando teorema mestre:
#   a = 16
#   b = 4
#   f(n) = n^2

# então:
#   logb(a) = log4(16) = 2
#   n^(logb(a)) = n^(2)

# comparando:
#   f(n) = n^2
#   n^(logb(a)) = n^2
#   sao iguais = caso 2 teorema mestre

# Resultado: T(n) = O(n^2 log n)

print("\nT3:")
def T3(n):
    """
    Calcula recursivamente a recorrência:

        T(n) = 16T(n/4) + n²

    Args:
        n (int): Tamanho da entrada.

    Returns:
        int: Valor da recorrência para n.
    """

    if n <= 1:
        return 1
    return 16*T3(n//4) + n**2

for n in [4, 16, 64]:
    print(n, T3(n))
