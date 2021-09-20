class Carreras:
    def iniciarBusqueda(self, datos):
        self.__carreras__ = ["ARQ","IAE","IAG","IEM","IGEM","IGGM","IIGM","IIMC","IIMS","IISL","IM","IMA","ISCM","ISCW","LAMK","LANI","MPIA","MPID","MPIS"]
        self.__CrearArchivoDeCarreras__(datos)
        return self.__CarreraSeleccionada__(self.__Seleccionar__(self.__Ultima__()))
    ##Metodo para crear el archvio de carreras
    def __CrearArchivoDeCarreras__(self, datos):
        f = open("Carreras.txt", "w")
        cont = 0
        enLista = []
        for i in datos:
            if self.__Esta__(i['Carrera'], enLista):
                if cont == 0:
                    f.write(i['Carrera'])
                else:
                    f.write("\n" + i['Carrera'])
                cont += 1
                enLista.append(i['Carrera'])
        f.close()
    ##Metodo que sirve para no repetir las carreras en el archivo
    def __Esta__(self, dato, lista):
        for i in lista:
            if dato in i:
                return False
        return True
    ##Metodo para sacar la ultima carrera a la que se envio el mensaje
    def __Ultima__(self):
        f = open("Ultima.txt", "r")
        ultimo = ""
        for d in f:
            ultimo = d
        return ultimo
    ##Metodo que regresa la posicion de la lista para mandar a esa carrera
    def __Seleccionar__(self, ultima):
        if len(ultima) == 0:
            print("Caso 1")
            return 0
        else:
            for x in range(0, len(self.__carreras__)):
                if (self.__carreras__[x] == ultima):
                    if ((x+1) < len(self.__carreras__)):
                        print("Caso 2")
                        return (x+1)
                    else:
                        print("Caso 3")
                        return 0
        print("Caso 4")
        return 0
    ##Escribir la ultima carrera
    def __NuevaUltima__(self, dato):
        f = open("Ultima.txt", "w")
        f.write(dato)
        f.close()
    ##Metodo que retorna la carrera a mandar el correo
    def __CarreraSeleccionada__(self, pos):
        selecionada = self.__carreras__[pos]
        self.__NuevaUltima__(selecionada)
        return selecionada