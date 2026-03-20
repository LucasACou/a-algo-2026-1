def palindromo(lista, inicio=0, fim=None):
    """
    Verifica recursivamente se uma lista é um palíndromo.

    Um palíndromo é uma sequência que permanece igual quando lida
    da esquerda para a direita e da direita para a esquerda.

    Args:
        lista (list): Lista de elementos a ser verificada.
        inicio (int, opcional): Índice inicial para comparação. Default é 0.
        fim (int, opcional): Índice final para comparação. Default é None,
                             sendo definido como o último índice da lista.

    Returns:
        str: "É palíndromo" se a lista for um palíndromo,
             "Não é palíndromo" caso contrário.
    """
    # Define o fim na primeira chamada
    if fim is None:
        fim = len(lista) - 1

    # Caso base: passou do meio
    if inicio >= fim:
        return "É palíndromo"

    # Se elementos diferentes, não é palíndromo
    if lista[inicio] != lista[fim]:
        return "Não é palíndromo"

    # Chamada recursiva avançando para o centro
    return palindromo(lista, inicio + 1, fim - 1)
    
array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print(palindromo(array1))  # True
print(palindromo(array2))  # True
print(palindromo(array3))  # True
print(palindromo(array4))  # False