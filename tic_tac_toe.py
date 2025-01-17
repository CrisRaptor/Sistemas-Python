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
    print("Posiciones disponibles: ", freefields)
    while (not validated):
        try:
            pos = int(input("Indica una posicion válida para 'O': "))
            pos = ConvertNumberToPos(board,pos)
            print("Posicion elegida:",pos)
            if pos in freefields:
                validated = True
        except:
            print("Debes indicar un numero del 1 al 9")
    board[pos[0]][pos[1]] = "O"
    return VictoryFor(board, "O")

#Lista de espacios disponibles en board
def MakeListOfFreeFields(board):
    freefields = []
    for i in range(len(board)):
        for x in range(len(board[i])):
            if (board[i][x] != "X" and board[i][x] != "O"):
                freefields.append((i,x))
    return freefields

#Comprueba si el simbolo de sign ha ganado
def VictoryFor(board, sign):
    # victoria = False
    # temp = False
    # for x in range(len(board)):
    #     temp = False
    #       #Comprueba vertical (sin terminar)
    #     if (len(board[x]) <=3):
    #         tupla = ()
    #         for y in range(3):

    return ((board[0][0]==sign and board[0][1]== sign and board[0][2]==sign)or
            (board[1][0]==sign and board[1][1]==sign and board[1][2]==sign)or
            (board[2][0]==sign and board[2][1]==sign and board[2][2]==sign)or
            (board[0][0]==sign and board[1][0]==sign and board[2][0]== sign)or
            (board[0][1]==sign and board[1][1]==sign and board[2][1]==sign)or
            (board[0][2]==sign and board[1][2]==sign and board[2][2]==sign)or
            (board[0][0]==sign and board[1][1]==sign and board[2][2]==sign)or 
            (board[0][2]==sign and board[1][1]==sign and board[2][0]==sign))   

#Movimiento de la maquina aleatorio entre los disponibles
def DrawMove(board):
    lista = MakeListOfFreeFields(board)
    pos = randrange(len(lista))
    pos = lista[pos]
    board[pos[0]][pos[1]] = "X"
    return VictoryFor(board,"X")

#Convierte el numero de board en la tupla con la posicion
def ConvertNumberToPos(board, number):
    number -= 1
    row = (number // len(board[0]))
    column = (number % len(board))
    return (row,column)

##Main
#Variables
board = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9])
victoria = False
#Juego
jugador = str(input("Nombre: "))
while(not victoria and len(MakeListOfFreeFields(board))!=0):
    DisplayBoard(board)
    #Movimiento Jugador
    if EnterMove(board):
        victoria = True
        print("Victoria para", jugador)
    DisplayBoard(board)
    if not victoria:
        #Movimiento Maquina
        print("Movimiento de la maquina...")
        if DrawMove(board):
            victoria = True
            print("Victoria para Python")
if (not victoria and len(MakeListOfFreeFields(board))==0){
    print("No hay más movimiento disponibles.")
    print("empate")
}