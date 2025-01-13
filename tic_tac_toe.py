board = [1,2,3,4,5,6,7,8,9]

#Muestra el tablero
def DisplayBoard(board):
    for i in 3:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for x in 3:
            print("|  ", board[x] ,"  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

#Input de la posicion
def EnterMove(board):
    pos = int(input("Indica una posicion válida para 'x': "))

#Lista de espacios en blanco
def MakeListOfFreeFields(board):
    freefields = []
    for i in board:
        if (i != "X" and i != "O"):
            freefields.append(i)
    return freefields

    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.

def VictoryFor(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    return -1

def DrawMove(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    return -1