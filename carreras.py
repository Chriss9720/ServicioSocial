class Carreras:
    def iniciarBusqueda(self, datos):
        self.__carreras__ = ["ARQ", "IA", "IAE", "IAG", "IEM", "IGEM", "IGGM", "II","IIGM", "IIMC", "IIMS", "IISL", "IM", "IMA", "ISCM", "ISCW", "LAMK", "LANI", "MPIA", "MPID", "MPIS"]
        data = self.__CrearArchivoDeCarreras__(datos)
        pos = (self.__Seleccionar__(self.__Ultima__()))
        return self.__Faltan__(self.__carreras__[pos], pos, data)
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
        return enLista
    ##Metodo que sirve para no repetir las carreras en el archivo
    def __Esta__(self, dato, lista):
        for i in lista:
            if dato == i:
                return False
        return True
    ##Metodo para buscar la carrera en la lista
    def __Ultima__(self):
        try:
            ultimo = ""
            f = open("Ultima.txt", "r")
            for d in f:
                ultimo = d
            return ultimo
        except Exception as e:
            print(f"Carrara.py: {e}")
            return ""
    ##Esta en la lista la que sigue
    def __Faltan__(self, buscar, pos, data):
        f = open("Carreras.txt", "r")
        encontrado = False
        for x in data:
            if (not encontrado and buscar in x):
                encontrado = True
        if (encontrado):
            return buscar
        else:
            if(pos < len(data)):
                return data[pos]
            else:
                return data[0]
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