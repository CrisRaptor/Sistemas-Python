from random import randrange
#Muestra el tablero
def DisplayBoard(board):
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        cadena = ""
        for x in range(3):
            cadena += "|   " + str(board[i][x]) +"   "
        print(cadena,"|",sep="")
        print("|       |       |       |")
        print("+-------+-------+-------+")

#Movimiento del jugador
def EnterMove(board):
    validated = False
    pos = 0
    freefields = MakeListOfFreeFields(board)
    #print("Posiciones disponibles: ", freefields)
    while (not validated):
        try:
            pos = int(input("Indica una posicion válida para 'O': "))
            pos = ConvertNumberToPos(board,pos)
            if pos in freefields:
                validated = True
        except:
            print("Indica un numero del 1 al 9, válido")
    board[pos[0]-1][pos[1]-1] = "O"
    return VictoryFor(board, "O")

#Lista de espacios en blanco
def MakeListOfFreeFields(board):
    freefields = []
    for i in range(len(board)):
        for x in range(len(board[i])):
            if (board[i][x] != "X" and board[i][x] != "O"):
                freefields.append((i,x))
    return freefields

#Comprueba si el simbolo de sign ha ganado
def VictoryFor(board, sign):
    return ((board[0][0]==sign and board[0][1]== sign and board[0][2]==sign )or
            (board[1][0]==sign and board[1][1]==sign and board[1][2]==sign )or
            (board[2][0]==sign and board[2][1]==sign and board[2][2]==sign )or
            (board[0][0]==sign and board[1][0]==sign and board[2][0]== sign )or
            (board[0][1]==sign and board[1][1]==sign and board[2][1]==sign )or
            (board[0][2]==sign and board[1][2]==sign and board[2][2]==sign )or
            (board[0][0]==sign and board[1][1]==sign and board[2][2]==sign )or 
            (board[0][2]==sign and board[1][1]==sign and board[2][0]==sign ))

#Movimiento de la maquina
def DrawMove(board):
    pos = randrange(len(MakeListOfFreeFields(board)))
    pos = ConvertNumberToPos(board,pos)
    board[pos[0]-1][pos[1]-1] = "X"
    return VictoryFor(board,"X")

#Convierte el numero en la tupla con la posicion
def ConvertNumberToPos(board, number):
    row = (number % len(board))
    column = (number // len(board))
    return (row,column)

board = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9])
victoria = False
jugador = str(input("Nombre: "))
while(not victoria):
    DisplayBoard(board)
    if EnterMove(board):
        victoria = True
        print("Victoria para", jugador)
    print("Movimiento de la maquina...")
    DisplayBoard(board)
    if not victoria and DrawMove(board):
        victoria = True
        print("Victoria para Python")