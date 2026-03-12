import time
import sys

# Aumentado o limite de recursão do python para 2000
sys.setrecursionlimit(2000)

def medir_tempo(func, n):
    """
    Mede o tempo usada na execução de um algoritmo de fatorial.

    Args:
        func (function): Função de fatorial a ser medida.
        n [int] : Número usado para calcular o fatorial.

    Returns:
        int : Tempo de execução em segundos.
    """

    # Guarda o tempo inicial.
    inicio = time.perf_counter()

    # Executa a função passada no parâmetro.
    resultado = func(n)

    # Guarda o tempo final.
    fim = time.perf_counter()

    # Retorna a diferença entre o tmepo final e o inicial,
    # sendo assim o tempo total de execução da função.
    return fim - inicio

def fatorial(n):
    """
    Calcula o fatorial de um numero através do uso de recursão.

    A complexidade assintótica desse algoritmo é O(n),
    pois o número de chamadas recursivas cresce linearmente
    com o valor de n. Cada chamada da função executa apenas
    uma multiplicação e uma nova chamada recursiva até atingir
    o caso base.

    Args:
        n [int] : Número usado para calcular o fatorial.

    Returns:
        float : Resultado do cálculo fatorial.
    """
    # Caso recursivo:
    # se n for maior que 1, multiplica-se n pelo fatorial de n-1
    # e chama a função novamente até atingir o caso base.
    if n > 1: 
        return n * fatorial(n-1)
    
    # Caso base:
    # quando n chega a 1 ou menor, retorna 1
    #encerrando as chamadas recursivas.
    return 1

# Lê um numero n e calculo o fatorial com aquele valor.
n = int(input("Digite um número inteiro: "))
print("Fatorial:", fatorial(n))
    
# Teste do algoritmo para diferentes valores de n
# e medição do tempo de execução.
print('\nmedição de tempo do calculo de fatorial de 10 usando recursividade')
print('Fatorial N = 10:',medir_tempo(fatorial, 10), "segundos")

print('\nmedição de tempo do calculo de fatorial de 100 usando recursividade')
print('Fatorial N = 100:',medir_tempo(fatorial, 100), "segundos")

print('\nmedição de tempo do calculo de fatorial de 500 usando recursividade')
print('Fatorial N = 500:',medir_tempo(fatorial, 500), "segundos")

print('\nmedição de tempo do calculo de fatorial de 1000 usando recursividade')
print('Fatorial N = 1000:',medir_tempo(fatorial, 1000), "segundos")