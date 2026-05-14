"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    qtd_x = 0
    qtd_o = 0

    for linha in board:
        for valor in linha:
            if valor == X:
                qtd_x += 1
            elif valor == O:
                qtd_o += 1

    if qtd_x > qtd_o:
        return O

    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    movimentos = set()

    for i in range(3):
        for j in range(3):

            if board[i][j] == EMPTY:
                movimentos.add((i, j))

    return movimentos


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    linha = action[0]
    coluna = action[1]

    if board[linha][coluna] != EMPTY:
        raise Exception("Jogada inválida")

    novo = []

    for l in board:
        novo.append(l.copy())

    novo[linha][coluna] = player(board)

    return novo


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # linhas
    for i in range(3):

        if board[i][0] == board[i][1] == board[i][2]:

            if board[i][0] is not None:
                return board[i][0]

    # colunas
    for j in range(3):

        if board[0][j] == board[1][j] == board[2][j]:

            if board[0][j] is not None:
                return board[0][j]

    # diagonal principal
    if board[0][0] == board[1][1] == board[2][2]:

        if board[0][0] is not None:
            return board[0][0]

    # diagonal secundaria
    if board[0][2] == board[1][1] == board[2][0]:

        if board[0][2] is not None:
            return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for linha in board:

        for valor in linha:

            if valor == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    ganhou = winner(board)

    if ganhou == X:
        return 1

    if ganhou == O:
        return -1

    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    vez = player(board)

    def valor(tabuleiro):

        if terminal(tabuleiro):
            return utility(tabuleiro)

        jogador_atual = player(tabuleiro)

        # X maximiza
        if jogador_atual == X:

            melhor = -math.inf

            for acao in actions(tabuleiro):

                resultado = valor(result(tabuleiro, acao))

                if resultado > melhor:
                    melhor = resultado

            return melhor

        # O minimiza
        else:

            melhor = math.inf

            for acao in actions(tabuleiro):

                resultado = valor(result(tabuleiro, acao))

                if resultado < melhor:
                    melhor = resultado

            return melhor

    melhor_jogada = None

    # Escolha para X
    if vez == X:

        melhor_valor = -math.inf

        for acao in actions(board):

            resultado = valor(result(board, acao))

            if resultado > melhor_valor:
                melhor_valor = resultado
                melhor_jogada = acao

    # Escolha para O
    else:

        melhor_valor = math.inf

        for acao in actions(board):

            resultado = valor(result(board, acao))

            if resultado < melhor_valor:
                melhor_valor = resultado
                melhor_jogada = acao

    return melhor_jogada