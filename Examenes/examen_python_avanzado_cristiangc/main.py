class Libro: #Clase libros
    
    #Constructor
    def __init__(self, titulo = "titulo desconocido", autor = "autor desconocido", 
                 editorial = "editorial desconocida", precio = 100, año_publicacion = 2000):
        self.titulo = titulo.strip()
        self.autor = autor.strip()
        self.editorial = editorial.strip()
        self.precio = precio
        self.año_publicacion = año_publicacion
        return

    #Metodo de mostrar informacion
    def mostrar_informacion(self):
        print("*************************\nTítulo:",self.titulo,
              "\nAutor:",self.autor,"\nEditorial:",self.editorial,
              "\nAño:",str(self.año_publicacion),"\nPrecio:",str(self.precio))

    #Metodo para aplicar descuento    
    def aplicar_descuento(self, porcentaje_descuento = 0.0):
        #Comprueba si el descuento es valido
        if (porcentaje_descuento > 100 or porcentaje_descuento < 0):
            return self.precio
        #Descuenta precio calculando el valor porcentual (0.0 - 1.0)
        self.precio = self.precio * ((100.0-porcentaje_descuento)/100)
        return self.precio
    
    #Compara el precio de 2 libros
    def comparar_precio(self, libro):
        try: #Posible excepcion por pasar algo que no sea de clase Libro
            if self.precio == libro.precio:
                print("Los libros poseen el mismo precio.")
                return
            if self.precio > libro.precio:
                print("El libro",self.titulo,"es más caro.")
                return
            print("El libro",libro.titulo,"es más caro.")
            return
        except BaseException:
            print("Error al comparar precios")
        return

class LibroElectronico(Libro): #Clase libro electronico
    #Atributos adicionales
    __formatos_validos = ["PDF","ePub","Mobi"] #Formatos permitidos

    #Constructor
    def __init__(self, titulo="titulo desconocido", autor="autor desconocido", 
                 editorial="editorial desconocida", precio=100.0, año_publicacion=2000,
                 formato="PDF"):
        super().__init__(titulo, autor, editorial, precio, año_publicacion)
        if self.comprobar_formato(formato):
            self.formato = formato
            return
        else:
            return Exception("Formato incorrecto")

    #Metodo para comprobar si el formato se encuentra entre los formatos validos
    def comprobar_formato(self, formato):
        for formato_valido in self.__formatos_validos:
            if formato_valido == formato:
                return True
        return False
    
    #Metodo que muestra una descarga
    def descargar(self):
        print("El libro",self.titulo,"se ha descargado en formato",self.formato)
        return
    
    #Mostrar informacion
    def mostrar_informacion_electronica(self):
        self.mostrar_informacion()
        print("Formato:",self.formato)

    #Metodo para cambiar un formato
    def cambiar_formato(self, formato):
        if self.comprobar_formato(formato):
            self.formato = formato
        return

catalogo = []
#Inicializacion
libro1 = Libro("Un mundo feliz","Aldous Huxley","Plaza & Janés", 19.90, 1932)
libro2 = Libro("Canción de hielo y fuego","George R.R.Martin","Gigamesh", 30, 1996)
libro_electronico = LibroElectronico("El Hobbit","J.R.R Tolkien","Minotauro", 4.95, 1937, "ePub")
#Añadimos al catalogo
catalogo.append(libro1.titulo)
catalogo.append(libro2.titulo)
catalogo.append(libro_electronico.titulo)

#Mostrar
print("---- Mostrando informacion ----")
libro1.mostrar_informacion()
libro2.mostrar_informacion()
libro_electronico.mostrar_informacion_electronica()
libro_electronico.descargar()

#Descuento
print("---- Mostrando descuento ----")
libro2.aplicar_descuento(30.0)
libro2.mostrar_informacion()

#Comparar precios
print("---- Mostrando comparacion de precios ----")
libro1.comparar_precio(libro2)

#Cambiar formato
print("---- Mostrando cambio de formato ----")
libro_electronico.cambiar_formato("PDF")
libro_electronico.mostrar_informacion_electronica()

#Mostrar catalogo
print("---- Mostrando catalogo ----")
print(catalogo)