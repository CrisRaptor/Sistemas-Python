# Ejercicio 1: Fusionar diccionarios con suma de valores
tienda1 = {"manzanas": 10, "naranjas": 15, "plátanos": 5}
tienda2 = {"manzanas": 8, "naranjas": 20, "uvas": 13}

tienda3 = tienda1.copy()
for producto, cantidad in tienda2.items():
    if producto in tienda3:
        tienda3[producto] += cantidad
    else:
        tienda3[producto] = cantidad

print(tienda3)