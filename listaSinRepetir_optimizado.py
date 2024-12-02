my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista_sin_repetir = [my_list[0]]

for i in range(1,len(my_list)):
    existe = False
    cont = 0
    while (not existe and (cont < len(lista_sin_repetir))):
        if (my_list[i] == lista_sin_repetir[cont]):
            existe = True
        cont += 1
    if (not existe):
        lista_sin_repetir.append(my_list[i])

print("La lista completa:",my_list)
print("La lista con elementos únicos:",lista_sin_repetir)
