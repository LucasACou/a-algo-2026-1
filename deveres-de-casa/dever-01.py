import random
import time

def insertion_sort(lista):
    """
    Aplica o algoritmo Insertion Sort em uma lista de números.

    Args:
        lista (list[int]): Lista de números a ser ordenada

    Returns:
        list[int]: Lista ordenada.
    """

    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = valor
        
    return lista

def gerador_lista(n):
    """
    Gera uma lista de números.

    Args:
        n (int): quantidade de números que teram na lista.

    Returns:
        list[int]: Lista de números aleatórios.
    """

    lista = [0] * n

    for i in range(0, n):
        numero = random.randint(1,500)
        lista[i] = numero

    return lista
    
def medir_tempo(func, lista):
    """
    Mede o tempo usada na execução de um algoritmo de ordenação.

    Args:
        func (function): Função de ordenação a ser medida.
        lista (list[int]): Lista de números a ser ordenada.

    Returns:
        float : Tempo de execução em segundos.
    """

    copia = lista.copy()

    inicio = time.perf_counter()
    resultado = func(copia)
    fim = time.perf_counter()

    return fim - inicio

lista_1k = gerador_lista(1000)
lista_5k = gerador_lista(5000)
lista_10k = gerador_lista(10000)
lista_20k = gerador_lista(20000)
lista_50k = gerador_lista(50000)

print('\ncomparação de tempo de sort de uma lista de 1000')
print('Insertion Sort:',medir_tempo(insertion_sort, lista_1k))
print('Pythin Sorted:',medir_tempo(sorted, lista_1k))

print('\ncomparação de tempo de sort de uma lista de 5000')
print('Insertion Sort:',medir_tempo(insertion_sort, lista_5k))
print('Pythin Sorted:',medir_tempo(sorted, lista_5k))

print('\ncomparação de tempo de sort de uma lista de 10000')
print('Insertion Sort:',medir_tempo(insertion_sort, lista_10k))
print('Pythin Sorted:',medir_tempo(sorted, lista_10k))

print('\ncomparação de tempo de sort de uma lista de 20000')
print('Insertion Sort:',medir_tempo(insertion_sort, lista_20k))
print('Pythin Sorted:',medir_tempo(sorted, lista_20k))

print('\ncomparação de tempo de sort de uma lista de 50000')
print('Insertion Sort:',medir_tempo(insertion_sort, lista_50k))
print('Pythin Sorted:',medir_tempo(sorted, lista_50k))