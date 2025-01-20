my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista_sin_repetir = []

for i in range(len(my_list)):
    existe = True
    for j in range(len(lista_sin_repetir)):
        if (my_list[i] == lista_sin_repetir[j]):
            existe = False
    if (existe):
        lista_sin_repetir.append(my_list[i])

print("La lista completa:",my_list)
print("La lista con elementos únicos:",lista_sin_repetir)
