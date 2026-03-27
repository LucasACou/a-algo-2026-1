def recursao(n):
    """
    Calcula o valor da função recursiva:
    F(n) = 2*F(n-1) + n²

    Caso base:
    F(1) = 2

    Args:
        n (int): valor inteiro positivo

    Returns:
        int: resultado da função F(n)
    """

    # Caso base: quando n é 1, retorna 2
    if n == 1:
        return 2
    
    # Caso recursivo:
    # chama a função novamente com (n-1)
    # multiplica o resultado por 2
    # soma com n²
    return 2 * recursao(n - 1) + n**2
    

# Solicita ao usuário um número inteiro
n = int(input("Digite um número inteiro: "))

# Chama a função e imprime o resultado
print("Resultado:", recursao(n))