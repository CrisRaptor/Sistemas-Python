#Esta funcion comprueba si el numero es capicua
def comprobar_capicua(numero):
    #"contador" calcula la mitad del tamaño del numero (la cantidad de iteraciones)
    contador = int(len(numero))//2
    #este bucle compara el numero de la posicion i con su contrario, devuelve False si encuentra 1 diferencia
    for i in range(contador):
        if numero[i] != numero[-(i+1)]:
            return False
    #devuelve True si no se ha encontrado diferencias
    return True

#Input
entrada = input("Indica un numero capicua: ")
#Salida, condicional que usa el metodo "comprobar_capicua"
if (comprobar_capicua(str(entrada))):
    print("El numero", str(entrada), "es capicua.")
else:
    print("El numero", str(entrada), "NO es capicua.")