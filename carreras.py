class Carreras:
    def iniciarBusqueda(self, datos):
        self.__carreras__ = ["ARQ", "IAE", "IAG", "IEM", "IGEM", "IGGM", "IIGM", "IIMC", "IIMS", "IISL", "IM", "IMA", "ISCM", "ISCW", "LAMK", "LANI", "MPIA", "MPID", "MPIS"]
        self.__CrearArchivoDeCarreras__(datos)
        return self.__Faltan__(self.__carreras__[(self.__Seleccionar__(self.__Ultima__()))])
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
        try:
            ultimo = ""
            f = open("Ultima.txt", "r")
            for d in f:
                ultimo = d
            return ultimo
        except:
            return ""
    ##Esta en la lista la que sigue
    def __Faltan__(self, buscar):
        f = open("Carreras.txt", "r")
        for x in f:
            if buscar in x:
                return self.__NuevaUltima__(buscar)
        return self.__NuevaUltima__(self.__carreras__[0])
    ##Metodo que regresa la posicion de la lista para mandar a esa carrera
    def __Seleccionar__(self, ultima):
        if len(ultima) == 0:
            return 0
        else:
            for x in range(0, len(self.__carreras__)):
                if (self.__carreras__[x] == ultima):
                    if ((x+1) < len(self.__carreras__)):
                        return (x+1)
                    else:
                        return 0
        return 0
    ##Escribir la ultima carrera
    def __NuevaUltima__(self, dato):
        f = open("Ultima.txt", "w")
        f.write(dato)
        f.close()
        return dato