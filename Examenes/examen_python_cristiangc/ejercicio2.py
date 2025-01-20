#Funcion que cuenta la cantidad de apariciones de "letra_buscada" en "palabra"
def contar_letra(palabra, letra_buscada):
    apariciones = 0
    #Bucle que itera cada letra de "palabra" y la compara con la "letra_buscada"
    for letra in palabra:
        if letra == letra_buscada:
            apariciones += 1
    return apariciones

#Input
palabra = str(input("Entrada: "))
#Caracteres que se buscaran, se puede modificar
letras_buscadas = ["a","e","i","o","u"]
#Bucle que itera por cada elemento en la lista "letras_buscadas"
for letra_buscada in letras_buscadas:
    #Muestra un mensaje con la cantidad de apariciones
    print(str(letra_buscada),": ",str(contar_letra(palabra, letra_buscada)), sep="")