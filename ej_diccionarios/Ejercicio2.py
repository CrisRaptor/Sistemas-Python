# Ejercicio 2: Crear un índice invertido
libros = {
"Cien años de soledad": ["Realismo mágico", "Drama"],
"El señor de los anillos": ["Fantasía", "Aventura"],
"1984": ["Distopía", "Política", "Drama"],
"Don Quijote": ["Clásico", "Aventura"]
}

invertido = {}

for libro, generos in libros.items():
    for genero in generos:
        if genero not in invertido.keys():
            invertido[genero] = [libro]
        else:
            invertido[genero].append(libro)

for genero, libros in invertido.items():
    print(genero, "{", libros, "}") 